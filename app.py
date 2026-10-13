import streamlit as st
import requests

st.set_page_config(page_title="AI Hiring Intelligence", page_icon="📋", layout="wide")
st.title("AI Hiring Intelligence System")
st.caption("AI-assisted resume evaluation · Human review required")

st.info("Upload a text-based PDF. Candidate data is transmitted to your configured n8n endpoint for analysis.")

with st.form("candidate_analysis"):
    position = st.text_input("Position name (optional)")
    jd = st.text_area("Job description", height=180, placeholder="Paste the role requirements here...")
    resumes = st.file_uploader("Upload Candidate Resumes (PDF)", type=["pdf"], accept_multiple_files=True)
    submit = st.form_submit_button("Analyze candidate", type="primary")

if submit:
    try:
        webhook = st.secrets["N8N_WEBHOOK_URL"]
    except (KeyError, FileNotFoundError):
        st.error("Configure N8N_WEBHOOK_URL in your Streamlit app secrets first.")
        st.stop()
    if not webhook.startswith("https://"):
        st.error("Use an HTTPS n8n production webhook URL.")
        st.stop()
    if not jd.strip() or resume is None:
        st.warning("Please provide both a job description and a PDF resume.")
        st.stop()
    if resume.size > 10 * 1024 * 1024:
        st.error("Please use a resume smaller than 10 MB.")
        st.stop()
    with st.spinner("Analyzing resume with n8n and Gemini..."):
        try:
            response = requests.post(
                webhook,
                data={"Job Description": jd, "Position Name": position},
                files={"Resume": (resume.name, resume.getvalue(), "application/pdf")},
                timeout=180,
            )
            response.raise_for_status()
            payload = response.json()
        except requests.exceptions.RequestException:
            st.error("The n8n workflow could not be reached or returned an error. Check its execution log and production webhook URL.")
            st.stop()
        except ValueError:
            st.error("The workflow did not return JSON. Add a Respond to Webhook node that returns evaluation JSON.")
            st.stop()

    if isinstance(payload, list):
        candidates = payload
    elif isinstance(payload, dict):
        candidates = payload.get("candidates")
        if candidates is None:
            candidates = [payload]
    else:
        candidates = []

    if not isinstance(candidates, list) or not candidates:
        st.error("No candidate result was returned. Review the n8n response configuration.")
        st.stop()

    for candidate in candidates:
        if not isinstance(candidate, dict):
            continue
        if candidate.get("analysis_failed") or candidate.get("parsing_error"):
            st.error("Candidate analysis failed. Please review this resume manually.")
            continue
        st.subheader(candidate.get("candidate_name", "Candidate evaluation"))
        st.write("**Degree:**", candidate.get("degree", "Not stated"))
        st.write("**Total professional experience:**", candidate.get("years_exp", candidate.get("total_experience", "Not stated")))
        cols = st.columns(5)
        for col, (title, key) in zip(cols, [
            ("Overall", "overall_score"), ("Technical", "tech_score"),
            ("Projects", "proj_score"), ("Education", "edu_score"),
            ("Experience", "exp_score"),
        ]):
            col.metric(title, candidate.get(key, "—"))
        st.write("**Experience match:**", candidate.get("experience_match", "Not stated"))
        st.write("**Recruiter takeaway:**", candidate.get("recruiter_takeaway", "Not stated"))
        for title, field in [("Matched qualifications", "matched_qualifications"), ("Skill gaps", "skill_gaps")]:
            entries = candidate.get(field, [])
            if isinstance(entries, list) and entries:
                st.write(f"**{title}:**")
                for entry in entries:
                    st.write("-", str(entry))
    st.caption("Scores are decision-support estimates, not automatic hiring decisions. Review evidence and applicable hiring policies before acting.")
