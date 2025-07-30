# async_agent_orchestrator.py

import asyncio
from typing import List, Dict, Any

# Simulate the existing MCP server's tool execution

class MCPToolExecutor:
    def __init__(self):
        self.available_tools = {
            "summarize" : self.summarize
            "translate" : self.translate
        }
        
        async def execute(self, tool_name: str, input_data: str) -> str:
            if tool_name in self.available_tools:
                return await self.available_tools[tool_name](input_data)
            else:
                raise ValueError(f"Tool '{tool_name}' not available.")
            
        async def summarize(self, text:str) -> str:
            await asyncio.sleep(1) # simulate processing
            return f"Summary: {text[:50]}..."
        
        async def translate(self, text:str) -> str:
            await asyncio.sleep(1)
            return f"Translated (mock): {text[::-1]}"
        
# Orchestrator to run tasks in sequence (asynchronously)
class AgentOrchestrator:
    def __init__(self, executor: MCPToolExecutor):
        self.executor = executor
        
    async def run_pipeline(self, tasks: List[Dict[str, Any]]) -> List[Str]:
        results = []
        for task in tasks:
            tool = task["tool"]
            input_data = task["input"]
            print(f"Running tool: {tool} with input: {input_data}")
            result = await self.execute(tool, input_data)
            print(f"Output: {result}\n")
            results.append(result)
        return results
    
# Usage
async def main():
    eexecutor = MCPToolExecutor()
    orchestrator = AgentOrchestrator(executor)
    
    task_pipeline = [
        {"tool" : "summarize", "input": "This is a long paragraph that needs summarizing."},
        {"tool" : "translate", "input": "Hello, how are you doing?"},
    ]
            
    final_outputs = await orchestrator.run_pipeline(task_pipeline)
    print("Final outputs:", final_outputs)
    
if __name__ =="__main__"
asyncio.run(main())