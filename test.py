#test.py

import requests
res = requests.post("http://localhost:5000/mcp", json={"input": "Write a Python script", "agent": "coder"})
print(res.json())

#you can use this script or curl / postman
# curl -X POST http://localhost:5000/mcp \
#   -H "Content-Type: application/json" \
#   -d '{"input": "Plan my day", "agent": "planner"}'

# Step 7: Add Complexity (Later)
# Once basics work:

# ✅ Add function-calling support via OpenAI

# ✅ Add tools like web search or code exec

# ✅ Add long-term memory (Redis, DB)

# ✅ Secure the API (auth tokens, rate limit)

# ✅ Deploy to cloud (Render, Fly.io, AWS)