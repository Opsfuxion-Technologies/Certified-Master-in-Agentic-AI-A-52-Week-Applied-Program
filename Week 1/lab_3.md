
---

## 🧠 **Lab 3: Setting Up Your Agentic AI Development Environment**

### 🎯 **Goal**

Set up a **fully functional local development environment** where you can experiment with **Agentic AI**, **LLM APIs**, and frameworks like **LangChain** and **CrewAI**.

You’ll install dependencies, configure your `.env` file, run your first LLM-powered script, and create a mini agent loop to simulate intelligent task handling.

---

### ⏱ **Estimated Time**

**90–120 minutes**

---

### 📦 **Deliverable**

A **working Python environment** capable of:

* Connecting to an LLM API
* Running a simple agent loop

---

## ⚙️ **Step-by-Step Instructions**

---

### 🧩 **Step 1: Install Python & Package Manager (10–15 min)**

1. Check your current Python version:

   ```bash
   python3 --version
   ```

2. If Python < 3.11, install Python 3.11+:

   * macOS:

     ```bash
     brew install python@3.11
     ```
   * Windows / Linux:
     Download from [python.org](https://www.python.org/downloads/)

3. Upgrade `pip`:

   ```bash
   python3 -m pip install --upgrade pip
   ```

---

### 🧱 **Step 2: Set Up a Virtual Environment (10 min)**

Create and activate a virtual environment to isolate dependencies:

```bash
python3 -m venv agentic_env
```

Activate it:

* **macOS/Linux:**

  ```bash
  source agentic_env/bin/activate
  ```
* **Windows:**

  ```bash
  agentic_env\Scripts\activate
  ```

You should now see `(agentic_env)` at the start of your terminal prompt.

---

### 📚 **Step 3: Install Core Libraries (15 min)**

Inside your virtual environment, install the key libraries:

```bash
pip install openai langchain crewai chromadb faiss-cpu requests
```

**Optional but recommended:**

```bash
pip install jupyter ipykernel python-dotenv
```

---

### 💻 **Step 4: Set Up an IDE or Notebook (10 min)**

1. Install an IDE (e.g. **VS Code**, **PyCharm**, or use **Jupyter Notebook**).
2. In **VS Code**:

   * Add the **Python extension**.
   * Select your virtual environment as the **interpreter**:

     ```
     Command Palette → Python: Select Interpreter → agentic_env
     ```

---

### 🔐 **Step 5: Configure API Keys Securely (10–15 min)**

1. Sign up for an **OpenAI API key** (or another LLM API provider).
   [https://platform.openai.com/](https://platform.openai.com/)

2. Create a `.env` file in your **project folder** (not in the virtual environment!):

   ```bash
   OPENAI_API_KEY=your_api_key_here
   ```

3. Install `python-dotenv` (if not yet installed):

   ```bash
   pip install python-dotenv
   ```

---

### 🤖 **Step 6: Run Your First LLM Call (15 min)**

Create a new file named **`hello_agent.py`**:

```python
import os
from dotenv import load_dotenv
from openai import OpenAI

# Load API key
load_dotenv()

# Initialize client
client = OpenAI()

# Send a simple message to the model
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": "Hello Agent! What can you do?"}]
)

# Print the LLM’s response
print(response.choices[0].message.content)
```

Then run it:

```bash
python hello_agent.py
```

✅ You should see a friendly AI-generated response like:

> “Hi there! I can assist with reasoning, problem-solving, and much more!”

---

### 🔁 **Step 7: Test a Mini-Agent Loop (20–25 min)**

Extend `hello_agent.py` to simulate a **basic agent loop**:

```python
import random
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
client = OpenAI()

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
```

When you run this, your agent will:

1. Receive a task
2. Process it through the LLM
3. Output a reasoned response

You’ve just simulated an **agentic reasoning loop** 🔄

---

### 📝 **Step 8: Document Your Setup (10 min)**

Create a **`README.md`** in your project folder documenting:

* Python version
* Installed libraries
* Environment setup steps
* Output from your test runs

**Important:**
🚫 Never commit your `.env` file to GitHub.

---

## ✅ **Outcome**

By completing this lab, you now have:

* A clean Python virtual environment (`agentic_env`)
* LLM connectivity using OpenAI API
* Core libraries for Agentic AI frameworks (LangChain, CrewAI)
* A working agent simulation script
* A well-documented local setup

This environment forms the **foundation** for all upcoming labs — including:

* Framework integration
* Memory systems
* RAG pipelines
* Multi-agent collaboration

---

