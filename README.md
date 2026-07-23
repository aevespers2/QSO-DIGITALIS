# QSO-DIGITALIS

QSO-DIGITALIS is a **documentation-first charter candidate** for a bounded, content-addressed evidence-exchange contract within the QSO portfolio.

The repository does not currently provide a field runtime, transport service, shared-memory system, identity authority, credential service, storage platform, autonomous decision-maker, or production deployment. Its only active work is to determine whether a distinct repository role can be justified without overlapping QSO-SEEKER retrieval, QuantumStateObjects runtime state, or QSO-FABRIC experiment evidence.

## Start here

- [Documentation front door](docs/index.md)
- [Project overview](docs/project-overview.md)
- [Architecture and trust boundaries](docs/architecture.md)
- [Contract and repository boundaries](docs/contract-boundary.md)
- [Charter decision packet](docs/charter-decision-packet.md)
- [Retirement and migration guide](docs/retirement-migration-guide.md)
- [Accessibility review](docs/accessibility-review.md)
- [Safe onboarding](docs/onboarding.md)
- [Developer documentation](docs/developer-guide.md)
- [Task chain](taskchain.md)
- [Punch list](punchlist.md)
- [Release plan](release.md)
- [Changelog](changelog.md)

## Current disposition

`REVIEW — CHARTER OR RETIREMENT DECISION REQUIRED`

A prior architecture candidate exists in PR #2, but it is stale relative to current `main`, currently non-mergeable, and includes scaffold materialization that remains outside the approved documentation scope. This branch preserves the useful charter questions while introducing no implementation or publication authority.

The [charter decision packet](docs/charter-decision-packet.md) defines the evidence and decision record required to approve, revise, split, or retire the repository. The [retirement and migration guide](docs/retirement-migration-guide.md) preserves provenance, consumer reachability, and rollback whether or not an active charter is ever approved.

## Proposed bounded role

The charter question is whether QSO-DIGITALIS should own a neutral envelope for **sanitized, inert, versioned evidence references** exchanged among portfolio components. Any accepted role must remain:

- content-addressed and hash-verifiable;
- non-executable and credential-free;
- capability-scoped and purpose-limited;
- explicit about sensitivity, retention, correction, revocation, and provenance;
- subordinate to source repositories rather than a replacement for them;
- independently testable by exact version and digest.

## Explicit non-goals

QSO-DIGITALIS does not claim literal consciousness, sentience, awareness, independent personhood, unrestricted shared memory, implicit trust, raw network capture transport, autonomous approval, repository writes, payments, settlement, credential custody, or production infrastructure.

The repository is also bound by `QSO-CONSENT-CAPACITY-LOCK-v1`; documentation or future fixtures cannot be used to bypass explicit, informed, current, revocable consent or human review.

## Evidence states

Documentation uses the following states consistently:

- `PROPOSED` — described but not accepted;
- `REVIEW` — ready for bounded architectural review;
- `BLOCKED` — missing a required decision or evidence;
- `VERIFIED` — validated only for the exact stated source and scope;
- `WITHDRAWN` — no longer current;
- `HISTORICAL` — preserved as provenance, not current authority.

Passing documentation checks establishes only source consistency. It does not approve the charter, merge PR #2, authorize scaffold writes, approve Pages publication, release a package, activate a service, or grant operational authority.

## Accessibility and review

Evidence state, authority, retirement, and rollback must be communicated in text and must not depend on color, layout, motion, or a diagram alone. Source review is required now; keyboard, focus, 200%/400% zoom and reflow, contrast, reduced-motion, and assistive-technology review remain required against any exact rendered publication candidate.

## FYSA-120 capability map

This documentation work uses the portfolio skill map as planning metadata:

- **CAT-012:** document architecture, technical exposition, link checking, docs-as-code, and lifecycle synchronization;
- **CAT-013:** repository-role modeling, contradiction detection, provenance, relationship-graph maintenance, and charter disposition analysis;
- **CAT-017:** exact-version references, source lineage, digest binding, correction propagation, and review records;
- **CAT-019:** plain-language explanation, accessible alternatives to diagrams, status comprehension, keyboard/focus review, and zoom/reflow review;
- **CAT-031:** acceptance criteria, hostile regressions, exact-head verification, and fail-closed publication review;
- **CAT-040:** repository archaeology, migration planning, compatibility boundaries, retirement, restoration, and rollback;
- **CAT-052:** least privilege, consent boundaries, audit evidence, and continuous assurance.

Proposed non-authoritative subdivisions:

- **`012-M — charter-stage repository documentation and retirement-readiness engineering`**;
- **`013-J — repository-charter decision matrices and contract-graph disposition analysis`**;
- **`019-K — evidence-state, authority-boundary, and retirement-route accessibility assurance`**;
- **`040-J — repository retirement, consumer-reachability, and restoration engineering`**.
