
from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage

from langgraph.graph import StateGraph, START, MessagesState
from langgraph.prebuilt import ToolNode, tools_condition
from langgraph.checkpoint.memory import InMemorySaver

from tools.crypto_tools import get_crypto_market_data
from tools.news_tools import search_crypto_news


# Load environment variables
load_dotenv()


# Initialize the OpenAI model
llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0,
    max_tokens=200
)


# Define available tools
tools = [
    get_crypto_market_data,
    search_crypto_news
]


# Give the model access to the tools
llm_with_tools = llm.bind_tools(tools)


# Define the agent instructions
system_message = SystemMessage(
    content=(
        "You are a professional cryptocurrency market analysis assistant. "
        "Use the available tools to retrieve current market data and news. "
        "Decide which tools are needed based on the user's question. "
        "After observing tool results, decide whether more information "
        "is necessary. You may call multiple tools when appropriate. "
        "Never invent prices, news, or market information. "
        "Clearly distinguish facts from interpretations. "
        "Keep your final answers concise. "

        "If a tool returns an error or no results, clearly explain "
        "that the requested data is unavailable. Never invent missing data. "

        "Only answer questions directly related to cryptocurrency, "
        "crypto markets, crypto prices, and crypto news. "
        "If a question is unrelated to cryptocurrency, politely explain "
        "that you are a cryptocurrency market analysis assistant "
        "and redirect the user to a relevant question."
        "When using news information, mention the article source "
"and publication date whenever available. "
"Distinguish reported news from your own market interpretation. "
"Do not claim that news caused a price movement without evidence. "
    )
)


# Define the assistant node (REASON)
def assistant(state: MessagesState):

    response = llm_with_tools.invoke(
        [system_message] + state["messages"]
    )

    return {
        "messages": [response]
    }


# Create the graph
builder = StateGraph(MessagesState)


# Add graph nodes
builder.add_node("assistant", assistant)
builder.add_node("tools", ToolNode(tools))


# Connect the nodes
builder.add_edge(START, "assistant")

builder.add_conditional_edges(
    "assistant",
    tools_condition
)

builder.add_edge("tools", "assistant")


# Add conversation checkpointing
memory = InMemorySaver()


# Compile the graph
graph = builder.compile(
    checkpointer=memory
)
