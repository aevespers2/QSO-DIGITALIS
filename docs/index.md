# QSO-DIGITALIS Documentation

**Status:** `REVIEW — DOCUMENTATION-ONLY CHARTER DECISION`

QSO-DIGITALIS is being evaluated as a possible schema-first evidence-exchange boundary. The repository remains on architectural hold until its role is shown to be necessary, non-overlapping, governable, reversible, and supportable.

## Reader routes

### Portfolio and architecture reviewers

1. Read the [project overview](project-overview.md).
2. Review the [architecture and trust boundaries](architecture.md).
3. Compare repository responsibilities in the [contract boundary](contract-boundary.md).
4. Record a charter disposition using the gates in `taskchain.md` and `release.md`.

### Contributors

1. Follow [safe onboarding](onboarding.md).
2. Read the [developer guide](developer-guide.md).
3. Keep all changes documentation-, fixture-, or validation-only until P0 is approved.
4. Bind claims to exact source, version, digest, and evidence state.

### Security, privacy, accessibility, and release reviewers

- Confirm all public examples are synthetic and non-sensitive.
- Confirm diagrams have equivalent prose.
- Confirm no credential, network, repository-write, autonomous-approval, payment, or deployment capability is introduced.
- Confirm `QSO-CONSENT-CAPACITY-LOCK-v1` remains fail-closed.
- Confirm correction, withdrawal, retirement, and rollback routes remain visible.

## Decision in plain language

The portfolio needs to decide whether a separate repository is useful for describing how inert evidence references move between components. A valid charter would define only the exchange contract and its governance. It would not own the source evidence, the consumer runtime, experiment conclusions, identity decisions, or operational authority.

## Current evidence boundary

The documentation may establish:

- a coherent problem statement;
- explicit repository responsibilities and non-goals;
- candidate record families and lifecycle questions;
- review, migration, correction, withdrawal, and retirement gates;
- exact-head documentation consistency.

It cannot establish:

- accepted schemas or namespaces;
- semantic compatibility with downstream repositories;
- implementation readiness;
- security or privacy approval;
- a release, Pages publication, deployment, or service;
- literal consciousness or autonomous authority.

## Planning controls

- [Task chain](../taskchain.md)
- [Punch list](../punchlist.md)
- [Release plan](../release.md)
- [Changelog](../changelog.md)

The source in `docs/` is Pages-ready documentation content, but publication remains separately blocked until explicit approval and resulting-state verification.
