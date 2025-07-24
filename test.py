#test.py

import requests
res = requests.post("http://localhost:5000/mcp", json={"input": "Write a Python script", "agent": "coder"})
print(res.json())

#you can use this script or curl / postman
# curl -X POST http://localhost:5000/mcp \
#   -H "Content-Type: application/json" \
#   -d '{"input": "Plan my day", "agent": "planner"}'
