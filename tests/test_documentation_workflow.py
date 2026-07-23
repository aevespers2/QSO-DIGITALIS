from __future__ import annotations

import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
WORKFLOW = ROOT / ".github" / "workflows" / "documentation-candidate.yml"
SHA40 = re.compile(r"^[0-9a-f]{40}$")
USES = re.compile(r"(?m)^\s*-?\s*uses:\s*([^\s#]+)")


class DocumentationWorkflowTests(unittest.TestCase):
    def source(self) -> str:
        return WORKFLOW.read_text(encoding="utf-8")

    def test_actions_are_sha_pinned_and_checkout_is_read_only(self):
        source = self.source()
        for action in USES.findall(source):
            action = action.strip("\"'")
            if action.startswith("./"):
                continue
            self.assertIn("@", action)
            self.assertRegex(action.rsplit("@", 1)[1], SHA40)
        self.assertIn("persist-credentials: false", source)
        self.assertIn("permissions:\n  contents: read", source)

    def test_concurrency_is_exact_head_and_does_not_cancel_evidence(self):
        source = self.source()
        self.assertIn(
            "group: qso-digitalis-documentation-${{ github.event.pull_request.head.sha || github.sha }}",
            source,
        )
        self.assertIn("cancel-in-progress: false", source)

    def test_failure_paths_preserve_artifacts_before_final_gate(self):
        source = self.source()
        self.assertIn("- name: Initialize evidence context", source)
        self.assertIn("- name: Upload retained evidence\n        id: upload\n        if: always()", source)
        self.assertIn("- name: Fail closed on unsuccessful validation\n        if: always()", source)
        self.assertLess(
            source.index("- name: Upload retained evidence"),
            source.index("- name: Fail closed on unsuccessful validation"),
        )
        for marker in (
            "CHECKOUT_OUTCOME",
            "PYTHON_OUTCOME",
            "SOURCE_STATUS",
            "VALIDATOR_STATUS",
            "TEST_STATUS",
            "HASH_STATUS",
            "UPLOAD_OUTCOME",
        ):
            self.assertIn(marker, source)

    def test_workflow_self_test_is_required_and_hashed(self):
        source = self.source()
        self.assertGreaterEqual(source.count("tests/test_documentation_workflow.py"), 3)
        self.assertIn(
            "python3 -m unittest tests.test_check_documentation tests.test_documentation_workflow -v",
            source,
        )


if __name__ == "__main__":
    unittest.main()
