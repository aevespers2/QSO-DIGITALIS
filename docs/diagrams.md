# Diagrams

These diagrams describe the charter candidate and its required controls. They do not claim an implemented service.

## Portfolio context

```mermaid
flowchart TB
    GOV[A.L.I.S.T.A.I.R.E. governance\npolicy, authorization, review]
    SEEK[QSO-SEEKER\naccepted inert evidence]
    DIG[QSO-DIGITALIS\ncandidate exchange contract]
    QSO[QuantumStateObjects\nbounded local use]
    FAB[QSO-FABRIC\nexperiment evidence]
    UI[QSO-STUDIO / AionUi\nread-only inspection]
    BR[Bridge\napproved external boundary]

    GOV -. approved policy .-> SEEK
    GOV -. approved policy .-> DIG
    GOV -. approved policy .-> QSO
    GOV -. approved policy .-> FAB
    SEEK -->|canonical record + provenance| DIG
    DIG -->|hash-fixed scoped view| QSO
    QSO -->|outputs + reference-use evidence| FAB
    DIG -->|status evidence| UI
    FAB -->|review evidence| UI
    FAB -. separately approved publication .-> BR
```

## Candidate publish-and-read sequence

```mermaid
sequenceDiagram
    participant P as Conforming publisher
    participant D as Exchange boundary
    participant S as Content-addressed store
    participant C as Scoped consumer
    participant E as Experiment evidence

    P->>D: Envelope candidate + canonical record reference
    D->>D: Validate version, identity, digest, capability, purpose, sensitivity, time
    alt invalid or unauthorized
        D-->>P: Reject with bounded evidence
    else valid
        D->>S: Verify or store immutable content by digest
        S-->>D: Exact digest and provenance status
        D-->>P: Accepted envelope reference
        C->>D: Scoped query or exact reference request
        D->>D: Evaluate consumer capability and policy intersection
        alt denied, expired, revoked, or mismatched
            D-->>C: Fail-closed response
        else allowed
            D-->>C: Immutable reference or bounded record
            C->>E: Record exact contract, policy, and evidence digests used
        end
    end
```

## Capability separation

```mermaid
flowchart LR
    ID[Verified subject] --> PUBLISH[publish]
    ID --> DISCOVER[discover]
    ID --> SUBSCRIBE[subscribe]
    ID --> READ[read]
    ID --> ACK[acknowledge]
    ID --> REVOKE[revoke]
    ID --> ADMIN[administer-policy]

    PUBLISH -. does not imply .- READ
    DISCOVER -. does not imply .- READ
    READ -. does not imply .- REVOKE
    ACK -. does not imply .- PUBLISH
    REVOKE -. does not imply .- ADMIN
```

## Trust boundaries

```mermaid
flowchart LR
    U[Untrusted external source] -->|outside repository| S[QSO-SEEKER boundary]
    S -->|accepted record candidate| P[Publisher conformance boundary]
    P -->|validated envelope| D[QSO-DIGITALIS policy boundary]
    D -->|least-privilege view| Q[Consumer boundary]
    Q -->|untrusted output + exact references| F[QSO-FABRIC evaluation boundary]
    F -->|evidence only| H[Human review and governance]

    classDef boundary stroke-width:3px;
    class S,P,D,Q,F,H boundary;
```

## Record lifecycle

```mermaid
stateDiagram-v2
    [*] --> Candidate
    Candidate --> Rejected: invalid / unauthorized
    Candidate --> Active: validated and accepted
    Active --> Expired: time or retention rule
    Active --> Revoked: authorized revocation
    Active --> Superseded: compatible replacement or migration
    Expired --> Tombstone
    Revoked --> Tombstone
    Superseded --> Tombstone
    Rejected --> EvidenceOnly
    Tombstone --> EvidenceOnly
    EvidenceOnly --> [*]
```

## Release gates

```mermaid
flowchart LR
    P0[P0 charter disposition] --> P1[P1 schemas, policies, fixtures]
    P1 --> P2[P2 bounded local reference path]
    P2 --> P3[P3 downstream compatibility]
    P3 --> RC[Release candidate evidence]
    RC --> RA[Separate release approval]
    RA --> DA[Separate deployment approval]

    P0 -. retirement .-> AR[Archive and successor links]
```

## Incident and rollback

```mermaid
flowchart TB
    D[Detect mismatch, leakage, nondeterminism, or authority expansion] --> H[Halt candidate path]
    H --> C[Revoke pending capabilities and preserve evidence]
    C --> I[Identify source, contract, policy, and artifact digests]
    I --> R[Restore previous accepted contract state]
    R --> V[Re-run deterministic, revocation, replay, tamper, and isolation tests]
    V --> Q{All evidence passes?}
    Q -->|No| H
    Q -->|Yes| A[Require fresh review and approval]
```
