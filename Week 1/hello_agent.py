import os
from dotenv import load_dotenv
from openai import OpenAI
 
load_dotenv()
client = OpenAI()
 
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": "Hello Agent! What can you do?"}]
)
 
print(response.choices[0].message.content)

import random
 
tasks = ["search weather", "do math", "summarize text"]
 
for task in tasks:
    print(f"\n[Agent received task]: {task}")
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful agent."},
            {"role": "user", "content": f"Please {task}"}
        ]
    )
    print("[Agent output]:", response.choices[0].message.content)