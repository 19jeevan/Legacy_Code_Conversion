import os


def load_java_code(root_dir: str):
    code_files = []

    for root, _, files in os.walk(root_dir):
        for file in files:
            if file.endswith(".java"):
                path = os.path.join(root, file)

                with open(path, "r", encoding="utf-8", errors="replace") as f:
                    code_files.append({
                        "path": path,
                        "content": f.read()
                    })

    return code_files