# MCP Server with Remote LLM Integration

This project implements an agentic AI control server using a lightweight MCP (Multi-Agent Control Protocol) framework. It connects agents to powerful remote LLMs like OpenAI and Claude, and exposes an HTTP API for orchestrating tasks like planning, classification, code generation, and anomaly detection.

---

## 🚀 Features

- Agent routing to LLMs based on task type
- Remote model integration: OpenAI GPT-4, Anthropic Claude 3
- Flask-based HTTP server (`/mcp` endpoint)
- Optional agent memory module
- Small, modular codebase for easy customization

---

## 🧱 Project Structure
mcp-server/
├── agent_router.py # Routes requests to appropriate agent/model
├── llm_clients.py # API wrappers for OpenAI & Claude
├── memory.py # Optional agent memory
├── server.py # Flask MCP server
├── .gitignore # Ignores venv and secrets
├── .env # API keys (not committed)
└── README.md # This file

## 🏃 Build and run locally
docker build -t mcp-server .
docker run -p 5000:5000 --env-file .env mcp-server

## ☁️ 3. Render Deployment (Free Hosting Option)
- Go to https://render.com

- Click "New Web Service"

- Connect your GitHub repo

- Set build settings:

Build Command:  pip install -r requirements.txt
Start Command:  python server.py
Environment:    Python 3.x

- Add environment variables in the "Environment" tab:
OPENAI_API_KEY = your-key
ANTHROPIC_API_KEY = your-key

- Hit deploy!

---

## 🧪 Setup Instructions

### 1. Clone the repo

```bash
git clone <your-repo-url>
cd mcp-server


2. Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

3. Install dependencies
pip install -r requirements.txt
#If requirements.txt doesn’t exist yet, generate it with:pip freeze > requirements.txt

4. Add API keys
Create a .env file in the root directory:
OPENAI_API_KEY=your_openai_key
ANTHROPIC_API_KEY=your_claude_key


5. Running the Server
python server.py
The API will be live at http://localhost:5000/mcp

Example request (via curl):
curl -X POST http://localhost:5000/mcp \
  -H "Content-Type: application/json" \
  -d '{"input": "Plan my day", "agent": "planner"}'

🔒 .gitignore
Make sure your .gitignore includes:
venv/
.env
__pycache__/
This prevents local environments and secrets from being tracked.

To untrack venv/ if it was already committed:

git rm -r --cached venv


Future Additions
Tool calling / function execution

Redis-backed long-term memory

Async agent orchestration

Slack or web front-end integration

📄 License
MIT License — see LICENSE file.

🙌 Credits
Built with inspiration from modern agentic architectures and the growing community around multi-agent AI systems.


---

