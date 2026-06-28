from google.cloud import bigquery

from config import MAX_ROWS

client = bigquery.Client()


def execute_sql(sql: str):

    sql_upper = sql.upper()

    if "LIMIT" not in sql_upper:
        sql += f"\nLIMIT {MAX_ROWS}"

    query_job = client.query(sql)

    df = query_job.result().to_dataframe()

    return df.to_dict(
        orient="records"
    )
