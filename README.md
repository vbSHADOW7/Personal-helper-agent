# 🧠 Personal Helper Agent (Google ADK)

A modular, scalable **AI-powered personal assistant** built using **Google Agent Development Kit (ADK)** with support for:

- ✅ Tool-based reasoning (Time, Calculator, Web Search)
- ✅ Centralized configuration using `config.yaml`
- ✅ Secure environment variables using `.env`
- ✅ Per-agent model configuration
- ✅ Multi-agent ready architecture
- ✅ Clean ADK root-agent entrypoint

---

## 📁 Project Structure
```
📁 Personal-helper
├── .env
├── .env.example
├── config.yaml
├── README.md
├── requirements.txt
│
│
└── src/
    ├── agent.py
    ├── config_loader.py
    │
    ├── agents/
    │   ├── __init__.py
    │   └── assistant/
    │       ├── agent.py
    │       └── __init__.py
    │
    └── tools/
        ├── calc_tools.py
        ├── time_tools.py
        └── __init__.py

```
---

## 🚀 Features

### ✅ Root Assistant Agent
- Acts as the main interface for users
- Uses tools instead of guessing
- Can delegate tasks to future auxiliary agents

### ✅ Built-in Tools
- **UTC Time Tool** – Always returns UTC
- **Calculator Tool** – Evaluates math expressions
- **Google Search Tool (ADK Built-in)** – For real-time web queries

### ✅ Centralized Configuration
- `config.yaml` → static settings
- `.env` → secrets & runtime environment
- `config_loader.py` → loads everything once using caching

### ✅ Per-Agent Model Support
Each agent can use a different model:

```yaml
agents:
  assistant:
    model: gemini-2.5-flash
```

## ⚙️ Installation
### 1️⃣ Clone the repository
```
git clone https://github.com/your-username/Personal-helper.git  
cd Personal-helper
```
### 2️⃣ Create virtual environment (recommended)
```
python -m venv venv  
venv\Scripts\activate   # Windows
```
### 3️⃣ Install dependencies
````
pip install -r requirements.txt
````
## ▶️ Running the Agent

    From project root:

    adk run src


    Web UI:

    adk web src


    ADK automatically loads:

    src/agent.py → agents/assistant/agent.py → root_agent
