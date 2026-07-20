# Operations and recovery

No QSO-DIGITALIS runtime or deployment is approved. This page defines the operational evidence that a future bounded candidate would need; it is not a runbook for a production service.

## Current operations

The only supported operational activity is repository review and documentation validation:

```bash
python -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements-docs.txt
mkdocs build --strict
```

Pull requests must also pass the repository consent-capacity lock. A successful documentation build does not advance P0, accept a schema, validate downstream compatibility, or authorize release.

## Future local verification profile

After P0 and P1 acceptance, the first permissible reference path must be:

- local and disposable;
- in-memory or confined to a temporary filesystem root;
- synthetic-data-only;
- credential-free and network-disabled;
- bounded by record count, byte count, nesting depth, query result count, subscriptions, and wall-clock time;
- deterministic under a recorded clock and random seed where applicable;
- incapable of external repository, release, deployment, payment, or physical-world writes;
- automatically cleaned after evidence capture.

## Startup verification

A candidate run should refuse to start unless it can record and verify:

1. exact source commit and clean working-tree status;
2. contract, schema, policy, fixture, and canonicalization digests;
3. validator and adapter source identity;
4. runtime and dependency versions;
5. temporary root path and confinement checks;
6. network-disabled and credential-absent state;
7. configured resource and time limits;
8. synthetic fixture set identity;
9. prior accepted state used for rollback;
10. human approval record for the bounded verification run.

## Health model

Health is not merely process availability. A candidate is healthy only while all of the following remain true:

- source and configuration identity match the approved run record;
- canonicalization and hashing are deterministic;
- schema and policy validation are strict;
- capability, purpose, sensitivity, retention, revocation, and isolation decisions are correct;
- provenance chains remain complete;
- expired and revoked records are unavailable while tombstones remain auditable;
- limits are enforced before resource exhaustion;
- no secret, network, execution, or external-write authority appears;
- evidence logs remain bounded and free of prohibited data.

## Observability

Record only the minimum non-secret evidence needed to reproduce decisions:

- run identifier and exact source commit;
- contract, schema, policy, fixture, and artifact digests;
- bounded timestamps or logical-clock values;
- decision code and relevant non-secret identifiers;
- accepted, rejected, expired, revoked, replayed, and tombstoned counts;
- limit events and cleanup status;
- final ledger or evidence-manifest digest.

Do not log raw restricted records, credentials, private keys, session material, unrestricted paths, or unnecessary personal information.

## Incident triggers

Immediately halt a candidate path when any of these occurs:

- source, schema, policy, fixture, or artifact identity mismatch;
- nondeterministic digest or validation result;
- accepted malformed, oversized, expired, or revoked record;
- purpose, sensitivity, retention, or cross-QSO isolation failure;
- provenance break, substitution, or unauthorized replay;
- secret or restricted-data exposure;
- path escape, link traversal, or cleanup failure;
- unexpected network, credential, execution, external-write, or administrative capability;
- inability to produce complete decision evidence;
- conflict with the consent-capacity lock.

## Incident response

1. Stop the candidate process and revoke pending capabilities.
2. Preserve immutable source, configuration, logs, fixtures, and artifact digests.
3. Confirm no external mutation occurred.
4. Classify affected records, consumers, and evidence bundles.
5. Restore the previous accepted contract and validator state.
6. Re-run deterministic positive and negative suites, including expiry, revocation, replay, tamper, isolation, limits, and cleanup.
7. Record the root cause and corrective change in the task chain and changelog.
8. Require fresh review; do not automatically resume.

## Rollback standard

Rollback is successful only when:

- the previous accepted source and contract identities are restored;
- all pending capabilities are invalidated;
- affected records are unavailable or correctly tombstoned;
- downstream consumers reject the failed version and accept only the restored version/hash;
- deterministic tests pass against the restored state;
- no residual files, listeners, credentials, or external changes remain;
- evidence is archived with a final digest and reviewer disposition.

## Post-validation

At the end of every future bounded run:

1. repeat a subset of deterministic fixtures;
2. verify revocation, expiry, replay, and tombstone behavior;
3. verify final evidence-manifest and artifact hashes;
4. confirm network and credential absence;
5. remove the temporary root;
6. confirm no external writes occurred;
7. archive logs and evidence under the approved retention policy;
8. return the environment to a known clean state.
