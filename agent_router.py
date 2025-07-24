# agent_router.py

from llm_clients import call_openai, call_claude

def route_to_agent(agent_name, user_input):
    if agent_name == "planner":
        prompt = f"You are a planner. Task: {user_input}"
        return call_openai(prompt)
    elif agent_name == "coder":
        prompt = f"You are a coding agent. User asks: {user_input}"
        return call_claude(prompt)
    else:
        prompt = f"You are a helpful assistant. User asks: {user_input}"
        return call_openai(prompt)