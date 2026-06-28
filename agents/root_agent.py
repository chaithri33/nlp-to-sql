from google.adk.agents import Agent

from config import MODEL_NAME

from agents.schema_agent import schema_agent
from agents.nlp_agent import nlp_agent

from tools.guardrail_tool import validate_sql
from tools.bigquery_tool import execute_sql


root_agent = Agent(

    name="root_agent",

    model=MODEL_NAME,

    description="""
Root orchestrator for the NLP-to-SQL workflow.
""",

    instruction="""
You are the Root Agent.

Workflow:

1. Receive the user's question.

2. Delegate schema retrieval to the Schema Agent.

3. Delegate SQL generation to the NLP Agent.

4. Validate the generated SQL using validate_sql.

5. Execute the validated SQL using execute_sql.

6. Return:
   - Generated SQL
   - Query results

Never execute:
- UPDATE
- DELETE
- INSERT
- DROP
- ALTER
- CREATE
- MERGE
- TRUNCATE
""",

    sub_agents=[
        schema_agent,
        nlp_agent
    ],

    tools=[
        validate_sql,
        execute_sql
    ]
)
