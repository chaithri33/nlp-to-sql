from google.cloud import bigquery

client = bigquery.Client()


def get_schema(table_fqn: str) -> str:
    """
    table_fqn:
    project.dataset.table
    """

    table = client.get_table(table_fqn)

    schema_lines = []

    for field in table.schema:
        schema_lines.append(
            f"{field.name} ({field.field_type})"
        )

    return "\n".join(schema_lines)

