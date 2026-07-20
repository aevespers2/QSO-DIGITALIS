# Portfolio role

## Proposed A.L.I.S.T.A.I.R.E. responsibility

QSO-DIGITALIS is being evaluated as the **evidence-exchange contract layer** of A.L.I.S.T.A.I.R.E.: the bounded interface that lets one subsystem refer to accepted evidence without collapsing retrieval, cognition, experimentation, and governance into a single trust domain.

The repository is useful only if this responsibility remains unique, narrow, and testable. If another canonical repository already owns the complete contract, QSO-DIGITALIS should be retired or converted into a compatibility index rather than duplicating authority.

## Responsibility matrix

| System | Primary responsibility | May provide to QSO-DIGITALIS | Must not delegate to QSO-DIGITALIS |
|---|---|---|---|
| `ALISTAIRE-` | Canonical system architecture, governance doctrine, portfolio roadmap | Approved policy and ownership decisions | Human final approval, portfolio governance, emergency authority |
| QSO-SEEKER | Retrieval, source adapters, source terms, canonical evidence preparation | Accepted inert record plus provenance and source-policy evidence | Retrieval credentials, raw responses, source acceptance decisions |
| QSO-DIGITALIS | Candidate evidence-envelope, capability, purpose, retention, revocation, and reference contract | — | Cognition, orchestration, repository control, deployment authority |
| QuantumStateObjects | Bounded local QSO execution and runtime evidence | Scoped evidence-reference requests and use records | Runtime memory, model authority, genome behavior |
| QSO-GENOMES | Identity and governed genome contracts | Approved identity or policy references | Genome mutation or ethics-governance authority |
| QSO-FABRIC | Experiment coordination, collaboration, and evidence bundles | Experiment scope and reference-use evidence | Experiment conclusions or promotion decisions |
| Bridge | External verification and publication boundary where approved | Verified external evidence references | Publication credentials or public-release authority |
| QSO-STUDIO / AionUi | Human-facing inspection and interaction | Read-only status and evidence views | Hidden administrative or operational authority |
| Autonomous development control plane | Planning, branch/PR preparation, verification orchestration, release workflow | Approved tasks and evidence requirements | Credentials, merges, deployments, or incident powers unless separately granted |

## Non-overlap rules

1. **SEEKER owns how evidence is acquired and accepted.** DIGITALIS may verify a publisher's conformance but must not redefine source retrieval or source licensing.
2. **QuantumStateObjects owns local execution.** DIGITALIS returns evidence references or bounded records; it does not run models, agents, tools, or memory.
3. **FABRIC owns experiment evidence.** DIGITALIS can record exchange events but does not decide experiment goals, scoring, or conclusions.
4. **Governance remains external.** A field record can carry policy evidence but cannot authorize its own promotion, merge, release, deployment, or emergency action.
5. **Bridge owns approved external publication boundaries.** DIGITALIS must not silently become a public API or publication service.
6. **Interfaces are observers by default.** A UI may inspect status but does not gain capabilities merely by rendering a record.

## Autonomous-development relationship

A.L.I.S.T.A.I.R.E.'s autonomous development loop may use QSO-DIGITALIS only as a source of immutable, policy-scoped evidence references. The development control plane remains responsible for:

- selecting authorized objectives;
- establishing branch and repository scope;
- granting temporary capabilities;
- requiring exact-head tests and review evidence;
- separating proposal, verification, merge, release, and deployment powers;
- preserving rollback and incident controls;
- obtaining human final approval for consequential changes.

QSO-DIGITALIS must never infer that a record is approved merely because it is present, frequently cited, or emitted by another QSO.

## Retirement test

Retirement is the correct outcome when any of the following is true:

- the proposed contract duplicates an accepted canonical contract elsewhere;
- ownership cannot be separated cleanly from SEEKER, runtime, FABRIC, or governance;
- the repository name creates persistent claims that the implementation cannot support;
- no downstream consumer accepts the contract by exact version and hash;
- the contract cannot be implemented without expanding into credentials, unrestricted networking, execution, or external mutation;
- privacy, source terms, retention, and revocation cannot be governed consistently.

A retirement decision should preserve provenance, link the successor contract, mark all scaffold artifacts as historical proposals, and prevent accidental release claims.
