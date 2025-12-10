## 🧠 Personal Helper Agent (Google ADK)

A modular, scalable AI-powered personal assistant built using Google ADK (Agent Development Kit) with support for:

✅ Tool-based reasoning (Time, Calculator, Web Search)

✅ Centralized configuration (config.yaml)

✅ Secure environment management (.env)

✅ Per-agent model configuration

✅ Future-ready multi-agent architecture

✅ Clean root-agent entrypoint for ADK

This project is designed for research, experimentation, real-world deployment, and future expansion into specialized AI agents.

### 📁 Project Structure
````
project_root
│   .env
│   .env.example
│   config.yaml
│   README.md
│   requirements.txt
│
└───src
    │   agent.py                # ✅ ADK entrypoint (root agent loader)
    │   config_loader.py        # ✅ Centralized config + env loader
    │
    ├───agents
    │   │   __init__.py
    │   └───assistant
    │       │instructions.py
    │       │agent.py        # ✅ Assistant agent 
    │       │   __init__.py
    │
    └───tools
            calc_tools.py      # ✅ Math expression evaluator
            time_tools.py      # ✅ time tool
            __init__.py

````
### 🚀 Features
✅ Root Assistant Agent

Acts as the primary interface for users

Uses tools instead of guessing

Can delegate tasks to auxiliary agents (future)

✅ Built-in Tools

UTC Time Tool – Fully timezone-safe

Calculator Tool – Evaluates math expressions

Google Search Tool (ADK Built-in) – For real-time web queries

✅ Configuration System

config.yaml – Static application & agent configuration

.env – Secure runtime secrets (API keys)

config_loader.py – Loads everything once, cached

✅ Per-Agent Model Control

Each agent can use a different LLM model via:

agents:
  assistant:
    model: gemini-2.5-flash


Future agents can safely use different models like:

agents:
  planner:
    model: gemini-2.5-pro

## ⚙️ Installation
1️⃣ Clone the Repository
git clone <your-repo-url>
cd Personal-helper

2️⃣ Create Virtual Environment (Recommended)
python -m venv venv
venv\Scripts\activate   # Windows

3️⃣ Install Dependencies
pip install -r requirements.txt

▶️ Running the Agent

From the project root:

adk run src


Or use the web UI:

adk web src


✅ ADK automatically loads:

src/agent.py → agents/assistant/agent.py → root_agent

