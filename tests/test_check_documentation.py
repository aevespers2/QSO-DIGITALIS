from __future__ import annotations

import importlib.util
import shutil
import tempfile
import unittest
from pathlib import Path

MODULE_PATH = Path(__file__).parents[1] / "scripts" / "check_documentation.py"
spec = importlib.util.spec_from_file_location("check_documentation", MODULE_PATH)
module = importlib.util.module_from_spec(spec)
assert spec and spec.loader
spec.loader.exec_module(module)


class DocumentationValidationTests(unittest.TestCase):
    def make_tree(self) -> tuple[tempfile.TemporaryDirectory, Path]:
        temp = tempfile.TemporaryDirectory()
        root = Path(temp.name)
        source = Path(__file__).parents[1]
        for rel in module.REQUIRED_FILES:
            src = source / rel
            dst = root / rel
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(src, dst)
        return temp, root

    def test_repository_documentation_passes(self):
        result = module.validate(Path(__file__).parents[1])
        self.assertEqual(result["status"], "PASS", result["findings"])

    def test_missing_required_route_fails(self):
        temp, root = self.make_tree()
        try:
            (root / "docs/onboarding.md").unlink()
            result = module.validate(root)
            self.assertEqual(result["status"], "FAIL_CLOSED")
            self.assertTrue(any("missing required file" in x for x in result["findings"]))
        finally:
            temp.cleanup()

    def test_missing_decision_packet_fails(self):
        temp, root = self.make_tree()
        try:
            (root / "docs/charter-decision-packet.md").unlink()
            result = module.validate(root)
            self.assertEqual(result["status"], "FAIL_CLOSED")
            self.assertTrue(any("missing required file" in x for x in result["findings"]))
        finally:
            temp.cleanup()

    def test_broken_internal_link_fails(self):
        temp, root = self.make_tree()
        try:
            readme = root / "README.md"
            readme.write_text(readme.read_text(encoding="utf-8") + "\n[Broken](docs/missing.md)\n", encoding="utf-8")
            result = module.validate(root)
            self.assertTrue(any("broken link" in x for x in result["findings"]))
        finally:
            temp.cleanup()

    def test_diagram_without_prose_fails(self):
        temp, root = self.make_tree()
        try:
            path = root / "docs/architecture.md"
            path.write_text(path.read_text(encoding="utf-8").replace("**Equivalent prose:**", "Equivalent description:"), encoding="utf-8")
            result = module.validate(root)
            self.assertTrue(any("equivalent prose" in x for x in result["findings"]))
        finally:
            temp.cleanup()

    def test_decision_record_option_drift_fails(self):
        temp, root = self.make_tree()
        try:
            path = root / "docs/charter-decision-packet.md"
            path.write_text(path.read_text(encoding="utf-8").replace("APPROVE_BOUNDED_CHARTER", "APPROVE"), encoding="utf-8")
            result = module.validate(root)
            self.assertTrue(any("charter decision packet missing marker" in x for x in result["findings"]))
        finally:
            temp.cleanup()

    def test_retirement_rollback_route_is_required(self):
        temp, root = self.make_tree()
        try:
            path = root / "docs/retirement-migration-guide.md"
            path.write_text(path.read_text(encoding="utf-8").replace("## Rollback and restoration", "## Recovery notes"), encoding="utf-8")
            result = module.validate(root)
            self.assertTrue(any("retirement guide missing marker" in x for x in result["findings"]))
        finally:
            temp.cleanup()

    def test_accessibility_400_percent_review_is_required(self):
        temp, root = self.make_tree()
        try:
            path = root / "docs/accessibility-review.md"
            path.write_text(path.read_text(encoding="utf-8").replace("400%", "four-hundred percent"), encoding="utf-8")
            result = module.validate(root)
            self.assertTrue(any("accessibility review missing marker: 400%" in x for x in result["findings"]))
        finally:
            temp.cleanup()

    def test_stale_candidate_classification_is_required(self):
        temp, root = self.make_tree()
        try:
            path = root / "release.md"
            text = path.read_text(encoding="utf-8")
            path.write_text(text.replace("stale", "superseded-candidate").replace("Stale", "Superseded-candidate"), encoding="utf-8")
            result = module.validate(root)
            self.assertTrue(any("does not mark stale" in x for x in result["findings"]))
        finally:
            temp.cleanup()

    def test_planning_decision_packet_alignment_is_required(self):
        temp, root = self.make_tree()
        try:
            path = root / "changelog.md"
            path.write_text(path.read_text(encoding="utf-8").replace("decision packet", "decision worksheet"), encoding="utf-8")
            result = module.validate(root)
            self.assertTrue(any("lacks decision-packet alignment" in x for x in result["findings"]))
        finally:
            temp.cleanup()

    def test_consent_policy_identifier_drift_fails(self):
        temp, root = self.make_tree()
        try:
            path = root / ".consent/consent-capacity-lock-v1.json"
            path.write_text(path.read_text(encoding="utf-8").replace("QSO-CONSENT-CAPACITY-LOCK-v1", "DRIFTED"), encoding="utf-8")
            result = module.validate(root)
            self.assertTrue(any("consent policy identifier changed" in x for x in result["findings"]))
        finally:
            temp.cleanup()

    def test_invalid_utf8_fails_closed(self):
        temp, root = self.make_tree()
        try:
            (root / "docs/index.md").write_bytes(b"# Docs\n\xff")
            result = module.validate(root)
            self.assertEqual(result["status"], "FAIL_CLOSED")
            self.assertTrue(any("invalid UTF-8" in x for x in result["findings"]))
        finally:
            temp.cleanup()

    def test_authority_promotion_fails(self):
        temp, root = self.make_tree()
        try:
            path = root / "docs/index.md"
            path.write_text(path.read_text(encoding="utf-8") + "\nPassing CI approves the charter.\n", encoding="utf-8")
            result = module.validate(root)
            self.assertTrue(any("authority promotion" in x for x in result["findings"]))
        finally:
            temp.cleanup()

    def test_source_review_cannot_promote_rendered_accessibility(self):
        temp, root = self.make_tree()
        try:
            path = root / "docs/accessibility-review.md"
            path.write_text(path.read_text(encoding="utf-8") + "\nSource review proves rendered accessibility.\n", encoding="utf-8")
            result = module.validate(root)
            self.assertTrue(any("authority promotion" in x for x in result["findings"]))
        finally:
            temp.cleanup()


if __name__ == "__main__":
    unittest.main()
