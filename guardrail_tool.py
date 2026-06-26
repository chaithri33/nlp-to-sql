import re

from config import ALLOWED_TABLES


FORBIDDEN_KEYWORDS = [
    "UPDATE",
    "DELETE",
    "INSERT",
    "DROP",
    "ALTER",
    "CREATE",
    "MERGE",
    "TRUNCATE"
]


def validate_sql(sql: str):

    sql_upper = sql.upper()

    # block dangerous statements

    for keyword in FORBIDDEN_KEYWORDS:

        if re.search(
            rf"\b{keyword}\b",
            sql_upper
        ):
            raise ValueError(
                f"Forbidden operation detected: {keyword}"
            )

    # allow only SELECT / WITH

    if not (
        sql_upper.strip().startswith("SELECT")
        or sql_upper.strip().startswith("WITH")
    ):
        raise ValueError(
            "Only SELECT statements are allowed"
        )

    # table whitelist validation

    found_tables = re.findall(
        r"`([^`]*)`",
        sql
    )

    for table in found_tables:

        if table not in ALLOWED_TABLES:
            raise ValueError(
                f"Unauthorized table: {table}"
            )

    return True
