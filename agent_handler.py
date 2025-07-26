# agent_handler.py
# used to handle agent messages
# integrate with MCP server- tool call detection

from tool_executor import execute_tool, ToolExecutionError

def handle_agent_message(message):
    if "function_call" in message:
        tool_name = message["function_call"]["name"]
        args_json = message["function_call"]["arguments"]
        
        try:
            result = execute_tool(tool_name, args_json)
            return {
                "role": "system",
                "tool_result":{
                    "name": result["tool_name"],
                    "result": result["result"]
                }
            }
        except ToolExecutionError as e:
            return {
                "role": "system",
                "tool_error": str(e)
            }
    else:
        # Normal agent message routing
        pass