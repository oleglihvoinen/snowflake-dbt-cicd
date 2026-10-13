# Release controls

This repository treats dbt delivery as a governed software release rather than a single build command.

## Pull-request gate

Every pull request passes two independent gates:

1. **Static policy** rejects broad `select *`, hard-coded production relations and destructive DDL inside model SQL.
2. **Warehouse validation** parses and builds the dbt project with fail-fast behavior.

dbt artifacts are retained so reviewers can inspect the exact manifest and run results produced by CI.

## Production gate

Production deployment is a separate, manually dispatched workflow bound to the GitHub `production` environment. The operator must provide the exact commit SHA being promoted. GitHub environment protection can require reviewers before Snowflake credentials become available.

This creates a visible chain:

`commit → PR policy → dbt build → review → exact SHA → protected environment → production build → retained artifacts`

## Further extension

For very large projects, the same design can add dbt state comparison/defer, build only modified nodes and their downstream dependencies, retain a production manifest as state, and publish run metadata into an operational audit table.
