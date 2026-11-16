# Crypto Market Analysis Agent

## 1. Project Overview

The Crypto Market Analysis Agent is an AI-powered application developed in Python. Its purpose is to provide cryptocurrency market information and news through a conversational interface.

The application uses OpenAI GPT-4o mini, LangChain, and LangGraph to create an intelligent agent that can understand user questions, select the appropriate tools, retrieve external information, and generate relevant answers.

The agent retrieves cryptocurrency market data through FreeCryptoAPI and cryptocurrency-related news through NewsAPI. It also maintains conversation history, allowing users to ask follow-up questions without repeating previous information.

## 2. Project Objectives

The main objectives of this project are:

- Develop an AI agent capable of answering cryptocurrency-related questions.
- Retrieve cryptocurrency market information using an external API.
- Search for cryptocurrency-related news.
- Implement a ReAct agent architecture using LangGraph.
- Enable the agent to select and use tools according to the user's questions.
- Implement conversation memory to support follow-up questions.
- Improve reliability by handling API errors and missing information.

## 3. Technologies and Tools

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| OpenAI GPT-4o mini | Language model used by the agent |
| LangChain | Integration of the language model and tools |
| LangGraph | Agent workflow and ReAct architecture |
| FreeCryptoAPI | Cryptocurrency market information |
| NewsAPI | Cryptocurrency-related news |
| Requests | Communication with external APIs |
| Python-dotenv | Loading API keys from environment variables |

## 4. Project Architecture

The project is organized into three main folders:

### `agent/`

Contains the main LangGraph agent implementation.

- `graph.py`: Defines the ReAct workflow, language model, available tools, and conversation memory.
- `agent_backup.py`: Backup of the earlier manual agent implementation.

### `services/`

Contains the functions responsible for communicating with external APIs.

- `crypto_api.py`: Retrieves cryptocurrency market data from FreeCryptoAPI.
- `news_api.py`: Retrieves cryptocurrency news from NewsAPI.

### `tools/`

Contains the LangChain tools that the agent can select and execute.

- `crypto_tools.py`: Provides cryptocurrency market information.
- `news_tools.py`: Searches for cryptocurrency-related news.

### Main project files

- `main.py`: Starts the application and manages the conversation with the user.
- `requirements.txt`: Lists the Python dependencies.
- `.env`: Stores API keys and environment variables.
- `.gitignore`: Excludes sensitive and unnecessary files from version control.

## 5. ReAct Agent Architecture

The application uses the ReAct (Reasoning and Acting) approach through LangGraph.

The agent follows an iterative process:

1. **Reason:** The language model analyzes the user's question and decides which tool is needed.
2. **Act:** LangGraph executes the selected tool.
3. **Observe:** The agent receives and examines the tool's result.
4. **Repeat or Respond:** The agent can request additional information using another tool or generate its final answer.

For example, when a user asks to compare Bitcoin and Ethereum and explain recent Bitcoin news, the agent can retrieve market data for both cryptocurrencies and search for relevant news before generating its response.

This approach allows the agent to make decisions dynamically instead of following a fixed sequence of operations.

## 6. Conversation Memory

Conversation memory is implemented using LangGraph's `InMemorySaver` checkpointer.

Each conversation is identified by a unique `thread_id`. This allows the agent to retain previous messages and understand follow-up questions.

For example:

- User: What is the current price of Bitcoin?
- User: What about Ethereum?
- User: Which one performed better today?

The agent can use the information retrieved during the previous interactions to answer the final question.

The current implementation uses in-memory storage. Therefore, conversation history is lost when the application is restarted.

## 7. External APIs

### FreeCryptoAPI

FreeCryptoAPI provides the cryptocurrency market information used by the agent.

The application retrieves information such as:

- Cryptocurrency symbol.
- Latest returned price.
- Daily percentage change.
- Lowest and highest returned prices.
- Data timestamp.
- Source exchange.

### NewsAPI

NewsAPI is used to search for cryptocurrency-related articles.

The application retrieves:

- Article titles.
- Publisher names.
- Publication dates.
- Descriptions.
- Article URLs.

**Note:** The NewsAPI Developer plan has a publication delay of up to 24 hours. Therefore, its results should not be considered breaking or real-time news.

## 8. Installation and Execution

### Requirements

- Python 3.11 or later.
- A FreeCryptoAPI account and API key.
- A NewsAPI account and API key.
- An OpenAI API key.

### Step 1: Clone or download the project

Download the project and open its folder in Visual Studio Code.

### Step 2: Create a virtual environment

```bash
python -m venv .venv
```

Activate it in Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### Step 3: Install dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Configure environment variables

Create a `.env` file in the project root directory:

```env
OPENAI_API_KEY=your_openai_api_key
FREECRYPTO_API_KEY=your_freecrypto_api_key
NEWS_API_KEY=your_news_api_key
```

Replace the example values with your own API keys.

Never publish or share this file.

### Step 5: Run the application

```bash
python main.py
```

The application will start an interactive conversation in the terminal.

To stop the application, type:

```text
exit
```

## 9. Example Questions

Users can ask questions such as:

- What is the current price of Bitcoin?
- Find recent news about Ethereum.
- Compare Bitcoin and Ethereum.
- Which cryptocurrency performed better today?
- Explain how recent Bitcoin news could influence its market.

The agent selects the appropriate tools according to the user's questions.

## 10. Error Handling and Reliability

The application includes basic error handling to improve reliability.

It can handle situations such as:

- Invalid cryptocurrency symbols.
- Missing market data.
- API connection failures.
- Unavailable news results.
- Missing information in returned market data.

The agent is also instructed not to invent market information and to explain when requested data is unavailable.

Additionally, it is designed to focus on cryptocurrency-related questions rather than general-purpose questions.

## 11. Limitations

The current implementation has several limitations:

- Conversation memory is temporary and stored in memory.
- Market information depends on the availability and accuracy of FreeCryptoAPI.
- NewsAPI Developer plan results can be delayed by up to 24 hours.
- The application currently operates through a terminal interface.
- The agent focuses on cryptocurrency market information and related news.
- The application does not provide guaranteed financial predictions or investment advice.

## 12. Conclusion

This project demonstrates how an AI agent can combine a language model, external APIs, tools, and conversation memory to perform cryptocurrency market analysis.

By implementing the ReAct architecture with LangGraph, the application can dynamically select tools, retrieve information, observe results, and generate answers based on the available data.

The project also provides practical experience with agentic AI concepts, API integration, tool calling, and conversational memory.
