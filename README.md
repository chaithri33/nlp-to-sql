# NLP to SQL Analytics Agent

An Agentic AI system built using Google ADK and BigQuery.

## Features

- Natural Language to SQL
- Dynamic BigQuery Schema Retrieval
- SQL Guardrails
- BigQuery Query Execution
- Analytics Agent
- OpenRouter Integration

## Architecture

User Query
→ Root Agent
→ Schema Tool
→ SQL Agent
→ Guardrail Tool
→ BigQuery Tool
→ Analytics Agent

## Setup

```bash
pip install -r requirements.txt
```

Create `.env`

```env
OPENROUTER_API_KEY=your_key
```

Run:

```bash
python main.py
```
