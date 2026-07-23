#!/usr/bin/env python3
"""Deterministic, network-free documentation validation for QSO-DIGITALIS."""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path
from typing import Iterable

REQUIRED_FILES = (
    "README.md",
    "docs/index.md",
    "docs/project-overview.md",
    "docs/architecture.md",
    "docs/contract-boundary.md",
    "docs/onboarding.md",
    "docs/developer-guide.md",
    "taskchain.md",
    "punchlist.md",
    "release.md",
    "changelog.md",
    ".consent/consent-capacity-lock-v1.json",
)

REQUIRED_README_ROUTES = (
    "docs/index.md",
    "docs/project-overview.md",
    "docs/architecture.md",
    "docs/contract-boundary.md",
    "docs/onboarding.md",
    "docs/developer-guide.md",
    "taskchain.md",
    "punchlist.md",
    "release.md",
    "changelog.md",
)

PLANNING_FILES = ("taskchain.md", "punchlist.md", "release.md", "changelog.md")
LINK_RE = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
EXTERNAL_SCHEMES = ("http://", "https://", "mailto:", "tel:", "#")


def read_utf8(path: Path) -> str:
    return path.read_bytes().decode("utf-8", errors="strict")


def iter_markdown(root: Path) -> Iterable[Path]:
    for path in sorted(root.rglob("*.md")):
        if ".git" not in path.parts:
            yield path


def normalize_link(source: Path, target: str) -> Path | None:
    clean = target.split("#", 1)[0].split("?", 1)[0].strip()
    if not clean or clean.startswith(EXTERNAL_SCHEMES):
        return None
    return (source.parent / clean).resolve()


def validate(root: Path) -> dict[str, object]:
    findings: list[str] = []
    checked: list[str] = []

    for rel in REQUIRED_FILES:
        path = root / rel
        if not path.is_file():
            findings.append(f"missing required file: {rel}")
            continue
        try:
            read_utf8(path)
        except UnicodeDecodeError:
            findings.append(f"invalid UTF-8: {rel}")
        checked.append(rel)

    if findings:
        return report(root, checked, findings)

    consent = json.loads(read_utf8(root / ".consent/consent-capacity-lock-v1.json"))
    if consent.get("policy_id") != "QSO-CONSENT-CAPACITY-LOCK-v1":
        findings.append("consent policy identifier changed")
    if consent.get("status") != "immutable":
        findings.append("consent policy is not immutable")
    if consent.get("lock_response", {}).get("automatic_unlock") is not False:
        findings.append("consent policy permits automatic unlock")

    readme = read_utf8(root / "README.md")
    for route in REQUIRED_README_ROUTES:
        if f"({route})" not in readme:
            findings.append(f"README missing route: {route}")
    for marker in (
        "REVIEW — CHARTER OR RETIREMENT DECISION REQUIRED",
        "QSO-CONSENT-CAPACITY-LOCK-v1",
        "documentation-first charter candidate",
        "Pages publication",
        "012-M",
    ):
        if marker not in readme:
            findings.append(f"README missing marker: {marker}")

    architecture = read_utf8(root / "docs/architecture.md")
    if "```mermaid" not in architecture:
        findings.append("architecture diagram missing")
    if "**Equivalent prose:**" not in architecture:
        findings.append("architecture diagram lacks equivalent prose")
    if "Architectural obstruction" not in architecture:
        findings.append("architecture obstruction register missing")

    overview = read_utf8(root / "docs/project-overview.md")
    for heading in ("## Purpose", "## Intended readers", "## Maturity", "## Non-goals"):
        if heading not in overview:
            findings.append(f"project overview missing heading: {heading}")

    contract = read_utf8(root / "docs/contract-boundary.md")
    for marker in ("## Contract acceptance tuple", "## Gluing conditions", "## Current obstruction register"):
        if marker not in contract:
            findings.append(f"contract boundary missing marker: {marker}")

    onboarding = read_utf8(root / "docs/onboarding.md")
    developer = read_utf8(root / "docs/developer-guide.md")
    if "python3 scripts/check_documentation.py" not in onboarding:
        findings.append("onboarding lacks first validation command")
    if "No documentation contribution can independently authorize" not in developer:
        findings.append("developer guide lacks release authority boundary")

    for rel in PLANNING_FILES:
        text = read_utf8(root / rel)
        if "PR #2" not in text:
            findings.append(f"{rel} does not classify PR #2")
        if "stale" not in text.lower():
            findings.append(f"{rel} does not mark stale candidate state")
        if "deployment" not in text.lower():
            findings.append(f"{rel} lacks deployment boundary")

    taskchain = read_utf8(root / "taskchain.md")
    release = read_utf8(root / "release.md")
    punchlist = read_utf8(root / "punchlist.md")
    if "P0.2" not in taskchain or "P0.2" not in punchlist:
        findings.append("charter decision gate P0.2 is not synchronized")
    if "BLOCKED — DOCUMENTATION CANDIDATE IN REVIEW" not in release:
        findings.append("release status is not documentation-candidate blocked")

    root_resolved = root.resolve()
    for path in iter_markdown(root):
        rel = path.relative_to(root).as_posix()
        try:
            text = read_utf8(path)
        except UnicodeDecodeError:
            continue
        for match in LINK_RE.finditer(text):
            target = normalize_link(path, match.group(1))
            if target is None:
                continue
            try:
                target.relative_to(root_resolved)
            except ValueError:
                findings.append(f"link escapes repository: {rel} -> {match.group(1)}")
                continue
            if not target.exists():
                findings.append(f"broken link: {rel} -> {match.group(1)}")

    prohibited_promotions = (
        "passing ci approves the charter",
        "documentation authorizes deployment",
        "mergeability establishes compatibility",
        "digest proves semantic truth",
    )
    for path in iter_markdown(root):
        text = read_utf8(path).lower()
        for phrase in prohibited_promotions:
            if phrase in text:
                findings.append(f"authority promotion in {path.relative_to(root)}: {phrase}")

    return report(root, checked, findings)


def report(root: Path, checked: list[str], findings: list[str]) -> dict[str, object]:
    hashes: dict[str, str] = {}
    for rel in sorted(set(checked)):
        path = root / rel
        if path.is_file():
            hashes[rel] = hashlib.sha256(path.read_bytes()).hexdigest()
    return {
        "profile": "QSO-DIGITALIS-DOCUMENTATION-CANDIDATE-001",
        "status": "PASS" if not findings else "FAIL_CLOSED",
        "checked_files": sorted(set(checked)),
        "file_sha256": hashes,
        "findings": sorted(set(findings)),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=".")
    parser.add_argument("--output")
    args = parser.parse_args()
    try:
        result = validate(Path(args.root))
    except Exception as exc:
        result = {
            "profile": "QSO-DIGITALIS-DOCUMENTATION-CANDIDATE-001",
            "status": "FAIL_CLOSED",
            "checked_files": [],
            "file_sha256": {},
            "findings": [f"validator exception: {type(exc).__name__}: {exc}"],
        }
    rendered = json.dumps(result, indent=2, sort_keys=True)
    if args.output:
        Path(args.output).write_text(rendered + "\n", encoding="utf-8")
    print(rendered)
    return 0 if result["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
