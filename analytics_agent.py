from google.adk.agents import Agent

from config import MODEL_NAME


analytics_agent = Agent(
    name="analytics_agent",

    model=MODEL_NAME,

    instruction="""
You are a business analyst.

Analyze SQL query results.

Provide:

1. Key insights
2. Trends
3. Anomalies
4. Business summary

Keep explanations concise.
"""
)
