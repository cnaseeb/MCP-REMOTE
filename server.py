# server.py

from flask import Flask, request, jsonify
from agent_router import route_to_agent

app = Flask(__name__)

@app.route("/mcp", methods=["POST"])
def handle_mcp():
    data = request.get_json()
    user_input = data.get("input", "")
    agent_name = data.get("agent", "default")
    
    response = route_to_agent(agent_name, user_input)
    return jsonify({"response": response})

if __name__ =="__main__":
    app.run(port=5000)