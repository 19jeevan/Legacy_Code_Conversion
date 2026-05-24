import json
from llm_client import call_llm

SYSTEM_PROMPT = """
You are a strict software auditor.
Return ONLY valid JSON.
"""


def extract_json(text: str) -> dict:
    decoder = json.JSONDecoder()

    text = text.replace("```json", "")
    text = text.replace("```", "")
    text = text.strip()

    for i, char in enumerate(text):
        if char == "{":
            try:
                obj, idx = decoder.raw_decode(text[i:])
                return obj
            except json.JSONDecodeError:
                continue

    raise ValueError("No valid JSON object found")



def evaluate_doc(java_code: str, documentation: str):
    prompt = f"""
Compare Java code and documentation.

Return ONLY JSON.

Expected format:

{{
  "coverage_score": 0.95,
  "risk_level": "LOW",
  "manual_review_items": [
    "review item"
  ]
}}

Java Code:
{java_code}

Documentation:
{documentation}
"""

    try:
        result = call_llm(SYSTEM_PROMPT, prompt)
        return extract_json(result)

    except Exception as e:
        return {
            "coverage_score": 0.0,
            "risk_level": "HIGH",
            "manual_review_items": [
                str(e)
            ]
        }