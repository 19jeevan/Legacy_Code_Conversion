from llm_client import call_llm

SYSTEM_PROMPT = """
You are a senior software architect.
Generate structured technical documentation.
"""


def generate_documentation(java_chunk: str) -> str:
    prompt = f"""
Analyze the Java code and generate documentation.

Include:
1. Module purpose
2. Business logic
3. Key classes
4. Methods
5. Data flow
6. Edge cases

Java Code:
{java_chunk}
"""

    return call_llm(SYSTEM_PROMPT, prompt)