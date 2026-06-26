from agents.root_agent import root_agent


def run_agent():

    table_fqn = (
        "my-project.sales.customer_data"
    )

    question = input(
        "Ask a question: "
    )

    prompt = f"""
Table:

{table_fqn}

Question:

{question}
"""

    response = root_agent.run(prompt)

    print(response)


if __name__ == "__main__":
    run_agent()
