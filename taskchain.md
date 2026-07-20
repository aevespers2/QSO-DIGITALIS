# Task Chain

## Repository status

QSO-DIGITALIS remains at the charter-disposition stage. Draft PR #2 proposes a bounded Digital Consciousness Field architecture and scaffold; draft PR #5 proposes the GitHub Pages, architecture, design, onboarding, security, operations, and release-evidence baseline. Neither candidate establishes an approved contract, tested field implementation, downstream integration, release, or deployment surface.

States: `PROPOSED` · `READY` · `IN PROGRESS` · `BLOCKED` · `REVIEW` · `DONE`

## Product directive

- **Next objective:** Review draft PR #2 and draft PR #5 together, then approve a unique bounded QSO-DIGITALIS charter, request bounded correction, or retire/archive the repository.
- **User outcome:** Portfolio contributors can determine whether QSO-DIGITALIS owns a necessary capability-scoped, content-addressed evidence-exchange contract; how it differs from QSO-SEEKER retrieval/canonicalization, QuantumStateObjects local runtime, QSO-FABRIC experiment evidence, Bridge publication boundaries, and the A.L.I.S.T.A.I.R.E. autonomous-development control plane; and what authority it explicitly lacks.
- **MVP scope:** documentation-only disposition covering purpose, users, field-envelope inputs/outputs, identity and capability ownership, non-goals, trust/data/privacy/source-license/retention/consent boundaries, repository relationships, verification, migration, rollback, incident response, and retirement criteria.
- **Priority:** Charter disposition is the only product priority. Documentation validation may proceed, but no scaffold materialization, schema acceptance, field runtime, transport, storage, signing, schedule, external integration, release, or deployment is authorized before P0 approval.
- **Success criteria:** an approved charter establishes a non-overlapping stable contract and explicit evidence-only authority boundary, or the repository is retired; downstream repositories later accept the contract by exact version and hash; no implementation task is opened solely because roadmap files or rendered documentation exist.
- **Non-goals:** literal-consciousness claims, raw network/credential/archive/package/binary/Git-object transport, unrestricted shared memory, implicit QSO trust, autonomous approval, repository writes, payments, settlement, production infrastructure, or physical-world authority.

## Active chain

| Priority | Task | Owner | Depends on | Status | Acceptance criteria |
|---|---|---|---|---|---|
| P0-D | Validate the documentation baseline | Documentation / Architect | — | REVIEW | Draft PR #5 builds strictly against its exact submitted head, passes the consent-capacity lock, retains rendered-site evidence, accurately separates current and proposed capability, and aligns all coordination files. |
| P0 | Approve, revise, or retire the QSO-DIGITALIS charter | Architect / User | P0-D evidence available | REVIEW | Draft PR #2 and PR #5 receive explicit disposition; purpose, users, ownership, envelopes, capabilities, trust/data/privacy/source-license/retention/consent boundaries, non-overlap, verification, migration, rollback, incident response, and retirement criteria are approved. |
| P1 | Publish the minimum schema-first contract candidate | QSOBuilder | P0 approved as active | BLOCKED | Only charter-approved schemas, policies, canonicalization, fixtures, negative cases, migrations, validators, tests, and exact-head CI are added; roadmap placeholders do not count as implementation. |
| P2 | Implement one bounded local in-memory/filesystem reference path | Builder | P1 accepted | PROPOSED | Deterministic content addressing, path confinement, capability scope, purpose/sensitivity filtering, retention, revocation, replay, tamper detection, limits, cleanup, and provenance pass without credentials, network, or implicit trust. |
| P3 | Validate cross-repository consumers | Architect / Builders | P2 accepted | PROPOSED | QSO-SEEKER publishes only accepted inert records; QuantumStateObjects consumes read-only hash-fixed views; QSO-FABRIC records reference use in append-only experiment evidence; all fail closed on version/hash/policy mismatch. |
| P4 | Select a release candidate | Release owner | P1-P3 accepted | BLOCKED | Complete source, contract, test, security, privacy, source-license, provenance, compatibility, migration, rollback, and approval evidence is linked to one immutable head. |
| P5 | Select a deployment target | Deployment owner | P4 approved | BLOCKED | A separate target, operator, credentials owner, monitoring, incident, emergency-stop, rollback, support, and human approval record exists. |
| P6 | Archive the repository | Architect | P0 retirement decision | BLOCKED | README, description, release state, PR dispositions, successor contract, migration links, and historical scaffold status clearly record retirement. |

## Candidate set

### Draft PR #2 — field charter/scaffold

**Status:** `REVIEW — ARCHITECTURE/SCAFFOLD ONLY`

PR #2 proposes the DCF architecture, roadmap manifest, and deterministic scaffold materializer. It excludes arbitrary code execution, raw credentials/packages/binaries/Git objects, unrestricted shared memory, implicit trust, and literal-consciousness claims. It does not include accepted schemas, fixtures, tests, CI evidence, security/privacy/source-license review, downstream compatibility, provenance, rollback evidence, or deployment approval.

### Draft PR #5 — documentation baseline

**Status:** `REVIEW — DOCUMENTATION ONLY`

PR #5 proposes the Pages-ready project overview, portfolio responsibility map, architecture and contract guidance, diagrams, security/privacy controls, onboarding, operations/recovery guidance, decision register, release-evidence map, contribution guide, pinned documentation toolchain, and exact-head documentation workflow. A passing documentation build cannot approve PR #2 or advance P1-P5.

## Architectural hold

Do not run the PR #2 materializer with `--write`, create runtime/storage/transport/signing authority, publish field envelopes, change downstream contracts, or configure release/deployment behavior until P0 is explicitly approved. Any future implementation must remain content-addressed, capability-scoped, purpose-limited, retention/revocation aware, consent-capacity compliant, human-reviewed, non-executing, independently testable by version/hash, and recoverable to a previously accepted state.

## Builder log requirements

Record approvals, decisions, PR and exact-head identities, validation commands/results, schema/policy/fixture/artifact hashes, threat/privacy/source-license/retention/consent review, migrations, rollback evidence, downstream consumer results, retirement links, and follow-ups.

## Builder log

- 2026-07-17 — Classified draft PR #2 as the first concrete charter candidate. P0 moved from `BLOCKED` to `REVIEW`; no implementation, materialization, release, or deployment was authorized.
- 2026-07-20 — Opened draft PR #5 as a documentation-only Pages and architecture baseline. Added P0-D validation without changing P0 or authorizing contract, runtime, integration, release, or deployment scope.
