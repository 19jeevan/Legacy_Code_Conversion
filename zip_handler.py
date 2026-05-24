import zipfile
import os
import shutil


def extract_zip(uploaded_zip, extract_path="temp_java"):
    if os.path.exists(extract_path):
        shutil.rmtree(extract_path)

    os.makedirs(extract_path, exist_ok=True)

    with zipfile.ZipFile(uploaded_zip, "r") as zip_ref:
        zip_ref.extractall(extract_path)

    return extract_path