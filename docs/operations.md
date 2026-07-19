# Operations, recovery, and rollback

## Current operating mode

There is no authorized QSO-DIGITALIS service. Current operations are limited to repository review, documentation validation, decision evidence, and draft pull-request maintenance.

## Documentation operations

### Build

```bash
mkdocs build --strict
```

### Review

- inspect every navigation entry;
- verify internal and repository links;
- render Mermaid diagrams in a supported preview;
- confirm proposal, limitation, and authority language is consistent;
- compare `README.md`, `taskchain.md`, `release.md`, and `changelog.md`;
- record the exact commit used for validation.

### Publication hold

A successful site build does not authorize GitHub Pages publication. Publication requires explicit review of claims, privacy, licensing, navigation, accessibility, and provenance.

## Future reference-path operating envelope

If the charter and contract are approved, the first reference path must be:

- local and disposable;
- in-memory or isolated filesystem only;
- credential-free and network-disabled;
- synthetic-data-only;
- bounded by record count, total bytes, depth, query count, and elapsed time;
- explicit about exact source, configuration, schema, and policy hashes;
- unable to mutate upstream repositories or external systems.

## Health criteria

A future reference path is healthy only when:

- startup identity matches accepted source and configuration hashes;
- canonicalization and content hashes are deterministic;
- unknown schema and policy versions fail closed;
- capability, purpose, sensitivity, retention, expiry, and revocation checks behave as specified;
- replay, duplicate, tamper, and cross-scope tests pass;
- provenance links remain complete and verifiable;
- denied authority remains unavailable;
- cleanup returns the environment to a known state.

## Incident response

1. Stop validation, reads, and materialization.
2. Preserve source, configuration, schema, policy, input, output, ledger-head, and artifact hashes.
3. Classify the trigger: version mismatch, nondeterminism, disclosure, retention/revocation failure, tamper, provenance gap, unexpected capability, or misleading claim.
4. Confirm whether any external mutation occurred.
5. Disable the affected candidate path.
6. Restore the last accepted documentation or contract state.
7. Reproduce with synthetic fixtures in an isolated environment.
8. Document cause, impact, repair, residual risk, and required approvals.
9. Re-run the complete deterministic and adversarial suite.
10. Resume only after explicit review.

## Rollback triggers

Rollback is mandatory when a change:

- widens repository authority;
- changes canonical bytes or hashes without migration;
- accepts unknown or ambiguous versions;
- produces nondeterministic decisions;
- weakens capability, purpose, sensitivity, retention, expiry, or revocation enforcement;
- exposes cross-scope data;
- introduces network, credentials, execution, repository writes, payments, or deployment control;
- breaks downstream version/hash acceptance;
- presents a proposal as implemented or approved.

## Documentation rollback

1. Identify the last accepted commit.
2. Revert only the documentation candidate or close the draft PR.
3. Rebuild the previous site with `mkdocs build --strict`.
4. Verify that no Pages deployment or release artifact was published without approval.
5. Preserve the rejected candidate and review record for provenance.
6. Update `changelog.md` and the builder log with the rollback evidence.

## Contract rollback

A future contract rollback must preserve historical decision identity. Restore the previously accepted version and policy hashes, disable the rejected version, verify migration reversal, re-run fixtures for both old and transition states, and require downstream consumers to confirm the restored exact version/hash.

## Retirement procedure

If the charter is rejected:

1. record the decision and rationale;
2. identify any repository receiving the responsibility;
3. replace capability-oriented wording with a retirement notice;
4. link the canonical destination and migration guidance;
5. close or supersede implementation candidates;
6. preserve decision and provenance records;
7. archive the repository only after links and downstream references are updated.
