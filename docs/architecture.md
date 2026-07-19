# Architecture outline

## Architectural posture

QSO-DIGITALIS is documentation-first and schema-first. No runtime architecture is accepted today. The model below describes the bounded charter candidate under review and must remain distinguishable from implementation evidence.

## Responsibility boundary

The proposed system sits between evidence production and evidence consumption:

1. QSO-SEEKER produces an inert canonical evidence record and its immutable identifier.
2. A publisher forms a versioned field envelope containing only accepted references and policy metadata.
3. QSO-DIGITALIS validates the envelope contract, capability, topic, purpose, sensitivity, retention, and provenance requirements.
4. An authorized consumer requests a bounded view.
5. The contract returns immutable references or bounded records and a deterministic decision record.
6. QSO-FABRIC records the access and resulting use in experiment evidence.
7. Human review remains required before a conclusion or action is promoted.

## Logical components

### Contract registry

Defines accepted versions and hashes for envelopes, topics, capabilities, queries, responses, acknowledgments, revocations, provenance links, evidence references, and policies.

### Envelope validator

Rejects malformed, unknown, mutable, executable, over-scoped, expired, revoked, or hash-inconsistent records. Validation must be deterministic and fail closed.

### Capability evaluator

Separates publish, discover, subscribe, read, acknowledge, and revoke permissions. A role never gains another capability by implication.

### Policy filter

Applies purpose, source class, sensitivity, retention, experiment scope, and human-review requirements before a view is returned.

### Content-addressed record view

Resolves only immutable identifiers accepted by the contract. The proposed field does not become the canonical source repository and must not silently rewrite evidence.

### Provenance and decision ledger

Records schema identity, policy identity, request scope, decision outcome, revocation state, and relevant hashes without storing secrets or raw source responses.

## Trust boundaries

### Outside the proposed boundary

- source retrieval and network adapters;
- canonicalization of raw evidence;
- QSO local reasoning or execution;
- experiment construction and conclusion approval;
- repository mutation, release publication, and deployment control.

### Inside the proposed boundary

- contract validation;
- capability separation;
- scope and policy filtering;
- immutable reference exchange;
- acknowledgment and revocation semantics;
- deterministic provenance and replay decisions.

## Data lifecycle

1. **Create:** an upstream producer creates a canonical, inert record.
2. **Reference:** a publisher binds the record hash to an accepted envelope version.
3. **Validate:** the field contract validates identity, capability, policy, retention, and provenance.
4. **Expose:** an authorized consumer receives a bounded read view.
5. **Acknowledge:** the consumer may record receipt without changing the source record.
6. **Revoke or expire:** future access is denied according to explicit policy while historical decision evidence is retained as permitted.
7. **Replay:** the same accepted inputs and policy versions produce the same decision.
8. **Retire:** superseded contract versions remain traceable through migrations and immutable release evidence.

## Invariants

- Records are non-executable and content-addressed.
- Every decision binds to exact schema and policy versions.
- Unknown versions, capabilities, hashes, or policy states fail closed.
- Access is least-privilege, purpose-limited, and time-bounded.
- Revocation and expiry are explicit, testable states.
- Acknowledgment never grants approval authority.
- No consumer may mutate upstream canonical evidence.
- Documentation and scaffold generation do not prove implementation.

## Deployment posture

No deployment target is authorized. A future first reference path, if approved, must be disposable, local, credential-free, network-disabled, synthetic-data-only, bounded in records and time, and independently reproducible.
