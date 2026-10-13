
import streamlit as st
import requests

st.set_page_config(
    page_title="AI Hiring Intelligence",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI Hiring Intelligence System")
st.write("AI-powered candidate screening and recruitment.")

job_description = st.text_area(
    "Enter Job Description",
    height=180
)

resume = st.file_uploader(
    "Upload Candidate Resume",
    type=["pdf", "txt"]
)

if st.button("Analyze Candidate"):
    if not job_description or not resume:
        st.warning("Please provide a job description and resume.")
    else:
        st.info(
            "Frontend is ready. Connect your n8n workflow "
            "to enable AI-powered resume analysis."
        )
