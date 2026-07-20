# Contributing to QSO-DIGITALIS

QSO-DIGITALIS is currently at the charter-disposition stage. Contributions must preserve that boundary and must not present proposed scaffolds, schemas, services, or integrations as implemented capability.

## Start here

Read `README.md`, `taskchain.md`, `release.md`, `changelog.md`, `punchlist.md`, and the documentation site before proposing changes. The active priority is P0: approve, revise, or retire the repository charter represented by draft PR #2.

## Before P0 approval

Appropriate work includes documentation corrections, ownership and non-overlap analysis, review questions, acceptance evidence, threat/privacy/license/retention analysis, migration and rollback requirements, and retirement guidance.

Do not add or materialize runtime, transport, storage, signing, scheduling, credential, external-integration, or deployment authority before the charter and contract gates are explicitly accepted.

## Documentation checks

```bash
python -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements-docs.txt
mkdocs build --strict
```

The repository consent-capacity lock must also pass against the submitted head. Documentation that discusses consent-sensitive content must remain explicitly bound to `QSO-CONSENT-CAPACITY-LOCK-v1` and may not weaken its fail-closed semantics.

## Pull-request template

Include:

- objective and intended user outcome;
- active task-chain item;
- current behavior and proposed change;
- authority added, removed, or explicitly unchanged;
- source, schema, policy, artifact, and workflow identities used for validation;
- security, privacy, source-license, retention, migration, and rollback impact;
- exact commands and results;
- unresolved questions and stop conditions.

For documentation-only work, state that no materialization, runtime, integration, release, or deployment is authorized.

## Claim discipline

Use **present**, **candidate**, **blocked**, and **not implemented** consistently. A file name, roadmap entry, generated placeholder, passing documentation build, or mergeable pull request is not evidence that a field capability exists.

## Review standard

A change is reviewable when it is narrowly scoped, internally consistent, aligned with the coordination files, free of secrets and restricted data, deterministic to validate, and explicit about what remains unapproved.
