from google.adk.agents import Agent

from config import (
    MODEL_NAME,
    SQL_GENERATION_PROMPT
)

nlp_agent = Agent(

    name="nlp_agent",

    model=MODEL_NAME,

    description="Converts natural language into BigQuery SQL.",

    instruction=SQL_GENERATION_PROMPT
)
