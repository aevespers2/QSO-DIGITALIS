# Developer onboarding

## Start here

QSO-DIGITALIS is on an architectural hold. New contributors should begin by reading:

1. the root `README.md`;
2. `taskchain.md` for the active priority;
3. `release.md` for acceptance gates;
4. `changelog.md` for recorded decisions;
5. this documentation site;
6. draft PR #2 as a proposal, not an accepted implementation.

## Local documentation preview

Use an isolated Python environment:

```bash
python -m venv .venv
. .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install mkdocs
mkdocs build --strict
mkdocs serve
```

On Windows PowerShell, activate with:

```powershell
.venv\Scripts\Activate.ps1
```

A successful build verifies navigation and Markdown rendering only. It does not approve the charter or establish runtime evidence.

## Contribution workflow

1. Confirm the proposed change is documentation, decision, or evidence planning within the current P0 scope.
2. Create a focused branch from current `main`.
3. Preserve the architectural-hold language and explicit non-claims.
4. Cross-check changes against `taskchain.md`, `release.md`, and `changelog.md`.
5. Run `mkdocs build --strict`.
6. Check internal links, Mermaid syntax, headings, tables, and terminology.
7. Open a draft pull request with exact scope, exclusions, validation commands, and unresolved decisions.
8. Keep charter approval, merge approval, release approval, and deployment approval separate.

## Documentation standards

- State whether content is current, proposed, blocked, or future.
- Prefer testable contracts and invariants over aspirational language.
- Name repository ownership and non-ownership explicitly.
- Link claims to immutable PR, commit, workflow, report, or artifact evidence.
- Avoid capability claims based solely on file presence.
- Record dates and exact identifiers for decisions and validation.
- Document migration and rollback whenever a contract could change hashes or interpretation.
- Keep examples synthetic, inert, non-sensitive, and bounded.

## Reviewing architecture changes

Reviewers should verify:

- non-overlap with QSO-SEEKER, QuantumStateObjects, QSO-FABRIC, and portfolio governance;
- separation of conformance from conclusion approval;
- explicit capability, purpose, sensitivity, retention, expiry, and revocation semantics;
- deterministic canonicalization and version/hash behavior;
- fail-closed handling for malformed, unknown, expired, revoked, and over-scoped inputs;
- no hidden network, credential, execution, repository-write, payment, or deployment authority;
- realistic verification, migration, recovery, and retirement paths.

## Proposed implementation sequence after approval

No implementation work is authorized today. If P0 is approved, the expected order is:

1. schemas and policy contracts;
2. canonicalization profile and deterministic fixtures;
3. validators and negative/adversarial tests;
4. exact-head CI and retained evidence;
5. local disposable reference path;
6. downstream compatibility fixtures;
7. security, privacy, license, provenance, recovery, and rollback review;
8. separate release decision;
9. separate deployment decision.

## Pull-request checklist

- [ ] Scope is documentation or charter-approved work.
- [ ] No implementation authority is inferred.
- [ ] `taskchain.md`, `release.md`, and `changelog.md` remain aligned.
- [ ] Documentation builds strictly.
- [ ] Links and diagrams are checked.
- [ ] Security, privacy, retention, and authority boundaries are preserved.
- [ ] Exact head and validation evidence are recorded.
- [ ] Remaining decisions and blockers are explicit.
