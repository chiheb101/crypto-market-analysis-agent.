
from agent.graph import graph


# Use one thread ID for this conversation
config = {
    "configurable": {
        "thread_id": "crypto-user-001"
    },
    "recursion_limit": 10
}


print("\n===== CRYPTO MARKET ANALYSIS AGENT =====")
print("Ask me anything about cryptocurrency.")
print("Type 'exit' to stop the conversation.\n")


while True:

    question = input("You: ")

    if question.strip().lower() == "exit":
        print("Agent: Goodbye!")
        break

    # Execute the agent with the current question
    result = graph.invoke(
        {"messages": [
            {"role": "user", "content": question}
        ]},
        config=config
    )

    # Display the final answer
    answer = result["messages"][-1].content

    print("\nAgent:", answer)
    print()
