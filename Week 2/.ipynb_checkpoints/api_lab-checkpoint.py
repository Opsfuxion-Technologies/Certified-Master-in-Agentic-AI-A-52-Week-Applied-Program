# Hello, GET request (10 min)
# Use a stable public API (JSONPlaceholder) to fetch posts.

import requests, json
 
BASE = "https://jsonplaceholder.typicode.com"
r = requests.get(f"{BASE}/posts/1", timeout=10)
r.raise_for_status()
data = r.json()
print(type(data), data["id"], data["title"])
Inspect response metadata:

print("Status:", r.status_code)
print("Content-Type:", r.headers.get("content-type"))
print("Preview:", json.dumps(data, indent=2)[:300])
