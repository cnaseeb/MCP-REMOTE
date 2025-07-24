# memory.py
# adding memory support (optional)
# simple in-mem cache
# use it when routing agents if needed

convesation_memory = {}

def update_memory(agent, user_input, model_output):
    if agent not in convesation_memory:
        convesation_memory[agent] = []
    convesation_memory[agent].append({"user": user_input, "model": model_output})
    
def get_memory(agent):
    return convesation_memory.get(agent, [])