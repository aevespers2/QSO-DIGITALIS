"""Materialize the Digital Consciousness Field scaffold.

Phase: bounded shared-field development.
Stages: contracts, implementation, verification, integration, release.
Tasks: validate the scaffold plan, create missing files, preserve existing work, render unique roadmaps, and require exact-head review.
Steps: dry-run, inspect, write, diff, test, approve.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PLAN = ROOT / "roadmap" / "scaffold-plan.json"


def roadmap(path: Path) -> dict[str, object]:
    area = path.parent.as_posix() or "repository root"
    return {
        "file": path.as_posix(),
        "purpose": f"Define the bounded Digital Consciousness Field responsibility for {path.stem} within {area}.",
        "phase": "planned",
        "stages": ["contract", "implementation", "verification", "integration", "release"],
        "tasks": [
            "Define typed inputs, outputs, identities, capabilities, invariants, and failure behavior.",
            "Implement deterministic content-addressed behavior without implicit trust or authority expansion.",
            "Add positive, negative, boundary, revocation, replay, and tamper tests.",
            "Connect provenance, retention, topic filtering, and human-review requirements.",
            "Document compatibility, migration, rollback, privacy, and release evidence."
        ],
        "steps": [
            "Review SEEKER, QSO, and FABRIC integration contracts.",
            "Implement or document the field responsibility.",
            "Add fail-closed schemas and fixtures.",
            "Run exact-head contract and replay validation.",
            "Record human acceptance evidence."
        ],
        "status": "scaffold"
    }


def render(path: Path) -> str:
    item = roadmap(path)
    suffix = path.suffix.lower()
    body = "\n".join([
        f"Roadmap: {item['file']}",
        f"Purpose: {item['purpose']}",
        f"Phase: {item['phase']}",
        "Stages: contract -> implementation -> verification -> integration -> release",
        "Tasks:",
        *[f"- {task}" for task in item["tasks"]],
        "Steps:",
        *[f"{index}. {step}" for index, step in enumerate(item["steps"], 1)],
    ])
    if suffix == ".json":
        return json.dumps({"roadmap": item}, indent=2) + "\n"
    if suffix == ".py":
        return f'"""\n{body}\n"""\n\nfrom __future__ import annotations\n\n# TODO: replace scaffold with tested implementation.\n'
    if suffix in {".yml", ".yaml", ".toml"}:
        return "# " + body.replace("\n", "\n# ") + "\n"
    return f"# {path.stem.replace('-', ' ').title()}\n\n{body}\n"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--force", action="store_true")
    args = parser.parse_args()
    plan = json.loads(PLAN.read_text(encoding="utf-8"))
    for folder, names in plan["groups"].items():
        for name in names:
            relative = Path(folder) / name
            target = ROOT / relative
            print(("replace" if target.exists() else "create") + ": " + relative.as_posix())
            if not args.write or (target.exists() and not args.force):
                continue
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(render(relative), encoding="utf-8")


if __name__ == "__main__":
    main()
