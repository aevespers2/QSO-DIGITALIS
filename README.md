# QSO-DIGITALIS

QSO-DIGITALIS is a **charter-stage evidence-exchange contract candidate** for the A.L.I.S.T.A.I.R.E. Quantum State Object portfolio. Its proposed role is to define how accepted, non-executable evidence can be published, discovered, filtered, referenced, revoked, retained, and audited across repository boundaries without transferring execution or governance authority.

> **Status:** P0 review. The repository has no approved field contract, runtime, transport service, persistent multi-user store, signing service, deployment target, or autonomous authority. Draft PR #2 is an architecture/scaffold candidate; draft PR #5 is a documentation baseline. Neither pull request authorizes materialization or implementation.

## Proposed portfolio boundary

| Repository or system | Responsibility |
|---|---|
| `ALISTAIRE-` | Canonical architecture, governance doctrine, roadmap, and final approval boundaries |
| QSO-SEEKER | Retrieval, source controls, canonical evidence preparation, and provenance |
| **QSO-DIGITALIS** | Candidate envelope, capability, purpose, retention, revocation, and evidence-reference contract |
| QuantumStateObjects | Bounded local QSO execution and runtime evidence |
| QSO-FABRIC | Experiment coordination and evidence bundles |
| Bridge | Separately approved external verification or publication boundary |
| Autonomous development control plane | Task authorization, branch/PR preparation, verification, release workflow, rollback, and incident controls |

QSO-DIGITALIS must not own retrieval credentials, QSO cognition, experiment conclusions, repository writes, payments, merges, releases, deployments, or emergency governance.

## What exists

- product and release coordination in [`taskchain.md`](taskchain.md), [`release.md`](release.md), [`changelog.md`](changelog.md), and [`punchlist.md`](punchlist.md);
- immutable consent-capacity policy `QSO-CONSENT-CAPACITY-LOCK-v1` and its pull-request check;
- draft PR #2 proposing a bounded Digital Consciousness Field architecture, roadmap manifest, and scaffold materializer;
- draft PR #5 proposing a GitHub Pages-ready documentation site and exact-head documentation evidence workflow.

## What does not exist

- accepted field schemas, policies, fixtures, validators, or migrations;
- a tested reference implementation;
- network transport, credentials, signing, external storage, or multi-user service;
- downstream compatibility evidence from QSO-SEEKER, QuantumStateObjects, or QSO-FABRIC;
- release or deployment approval;
- evidence supporting literal consciousness, awareness, sentience, or independent authority claims.

## Design principles

1. **Schema and fixtures before runtime.**
2. **Evidence references remain inert and content-addressed.**
3. **Capabilities are explicit, separate, least-privilege, purpose-bound, and revocable.**
4. **Unknown versions, mismatched hashes, expired records, and invalid policy states fail closed.**
5. **Current and proposed capabilities are documented separately.**
6. **Consequential conclusions and actions require separate human review and authorization.**
7. **Retirement is preferred to duplicated or ambiguous portfolio ownership.**

## Documentation

The Pages-ready site covers:

- [project overview](docs/index.md);
- [A.L.I.S.T.A.I.R.E. portfolio role](docs/portfolio-role.md);
- [architecture](docs/architecture.md);
- [candidate contract design](docs/contracts.md);
- [Mermaid diagrams](docs/diagrams.md);
- [security and privacy](docs/security.md);
- [developer onboarding](docs/onboarding.md);
- [operations and recovery](docs/operations.md);
- [decisions and open questions](docs/decisions.md);
- [release evidence](docs/release-evidence.md).

Build locally:

```bash
python -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements-docs.txt
mkdocs build --strict
mkdocs serve
```

See [`CONTRIBUTING.md`](CONTRIBUTING.md) before proposing changes.

## Current architectural decision

P0 must explicitly approve, revise, or reject a unique QSO-DIGITALIS charter. The decision must settle contract ownership, identity and capability issuance, data/privacy/source-license/retention boundaries, downstream acceptance, migration and rollback, autonomous-development control-plane boundaries, release authority, emergency stop, and retirement criteria.
