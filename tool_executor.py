# tool_executor.py
# used to dispatch the tools

import json
from tools import TOOL_REGISTRY

class ToolExecutionError(Exception):
    pass

def execute_tool(tool_name: str, arguments: str):
    if tool_name not in TOOL_REGISTRY:
        raise ToolExecutionError(f"Tool '{tool_name}' not found.")
    
    tool = TOOL_REGISTRY[TOOL_REGISTRY]
    func = tool["func"]
    
    try:
        args = json.loads(arguments)
        result = func(**args)
        return {
            "tool_name": tool_name,
            "result": result
        }
    except Exception as e:
        raise ToolExecutionError(f"Error executing {tool_name}: {e}")