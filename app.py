import streamlit as st
import os
import shutil
import json

from zip_handler import extract_zip
from modernizer import run_modernization


st.set_page_config(
    page_title="Legacy Code Modernizer",
    layout="wide"
)

st.title("🧠 Legacy Java → Python Modernizer")

if "completed" not in st.session_state:
    st.session_state.completed = False


uploaded_zip = st.file_uploader(
    "Upload Java ZIP File",
    type=["zip"]
)


if uploaded_zip:

    st.success("ZIP uploaded successfully")

    if st.button("🚀 Start Modernization"):

        with st.spinner("Extracting ZIP..."):
            java_root = extract_zip(uploaded_zip)

        with st.spinner("Running modernization pipeline..."):
            evaluation = run_modernization(java_root)

        st.session_state.completed = True
        st.success("Modernization completed")


if st.session_state.completed:

    st.subheader("📘 Documentation Preview")

    with open(
        "output/docs/system_documentation.md",
        "r",
        encoding="utf-8",
        errors="replace"
    ) as f:

        st.text_area(
            "Generated Documentation",
            f.read(),
            height=300
        )

    st.subheader("📊 Evaluation Dashboard")

    with open(
        "output/evaluation.json",
        "r",
        encoding="utf-8"
    ) as f:
        report = json.load(f)

    st.json(report)

    high_risk = [
        r for r in report
        if r.get("risk_level") == "HIGH"
    ]

    st.metric("High Risk Components", len(high_risk))

    # ----------------------------
    # Create ZIPs
    # ----------------------------

    def zip_folder(folder_path, zip_name):
        if os.path.exists(folder_path):
            shutil.make_archive(zip_name, "zip", folder_path)

    zip_folder("output/python_code", "python_code")
    zip_folder("output/tests", "tests")
    zip_folder("output/docs", "documentation")

    st.subheader("⬇️ Download Outputs")

    if os.path.exists("python_code.zip"):
        st.download_button(
            label="Download Python Code",
            data=open("python_code.zip", "rb"),
            file_name="python_code.zip",
            key="python_zip"
        )

    if os.path.exists("tests.zip"):
        st.download_button(
            label="Download Tests",
            data=open("tests.zip", "rb"),
            file_name="tests.zip",
            key="tests_zip"
        )

    if os.path.exists("documentation.zip"):
        st.download_button(
            label="Download Documentation",
            data=open("documentation.zip", "rb"),
            file_name="documentation.zip",
            key="docs_zip"
        )

    if os.path.exists("output/evaluation.json"):
        st.download_button(
            label="Download Evaluation Report",
            data=open("output/evaluation.json", "rb"),
            file_name="evaluation.json",
            key="eval_json"
        )
