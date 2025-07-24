# llm_clients.py
# Connect to remote models

import os
import openai
import anthropic
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")
claude_client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

def call_openai(prompt):
    response = openai.ChatCompletion.create(
        model = "gpt-4",
        messages = [{"role": "user", "content": prompt}],
        temperature = 0.7
    )
    return response.choices[0].message['content']

def call_claude(prompt):
    response = claude_client.messages.create(
        model ="claude-3-opus-20240229",
        max_tokens=1000,
        messages=[
            {"role":"user", "content": prompt}
        ]
    )
    return response.content[0].text 

