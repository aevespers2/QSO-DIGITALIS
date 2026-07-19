# Architecture diagrams

These diagrams describe the charter candidate only. They do not indicate that a field runtime, transport, datastore, or deployment exists.

## Portfolio responsibility map

```mermaid
flowchart LR
    Source[External source] -->|isolated retrieval| Seeker[QSO-SEEKER]
    Seeker -->|canonical inert evidence + hash| Publisher[Publisher adapter]
    Publisher -->|proposed envelope| Digitalis[QSO-DIGITALIS contract]
    Digitalis -->|capability-scoped read view| QSO[QuantumStateObjects]
    QSO -->|evidence use| Fabric[QSO-FABRIC]
    Fabric -->|review bundle| Human[Human reviewer]

    Digitalis -. does not own .-> Source
    Digitalis -. does not execute .-> QSO
    Digitalis -. does not approve .-> Human
```

## Proposed validation path

```mermaid
sequenceDiagram
    participant P as Authorized publisher
    participant D as Digitalis contract
    participant R as Contract registry
    participant C as Authorized consumer
    participant F as QSO-FABRIC

    P->>D: Envelope + content hash + policy metadata
    D->>R: Resolve exact schema and policy versions
    R-->>D: Accepted versions and hashes
    D->>D: Validate capability, topic, purpose, sensitivity, retention, provenance
    alt valid and in scope
        D-->>P: Immutable acceptance record
        C->>D: Scoped query
        D->>D: Re-evaluate capability and current revocation/expiry state
        D-->>C: Bounded immutable view
        C->>F: Record evidence use and decision identity
    else invalid, unknown, expired, revoked, or over-scoped
        D-->>P: Deterministic rejection record
    end
```

## Authority boundaries

```mermaid
flowchart TB
    subgraph Outside[Outside QSO-DIGITALIS authority]
        Retrieval[Network retrieval]
        Canon[Raw evidence canonicalization]
        Runtime[QSO runtime and reasoning]
        Experiment[Experiment assembly]
        Approval[Conclusion or action approval]
        Deploy[Release and deployment control]
    end

    subgraph Candidate[Proposed QSO-DIGITALIS authority]
        Registry[Versioned contract registry]
        Validate[Envelope validation]
        Capability[Capability separation]
        Policy[Purpose / sensitivity / retention filtering]
        View[Immutable scoped views]
        Provenance[Decision and provenance records]
    end

    Retrieval --> Canon --> Validate
    Registry --> Validate --> Capability --> Policy --> View
    View --> Runtime --> Experiment --> Approval
    Provenance --> Experiment
    Deploy -. independent approval .-> Candidate
```

## Record lifecycle

```mermaid
stateDiagram-v2
    [*] --> Proposed
    Proposed --> Rejected: malformed / unknown / over-scoped
    Proposed --> Accepted: validation passes
    Accepted --> Available: authorized scoped view
    Available --> Acknowledged: receipt recorded
    Accepted --> Revoked: explicit revocation
    Available --> Revoked: explicit revocation
    Accepted --> Expired: retention or lease ends
    Available --> Expired: retention or lease ends
    Acknowledged --> Expired: retention or lease ends
    Revoked --> Historical: decision evidence retained as permitted
    Expired --> Historical: decision evidence retained as permitted
    Historical --> [*]
```

## Release decision flow

```mermaid
flowchart TD
    A[Review charter candidate] --> B{Unique bounded role?}
    B -- No --> R[Retire or transfer responsibility]
    B -- Yes --> C{Security, privacy, retention, license, migration, rollback approved?}
    C -- No --> H[Keep architectural hold]
    C -- Yes --> S[Publish schema-first contract candidate]
    S --> T{Fixtures, negative tests, exact-head CI, provenance pass?}
    T -- No --> H
    T -- Yes --> L[Consider local disposable reference path]
    L --> D{Downstream consumers accept exact version and hash?}
    D -- No --> H
    D -- Yes --> E[Separate release and deployment decisions]
```
