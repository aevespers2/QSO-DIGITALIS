# QSO-DIGITALIS

QSO-DIGITALIS is a **charter-stage interpretation, policy-projection, and evidence-exchange contract candidate** for the A.L.I.S.T.A.I.R.E. Quantum State Object portfolio. Its lowest-coupling proposed role is to preserve immutable source identity while attaching separately identified temporal and domain assessments, producing purpose-limited non-executable views, and packaging typed references for downstream validation without transferring execution, transport, canonical-state, or governance authority.

> **Status:** P0 review. The repository has no approved field contract, runtime, transport service, persistent multi-user store, signing service, deployment target, or autonomous authority. Draft PR #2 is an architecture/scaffold candidate; draft PR #5 is a documentation and contract-analysis baseline. Neither pull request authorizes materialization or implementation.

## Proposed portfolio boundary

| Repository or system | Responsibility |
|---|---|
| `ALISTAIRE-` | Canonical architecture, governance doctrine, roadmap, and final approval boundaries |
| QSO-SEEKER | Retrieval, hostile-input controls, sanitization, attribution, and inert source-observation records |
| Temporal authority | Clock identity, ordering, freshness, uncertainty, expiry interpretation, and replay assessment |
| **QSO-DIGITALIS** | Candidate interpretation references, policy-limited projections, lineage declarations, and profile-specific inert exchange envelopes |
| Bridge | Separately approved admission, transport transformation, delivery, and receipt semantics |
| Repository `1` | Candidate quarantine, capability, canonical disposition, correction, revocation, checkpoint, and recovery authority |
| QuantumStateObjects | Bounded local QSO execution and runtime evidence |
| QSO-FABRIC | Experiment coordination and evidence bundles |
| QSO-STUDIO / AionUi | Human-facing inspection and presentation without implicit authority |
| Autonomous development control plane | Task authorization, branch/PR preparation, verification, release workflow, rollback, and incident controls |

QSO-DIGITALIS must not own source retrieval credentials, temporal truth, generic transport, Repository `1` canonical state, QSO cognition, experiment conclusions, repository writes, payments, merges, releases, deployments, or emergency governance.

## What exists

- product and release coordination in [`taskchain.md`](taskchain.md), [`release.md`](release.md), [`changelog.md`](changelog.md), and [`punchlist.md`](punchlist.md);
- immutable consent-capacity policy `QSO-CONSENT-CAPACITY-LOCK-v1` and its pull-request check;
- draft PR #2 proposing a bounded Digital Consciousness Field architecture, roadmap manifest, and scaffold materializer;
- draft PR #5 proposing a GitHub Pages-ready documentation site, source-observation interpretation profile, obstruction/gluing ledger, and exact-head documentation evidence workflow.

## What does not exist

- accepted field schemas, policies, fixtures, validators, migrations, canonicalization rules, or shared vocabularies;
- a tested reference implementation;
- network transport, credentials, signing, external storage, or multi-user service;
- downstream compatibility evidence from QSO-SEEKER, temporal-invariants, Bridge, Repository `1`, QuantumStateObjects, QSO-FABRIC, QSO-STUDIO, or AionUi;
- release or deployment approval;
- evidence supporting literal consciousness, awareness, sentience, personhood, truth authority, or independent operational authority claims.

## Design principles

1. **Schema and fixtures before runtime.**
2. **Source evidence is immutable.** Interpretations and projections reference source records; they do not overwrite them.
3. **Every stage has a distinct identity.** Source, temporal, interpretation, projection, envelope, transport, receipt, disposition, and consumption records do not alias each other.
4. **Evidence references remain inert and content-addressed.**
5. **Capabilities are explicit, separate, least-privilege, purpose-bound, and revocable.**
6. **Transformations are declared.** Repackaging, normalization, redaction, aggregation, and derivation are independently visible and reproducible.
7. **Unknown versions, mismatched hashes, stale assessments, expired records, revoked access, and invalid policy states fail closed.**
8. **The most restrictive privacy, source-license, consent, retention, and disclosure rule survives downstream derivation.**
9. **Transport, storage, runtime, and interface success do not equal truth, authority, or canonical acceptance.**
10. **Retirement is preferred to duplicated or ambiguous portfolio ownership.**

## Documentation

The Pages-ready site covers:

- [project overview](docs/index.md);
- [A.L.I.S.T.A.I.R.E. portfolio role](docs/portfolio-role.md);
- [architecture](docs/architecture.md);
- [candidate contract design](docs/contracts.md);
- [source-observation interpretation profile](docs/source-observation-interpretation-profile.md);
- [obstruction and gluing analysis](docs/obstruction-and-gluing.md);
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

P0 must explicitly approve, revise, split, rename, or reject the QSO-DIGITALIS charter. The decision must settle generic envelope/profile ownership, source and subject namespaces, temporal authority, interpretation/projection ownership, canonicalization and digest scopes, data/privacy/source-license/retention boundaries, correction/revocation and cache invalidation, the exact Seeker → temporal/Digitalis → Bridge → Repository `1` route, downstream acceptance, migration and rollback, release authority, emergency stop, recovery, and retirement criteria.
