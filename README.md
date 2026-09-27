# Snowflake + dbt CI/CD

Portfolio/reference implementation of a Git-based CI workflow for dbt transformations running on Snowflake.

## Delivery flow
```text
Feature branch -> Pull request -> dbt build/test -> review -> merge -> production deployment
```

## Demonstrated controls
- dbt-snowflake installed in a repeatable runner
- Automated `dbt deps` and `dbt build`
- Snowflake configuration supplied through GitHub secrets
- Pull-request validation
- Version-controlled data transformation delivery

Required secrets: `SNOWFLAKE_ACCOUNT`, `SNOWFLAKE_USER`, `SNOWFLAKE_PASSWORD`, `SNOWFLAKE_ROLE`, `SNOWFLAKE_WAREHOUSE`, `SNOWFLAKE_DATABASE`, and `SNOWFLAKE_SCHEMA`.

For a production platform I would additionally use environment protection, least-privilege roles, state-aware/slim CI, artifact retention and operational monitoring.
