# QSO-DIGITALIS Documentation

**Status:** `REVIEW — DOCUMENTATION-ONLY CHARTER DECISION`

QSO-DIGITALIS is being evaluated as a possible schema-first evidence-exchange boundary. The repository remains on architectural hold until its role is shown to be necessary, non-overlapping, governable, reversible, accessible, and supportable.

## Reader routes

### Portfolio and architecture reviewers

1. Read the [project overview](project-overview.md).
2. Review the [architecture and trust boundaries](architecture.md).
3. Compare repository responsibilities in the [contract boundary](contract-boundary.md).
4. Use the [charter decision packet](charter-decision-packet.md) to evaluate approval, revision, split, or retirement.
5. Review the [retirement and migration guide](retirement-migration-guide.md) before any disposition.
6. Record a charter disposition using the gates in `taskchain.md` and `release.md`.

### Contributors

1. Follow [safe onboarding](onboarding.md).
2. Read the [developer guide](developer-guide.md).
3. Keep all changes documentation-, fixture-, or validation-only until P0 is approved.
4. Bind claims to exact source, version, digest, and evidence state.
5. Use the [accessibility review](accessibility-review.md) for every new reader route, diagram, table, decision surface, or rendered publication candidate.

### Security, privacy, accessibility, and release reviewers

- Confirm all public examples are synthetic and non-sensitive.
- Confirm diagrams have equivalent prose.
- Confirm evidence and authority states are expressed in text and are not conveyed by color alone.
- Confirm keyboard, focus, 200%/400% zoom and reflow, contrast, reduced-motion, and assistive-technology review remains bound to the exact rendered candidate.
- Confirm no credential, network, repository-write, autonomous-approval, payment, or deployment capability is introduced.
- Confirm `QSO-CONSENT-CAPACITY-LOCK-v1` remains fail-closed.
- Confirm correction, withdrawal, retirement, restoration, and rollback routes remain visible.

## Decision in plain language

The portfolio needs to decide whether a separate repository is useful for describing how inert evidence references move between components. A valid charter would define only the exchange contract and its governance. It would not own the source evidence, the consumer runtime, experiment conclusions, identity decisions, or operational authority.

The decision must be explicit. A repository name, documentation quality, mergeability, inactivity, or successful checks cannot approve a role. When a unique role is not demonstrated, the safe outcome is a provenance-preserving retirement or migration rather than inferred implementation scope.

## Current evidence boundary

The documentation may establish:

- a coherent problem statement;
- explicit repository responsibilities and non-goals;
- candidate record families and lifecycle questions;
- a reviewable charter decision matrix and required decision record;
- review, migration, correction, withdrawal, restoration, and retirement gates;
- source-level accessibility requirements;
- exact-head documentation consistency.

It cannot establish:

- accepted schemas or namespaces;
- semantic compatibility with downstream repositories;
- implementation readiness;
- security, privacy, licensing, rendered accessibility, or support approval;
- a release, Pages publication, deployment, or service;
- literal consciousness or autonomous authority.

## Planning controls

- [Task chain](../taskchain.md)
- [Punch list](../punchlist.md)
- [Release plan](../release.md)
- [Changelog](../changelog.md)

The source in `docs/` is Pages-ready documentation content, but publication remains separately blocked until explicit approval and resulting-state verification.
