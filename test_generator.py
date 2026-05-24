from llm_client import call_llm

SYSTEM_PROMPT = """
You are a QA engineer.
Generate PyTest test cases.
"""


def generate_tests(python_code: str):
    prompt = f"""
Generate unit tests for the following Python code.

Include:
- Happy paths
- Edge cases
- Exception tests

Python Code:
{python_code}
"""

    return call_llm(SYSTEM_PROMPT, prompt)