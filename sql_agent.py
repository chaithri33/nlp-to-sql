from google.adk.agents import Agent

from config import (
    MODEL_NAME,
    SQL_GENERATION_PROMPT
)

sql_agent = Agent(
    name="sql_generator",

    model=MODEL_NAME,

    instruction=SQL_GENERATION_PROMPT,
)
