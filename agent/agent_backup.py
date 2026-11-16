
import os
import json

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage, ToolMessage

from tools.crypto_tools import get_crypto_market_data
from tools.news_tools import search_crypto_news


# Load environment variables
load_dotenv()


# Initialize the OpenAI model
llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0,
    max_tokens=120
)


# Make tools available to the model
tools = [
    get_crypto_market_data,
    search_crypto_news
]

llm_with_tools = llm.bind_tools(tools)


# Agent instructions
system_message = SystemMessage(
    content=(
        "You are a cryptocurrency market analysis assistant. "
        "Use the available tools when current market data or news "
        "is needed. Never invent market information. "
        "Clearly distinguish retrieved facts from your interpretation. "
        "Keep your answers concise."
    )
)


def ask_agent(question):

    messages = [
        system_message,
        HumanMessage(content=question)
    ]

    # Ask the model to decide whether to use a tool
    response = llm_with_tools.invoke(messages)

    # Store the model response
    messages.append(response)

    # Execute requested tools
    for tool_call in response.tool_calls:

        print("\nTool selected:", tool_call["name"])
        print("Arguments:", tool_call["args"])

        if tool_call["name"] == "get_crypto_market_data":
            result = get_crypto_market_data.invoke(
                tool_call["args"]
            )

        elif tool_call["name"] == "search_crypto_news":
            result = search_crypto_news.invoke(
                tool_call["args"]
            )

        else:
            raise ValueError("Unknown tool requested")

        # Return the tool result to the model
        messages.append(
            ToolMessage(
                content=json.dumps(result),
                tool_call_id=tool_call["id"]
            )
        )

    # Ask the model to generate its final answer
    if response.tool_calls:
        final_response = llm.invoke(messages)
    else:
        final_response = response

    return final_response.content
