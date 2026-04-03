import requests
import json
import re


def extract_json(text):
    match = re.search(r"\{.*\}", text, re.DOTALL)
    if match:
        return match.group()
    return "{}"


def parse_step(step):
    step_lower = step.lower()

    # ✅ RULE-BASED FIX
    if "open" in step_lower:
        url = re.findall(r"https?://\S+", step)
        if url:
            return {"action": "open", "value": url[0]}

    if "validate" in step_lower and "title" in step_lower:
        if "facebook" in step_lower:
            return {"action": "validate", "type": "title", "value": "Facebook"}
        
    if "email" in step_lower:
            value=step.split()[-1]
            return {
        "action": "send_keys",
        "locator": "//label[contains(text(),'Email')]/../input",
        "value": value
    }    

    if "password" in step_lower:
            value=step.split()[-1]
            return {
        "action": "send_keys",
        "locator": "//label[contains(text(),'Password')]/../input",
        "value": value
    }   

    if "log in" in step_lower or "login" in step_lower:
       return {
        "action": "click",
        "locator": "//button[@name='login']"
    }

    if "click" in step_lower and "login" in step_lower:
       return {
        "action": "click",
        "locator": "//button[@name='login']"
    }

    

    # ✅ PROMPT (keep your updated one)
    prompt = f"""
You are a machine that ONLY outputs JSON.

STRICT RULES:
- Output ONLY JSON
- NO explanation
- NO text
- NO sentences
- NO examples
- NO markdown
- NO extra characters

If you fail, return:
{{"action":"unknown"}}

Valid format:
{{
  "action": "...",
  "locator": "...",
  "value": "..."
}}

Step: {step}
"""

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
        
        "model": "phi",
        "prompt": prompt,
        "stream": False,
        "temperature": 0   # 🔥 important
}
    )

    res_json = response.json()
    print("FULL API RESPONSE:", res_json)

    if "response" in res_json:
        raw_output = res_json["response"]
    else:
        print("⚠️ Invalid API response:", res_json)
        return {"action": "unknown"}   # ✅ fixed indentation

    print("LLM RAW:", raw_output)

    # ✅ extract JSON
    cleaned = extract_json(raw_output)
    print("CLEANED:", cleaned)

    try:
        return json.loads(cleaned)   # ✅ properly indented
    except:
        return {"action": "unknown", "raw": raw_output}