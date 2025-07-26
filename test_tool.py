# test_tool.py

from tool_executor import execute_tool

tool_name = "math_add"
args = '{"a":10, "b":27}'
print(execute_tool(tool_name, args))

tool_name = "get_weather"
args = '{"city":Berlin}'
print(execute_tool(tool_name, args))
