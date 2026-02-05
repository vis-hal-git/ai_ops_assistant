# AI Operations Assistant

A powerful, agentic AI assistant built with **LangGraph**, **LangChain**, and **Streamlit**. This tool is designed to autonomously plan, execute, and verify operations tasks such as fetching weather data, retrieving news, and searching GitHub repositories.

## 🚀 Features

- **Intelligent Planning**: Breaks down complex user requests into executable steps.
- **Autonomous Execution**: Uses specialized tools to gather information.
- **Verification Layer**: Reviews results to ensure accuracy before presenting the final answer.
- **Tools Included**:
    - 🌤️ **Weather**: Real-time weather updates.
    - 📰 **News**: Latest headlines and articles.
    - 💻 **GitHub**: Repository search and stats.

## 🛠️ Prerequisites

- Python 3.8 or higher.
- API Keys for:
    - **OpenAI** (LLM power)
    - **Weather API** (e.g., OpenWeatherMap)
    - **News API** (e.g., NewsAPI.org)
    - **GitHub** (Optional, for higher rate limits)

## 📦 Installation

1.  **Clone the Repository**
    ```bash
    git clone <repository-url>
    cd ai_ops_assistant
    ```

2.  **Create a Virtual Environment** (Recommended)
    ```bash
    python -m venv venv
    # Windows
    .\venv\Scripts\activate
    # macOS/Linux
    source venv/bin/activate
    ```

3.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure Environment Variables**
    Copy the example environment file and fill in your keys:
    ```bash
    cp .env.example .env
    ```
    Open `.env` and add your API keys:
    ```env
    OPENAI_API_KEY="sk-..."
    WEATHER_API_KEY="..."
    NEWS_API_KEY="..."
    GITHUB_TOKEN="..."
    ```

## ▶️ Usage

Run the Streamlit application:

```bash
streamlit run main.py
```

Or simply:

```bash
python main.py
```

The web interface will open in your browser. Enter a task in the text box and click **Run**.

### Example Tasks
- "What is the current weather in New York and the latest news about AI?"
- "Find the top 5 machine learning repositories on GitHub and summarize them."
- "Check the weather in London."

## 📂 Project Structure

- `agents/`: Logic for Planner, Executor, and Verifier agents.
- `graph/`: LangGraph state machine definition.
- `tools/`: Interfaces for external APIs (Weather, Github, News).
- `ui/`: Streamlit frontend code.
- `llm/`: OpenAI client setup.
- `main.py`: Entry point for the application.
