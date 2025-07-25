# tools.py
# Tool Registry

def get_weather(city: str) -> str:
    return f"The weather in {city} is 24°C and sunny" 

def math_add(a: float, b: float) -> float:
    return a+ b

TOOL_REGISTRY = {
    "get_weather": {
        "func": get_weather,
        "description": "Returns weather info for a city",
        "schema": {
            "type": "object",
            "properties": {
                "city": {"type": "string"}
            },
            "required": ["city"]
        }
    },
    "math_add": {
        "func": math_add,
        "description": "Adds two numbers",
        "schema": {
            "type": "object",
            "properties": {
                "a": {"type": "number"},
                "b": {"type": "number"}
            },
            "required": ["a", "b"]
        }
    }
}