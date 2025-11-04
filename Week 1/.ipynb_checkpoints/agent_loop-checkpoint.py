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