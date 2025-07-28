""" Redis (REmote DIctionary Server) is a fast, in-memory key-value database, often used for:

- Caching

- Session storage

- Message queues

- Temporary or persistent memory storage

For your MCP server, Redis is used to store long-term memory, such as:

- User state or preferences

- Conversation history

- Context across sessions

It enables fast reads/writes and is suitable for both short-term and persistent memory (when configured).

Redis-backed long-term memory means:

- Storing user/client state or conversation history in Redis.

- Retrieving that data for future use across sessions.

- Optionally setting expiry or tagging data as long-term.

You can use redis-py as the Redis client and organize the data using structured keys and TTL (time-to-live) or persistent storage.
"""
# memory-manager.py

import redis
import json
from typing import Optional

class MemoryManager:
    def __init__(self, redis_url: str = "redis://localhost:6379/0"):
        self.redis = redis.Redis.from_url(redis_url, decode_responses=True)
        
    def _make_key(self, namespace:str, user_id: str)-> str:
        return f"memory:{namespace}:{user_id}"
    
    
    
    