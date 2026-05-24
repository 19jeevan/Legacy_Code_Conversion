import os
import json
import shutil

from code_loader import load_java_code
from chunker import chunk_code
from documentation import generate_documentation
from evaluator import evaluate_doc
from python_generator import generate_python_from_doc
from test_generator import generate_tests



def clear_output_folder():
    if os.path.exists("output"):
        shutil.rmtree("output")

    os.makedirs("output/docs", exist_ok=True)
    os.makedirs("output/python_code", exist_ok=True)
    os.makedirs("output/tests", exist_ok=True)



def run_modernization(java_root: str):
    clear_output_folder()

    evaluation_results = []

    files = load_java_code(java_root)

    for file in files:
        chunks = chunk_code(file["content"])

        for chunk in chunks:

            # Generate documentation
            doc = generate_documentation(chunk)

            # Evaluate documentation
            evaluation = evaluate_doc(chunk, doc)
            evaluation_results.append(evaluation)

            # Generate Python code from documentation
            py_code = generate_python_from_doc(doc)

            # Generate unit tests
            tests = generate_tests(py_code)

            # Save documentation
            with open(
                "output/docs/system_documentation.md",
                "a",
                encoding="utf-8"
            ) as f:
                f.write(doc + "\n\n")

            # Save Python code
            with open(
                "output/python_code/app.py",
                "a",
                encoding="utf-8"
            ) as f:
                f.write(py_code + "\n\n")

            # Save tests
            with open(
                "output/tests/test_app.py",
                "a",
                encoding="utf-8"
            ) as f:
                f.write(tests + "\n\n")

    # Save evaluation report
    with open(
        "output/evaluation.json",
        "w",
        encoding="utf-8"
    ) as f:
        json.dump(evaluation_results, f, indent=2)

    return evaluation_results
