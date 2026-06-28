from google.adk.agents import Agent

from config import MODEL_NAME
from tools.schema_tool import get_schema


schema_agent = Agent(
    name="schema_agent",

    model=MODEL_NAME,

    description="Retrieves BigQuery table schema.",

    instruction="""
You are responsible for retrieving the schema of a BigQuery table.

Whenever a table name is provided:

1. Call the get_schema tool.
2. Return only the schema.
3. Do not generate SQL.
4. Do not answer the user's question.
""",

    tools=[
        get_schema
    ]
)
