# Snowflake + dbt Release Engineering

A governed CI/CD pattern for Snowflake/dbt that treats analytical transformations as a **controlled software release**, not just a `dbt build` command.

## Release flow

```text
commit
  ↓
pull request
  ├─ static SQL policy
  ├─ Python policy tests
  ├─ dbt parse/build
  └─ retained dbt artifacts
  ↓
review / merge
  ↓
exact approved Git SHA
  ↓
protected GitHub production environment
  ↓
production dbt build
  ↓
retained manifest + run results
```

## Implemented controls

- static policy scanner for model SQL
- blocks broad `select *`
- blocks hard-coded PROD/PRODUCTION relations
- blocks destructive DDL in model SQL
- automated policy tests
- pull-request dbt parse/build with fail-fast behavior
- artifact retention for `manifest.json`, `run_results.json` and catalog when present
- separate production deployment workflow
- exact commit-SHA verification before deployment
- GitHub environment boundary for production approvals/secrets
- documented path to dbt state-aware/slim CI

This repository demonstrates release governance. Actual Snowflake execution requires repository secrets and environment-specific roles.

**Technologies:** Snowflake · dbt · GitHub Actions · Python · SQL policy-as-code · CI/CD · release governance · DevOps
