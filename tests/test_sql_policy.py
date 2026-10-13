from ci.sql_policy import inspect_sql


def write(tmp_path, sql):
    p = tmp_path / "model.sql"
    p.write_text(sql, encoding="utf-8")
    return p


def test_select_star_is_rejected(tmp_path):
    assert "select_star" in inspect_sql(write(tmp_path, "select * from {{ ref('x') }}"))


def test_hardcoded_production_relation_is_rejected(tmp_path):
    issues = inspect_sql(write(tmp_path, "select a from PROD.CORE.CUSTOMERS"))
    assert "hardcoded_production_relation" in issues


def test_destructive_ddl_is_rejected(tmp_path):
    assert "destructive_ddl" in inspect_sql(write(tmp_path, "drop table PROD.CORE.X"))


def test_normal_dbt_model_passes(tmp_path):
    assert inspect_sql(write(tmp_path, "select order_id from {{ ref('stg_orders') }}")) == []
