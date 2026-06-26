from google.adk.agents import Agent

from config import MODEL_NAME

from agents.sql_agent import sql_agent
from agents.analytics_agent import analytics_agent

from tools.schema_tool import get_schema
from tools.guardrail_tool import validate_sql
from tools.bigquery_tool import execute_sql


root_agent = Agent(
    name="nlp_to_sql_root_agent",

    model=MODEL_NAME,

    description="""
NLP to SQL analytics system.
""",

    instruction="""
You are an enterprise analytics assistant.

Workflow:

1. Receive user question.

2. Get schema using:
   get_schema(table_fqn)

3. Delegate SQL generation
   to sql_generator.

4. Validate SQL using:
   validate_sql()

5. Execute SQL using:
   execute_sql()

6. Delegate result explanation
   to analytics_agent.

7. Return:

   - generated SQL
   - query results
   - business insights

Never execute
UPDATE
DELETE
INSERT
DROP
ALTER
CREATE
MERGE
TRUNCATE
""",

    sub_agents=[
        sql_agent,
        analytics_agent
    ],

    tools=[
        get_schema,
        validate_sql,
        execute_sql
    ]
)
