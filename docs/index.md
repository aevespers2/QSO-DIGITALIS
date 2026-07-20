# QSO-DIGITALIS

QSO-DIGITALIS is a **charter-stage contract candidate** for bounded, content-addressed evidence exchange within the A.L.I.S.T.A.I.R.E. Quantum State Object portfolio. It is intended to define how accepted, non-executable evidence may be published, discovered, filtered, referenced, revoked, retained, and audited across repository boundaries.

!!! warning "Current status"
    The repository does not contain an approved field contract, production runtime, transport service, persistent multi-user store, signing service, deployment target, or autonomous authority. Draft PR #2 is an architecture/scaffold candidate under review. Its roadmap and materializer are proposal artifacts, not proof of implementation.

## Why this repository exists

The portfolio needs a stable boundary between systems that retrieve evidence, systems that execute local cognition, and systems that coordinate experiments. QSO-DIGITALIS is being evaluated as the owner of that boundary:

- QSO-SEEKER would prepare accepted inert evidence records.
- QSO-DIGITALIS would define the exchange envelope and policy contract.
- QuantumStateObjects would consume hash-fixed, capability-scoped views.
- QSO-FABRIC would record use of those references in experiment evidence.
- A.L.I.S.T.A.I.R.E. governance would retain prioritization, authorization, release, and incident authority elsewhere.

## Present repository surface

| Area | Present evidence | Status |
|---|---|---|
| Product direction | `taskchain.md`, `release.md`, `punchlist.md`, `changelog.md` | Active planning evidence |
| Consent control | `.consent/consent-capacity-lock-v1.json` and CI lock | Accepted repository control |
| Field architecture | Draft PR #2 | Review candidate only |
| Schemas and fixtures | Roadmap names only | Not implemented |
| Runtime and storage | None accepted | Not implemented |
| Integration evidence | None | Not validated |
| Deployment | None authorized | Blocked |

## Design principles

1. **Schema before runtime.** Contracts, fixtures, negative cases, and migrations must precede implementation.
2. **Evidence, not execution.** Field records must remain inert and must never grant code, credential, repository, payment, or deployment authority.
3. **Capability separation.** Publish, discover, subscribe, read, acknowledge, revoke, and administer are distinct permissions.
4. **Purpose limitation.** Every view is constrained by approved purpose, sensitivity, retention, source class, and experiment scope.
5. **Content-addressed provenance.** Consumers bind to explicit versions and hashes rather than mutable names alone.
6. **Fail closed.** Unknown schema versions, invalid hashes, expired records, revoked access, or missing policy evidence produce rejection.
7. **Human final review.** Consequential promotion, action, merge, release, and deployment remain separately authorized.

## Documentation map

- [Portfolio role](portfolio-role.md) — ownership and non-overlap across A.L.I.S.T.A.I.R.E.
- [Architecture](architecture.md) — current boundary and candidate lifecycle
- [Contract design](contracts.md) — proposed records, capabilities, and invariants
- [Diagrams](diagrams.md) — context, lifecycle, trust, and recovery views
- [Security and privacy](security.md) — protected assets, threats, and controls
- [Developer onboarding](onboarding.md) — safe documentation and future contract workflow
- [Operations and recovery](operations.md) — verification, rollback, and incident expectations
- [Decisions](decisions.md) — P0 disposition and unresolved ownership questions
- [Release evidence](release-evidence.md) — gate-by-gate evidence requirements

## Source-of-truth files

Repository work must remain aligned with [`taskchain.md`](../taskchain.md), [`release.md`](../release.md), [`changelog.md`](../changelog.md), and [`punchlist.md`](../punchlist.md). Where documentation and implementation claims conflict, the most conservative evidence-backed interpretation governs.
