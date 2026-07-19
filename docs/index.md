# QSO-DIGITALIS

QSO-DIGITALIS is currently a **charter decision repository**, not an implemented service. Its active work is to decide whether the repository should own a bounded, content-addressed evidence-exchange contract for the QSO portfolio or be retired.

The leading proposal is the **Digital Consciousness Field (DCF)** described in draft PR #2. In this documentation, that name is architectural shorthand only. It does not claim awareness, sentience, identity, agency, or independent authority.

## Current status

| Area | Status |
|---|---|
| Product charter | Under review |
| Accepted schemas | None |
| Reference implementation | None |
| Network or storage service | Not authorized |
| Deployment | Not authorized |
| Release | Blocked |

## Proposed responsibility

If approved, QSO-DIGITALIS would define a narrow contract for exchanging immutable, non-executable, policy-bound evidence references among authorized portfolio components. It would not perform retrieval, run Quantum State Objects, assemble experiments, approve conclusions, mutate repositories, or provide production infrastructure.

## Repository relationships

- **QSO-SEEKER** retrieves, sanitizes, canonicalizes, and records source evidence.
- **QuantumStateObjects** may consume read-only, capability-scoped views.
- **QSO-FABRIC** assembles experiment evidence and records use.
- **QSO-DIGITALIS**, if chartered, would own only the exchange envelope, capability, topic, retention, revocation, and provenance-link contracts between those systems.

## Documentation map

- [Project overview](project-overview.md)
- [Architecture outline](architecture.md)
- [Architecture diagrams](diagrams.md)
- [Design contracts](design-contracts.md)
- [Charter decision](charter-decision.md)
- [Security and privacy](security-privacy.md)
- [Known limitations](limitations.md)
- [Developer onboarding](onboarding.md)
- [Operations and recovery](operations.md)

## Scope rule

Documentation may clarify the proposed contract and its boundaries. It must not be interpreted as implementation evidence, approval of draft PR #2, permission to run scaffold materialization, or authorization for runtime, release, publication, or deployment.
