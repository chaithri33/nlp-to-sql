# AI-Powered Text-to-SQL Analytics Agent

A multi-agent AI system built using **Google Agent Development Kit (ADK)** that converts natural language questions into secure BigQuery SQL queries. The application dynamically retrieves table schemas, generates SQL, validates queries using guardrails, and executes only safe read-only queries on BigQuery.

## ✨ Features

* Multi-agent architecture using Google ADK
* Natural Language to BigQuery SQL conversion
* Dynamic BigQuery schema retrieval
* SQL guardrails for secure query execution
* BigQuery integration for real-time analytics
* Support for Gemini/OpenRouter models

## 🛠️ Technologies

* Python
* Google ADK
* Google BigQuery
* SQL
* Google Gemini / OpenRouter
* Pandas

## 🔄 Workflow

1. User submits a natural language query.
2. Root Agent orchestrates the workflow.
3. Schema Agent retrieves the table schema.
4. NLP Agent generates the SQL query.
5. Guardrail Tool validates the generated SQL.
6. BigQuery Tool executes the query and returns the results.

## 🔒 Security

The system executes only read-only SQL queries. Operations such as **UPDATE, DELETE, INSERT, DROP, ALTER, CREATE, MERGE,** and **TRUNCATE** are blocked before execution.

## 🚀 Getting Started

```bash
pip install -r requirements.txt
python main.py
```

Create a `.env` file with your API key:

```env
OPENROUTER_API_KEY=your_openrouter_api_key
```

## 📌 Sample Query

> Show the top 10 users with the highest reputation.


