# basic mcp integration
# Assuming the MCP server exposes a REST API (common setup)

import requests

MCP_SERVER_URL = MCP_SERVER

def send_mcp_message(role, content, context_id=None):
    payload = {
        "role": role,
        "content": content
    }
    if context_id:
        payload["context_id"] = context_id
        
    response = requests.post(MCP_SERVER_URL, json=payload)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"MCP Error {response.status_code}: {response.text}")
    

# Usage
if __name__ == "__main__":
    reply = send_mcp_message(role="user", content = "Summarize this document.")
    print("Agent Response", reply)