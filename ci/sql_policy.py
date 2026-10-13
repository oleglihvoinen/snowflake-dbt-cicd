from __future__ import annotations

import argparse
from pathlib import Path
import re
import sys

SELECT_STAR = re.compile(r"\bselect\s+\*", re.IGNORECASE | re.MULTILINE)
HARDCODED_PROD = re.compile(r"\b(PROD|PRODUCTION)\.[A-Z0-9_]+\.[A-Z0-9_]+\b", re.IGNORECASE)
DESTRUCTIVE = re.compile(r"\b(drop|truncate)\s+(table|schema|database)\b", re.IGNORECASE)


def inspect_sql(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8")
    issues: list[str] = []
    if SELECT_STAR.search(text):
        issues.append("select_star")
    if HARDCODED_PROD.search(text):
        issues.append("hardcoded_production_relation")
    if DESTRUCTIVE.search(text):
        issues.append("destructive_ddl")
    return issues


def scan(root: Path) -> dict[str, list[str]]:
    findings = {}
    for path in sorted(root.rglob("*.sql")):
        issues = inspect_sql(path)
        if issues:
            findings[str(path)] = issues
    return findings


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--models", default="models")
    args = parser.parse_args()
    findings = scan(Path(args.models))
    if findings:
        for path, issues in findings.items():
            print(f"{path}: {', '.join(issues)}")
        return 1
    print("SQL policy checks passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
