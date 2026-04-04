import requests

OLLAMA_URL = "http://localhost:11434/api/generate"

# Calling API(Pro Level initialization)
def call_llm(prompt):
    for model in ["llama3", "phi", "mistral"]:
        try:
            response = requests.post(
                OLLAMA_URL,
                json={
                    "model": model,
                    "prompt": prompt,
                    "stream": False
                }
            )

            data = response.json()

            if "response" in data and data["response"].strip():
                print(f"✅ Using model: {model}")
                return data["response"]

        except Exception as e:
            print(f"❌ {model} failed:", e)

    return ""


def generate_steps_from_goal(goal):
    prompt = f"""
You are a test automation step generator.

STRICT RULES:
- DO NOT write code
- DO NOT write python
- DO NOT write explanations
- ONLY write simple test steps
- ONE step per line

ALLOWED FORMAT:
open https://www.facebook.com
enter email test@gmail.com
enter password 123456
click login

FORBIDDEN:
- import
- driver
- selenium
- code
- comments

Goal:
{goal}

Output:
"""

    output = call_llm(prompt)
# Filtering step
    steps = []

    print("RAW LLM OUTPUT:\n", output)

    for line in output.split("\n"):
        line = line.strip().lower()

        if any(line.startswith(x) for x in ["open", "enter", "click"]):
           steps.append(line)

    return steps