from llm_client import call_llm

SYSTEM_PROMPT = """
You are a senior Python architect.
Generate production-ready Python code.
"""


def generate_python_from_doc(documentation: str):
    prompt = f"""
Generate Python code from the following documentation.

Rules:
- Use dataclasses
- Use type hints
- Modular architecture
- Production-ready code
- No Java syntax

Documentation:
{documentation}
"""

    return call_llm(SYSTEM_PROMPT, prompt)