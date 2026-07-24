# Safe Onboarding

## Before making changes

QSO-DIGITALIS is on an architectural hold. Contributors may improve documentation, decision records, synthetic fixtures, validators, and test plans. They may not activate a runtime, write generated scaffold files as implementation evidence, connect external services, add credentials, publish Pages, or broaden repository authority.

Read in this order:

1. [Project overview](project-overview.md)
2. [Architecture and trust boundaries](architecture.md)
3. [Contract and repository boundaries](contract-boundary.md)
4. [Developer guide](developer-guide.md)
5. [`taskchain.md`](../taskchain.md)
6. [`release.md`](../release.md)
7. [`punchlist.md`](../punchlist.md)

## Supported first contribution

A safe first contribution is one of:

- clarify a non-goal or evidence state;
- repair an internal documentation link;
- add equivalent prose for a diagram;
- add a synthetic negative fixture after a schema is approved;
- improve deterministic documentation validation;
- record an ownership vacancy or unresolved decision;
- preserve superseded evidence without presenting it as current.

## Local documentation validation

The documentation checker uses only the Python standard library:

```bash
python3 scripts/check_documentation.py
python3 -m unittest tests.test_check_documentation -v
```

A passing result confirms only the checked source structure and exact documentation rules. It does not approve the charter or establish semantic compatibility.

## Change preparation

Every pull request should state:

- the exact base and submitted head;
- documentation surfaces changed;
- whether scope, terminology, evidence state, or repository relationships changed;
- tests run and their results;
- unresolved architecture, ownership, security, privacy, accessibility, licensing, retention, migration, or rollback questions;
- confirmation that implementation and publication authority remain unchanged.

## Data and security rules

- Use synthetic, non-sensitive examples only.
- Do not add production credentials, tokens, keys, private source records, personal data, raw forensic material, or live network responses.
- Do not enable network access, external writes, autonomous actions, repository mutation, payments, or deployment.
- Do not represent hashes as proof of truth, consent, authorship, semantic compatibility, or continuing availability.
- Preserve `QSO-CONSENT-CAPACITY-LOCK-v1` and explicit human final review.

## Accessibility rules

- Use descriptive headings and link text.
- Give every meaningful diagram an equivalent prose explanation.
- Do not rely on color, icons, or spatial position alone.
- Explain states and abbreviations on first use.
- Keep tables readable as linear text.

## Stopping conditions

Stop and record a blocker when a change would:

- select the repository charter without explicit approval;
- introduce or accept a namespace or schema;
- appoint an owner or custodian;
- activate the scaffold materializer;
- require credentials or external systems;
- publish Pages or a package;
- conceal a conflict, vacancy, stale source, or rollback gap;
- infer implementation authority from documentation or CI.
