# main.py

from memory_manager import MemoryManager # memory-manager - has issues 

memory = MemoryManager()

user_id = "user123"
namespace = "chat" #chat for conversation history, "state" for user context, "session" for session-related (local) data

#save memory
memory.save_memory(namespace, user_id, {"last_message": "hello world"})

# You can pass TTL (the time limit) in seconds to save_memory() if you'd like the memory to expire at a set interval
memory.save_memory("chat", "user123", {"msg": "Hello"}, ttl=3600) #Expires in 1 hour

# retrieve memory
data = memory.get_memory(namespace, user_id)
print("Loaded Memory :", data)

# Append Memory
memory.append_memory(namespace, user_id, {"last_command": "/start"})

# Delete Memory
# memory.delete_memory(namespace, user_id)

# Integration / Steps
""" To integrate this into your MCP server:

- Instantiate MemoryManager when initializing your server.

- Use get_memory and save_memory during request processing.

- Optionally trigger appends or resets on events (e.g., user disconnects, conversation ends).# """
