select
    current_timestamp() as pipeline_checked_at,
    current_database() as database_name,
    current_schema() as schema_name
