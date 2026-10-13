
import streamlit as st
import requests

st.set_page_config(
    page_title="AI Hiring Intelligence",
    page_icon="📋",
    layout="wide"
)

st.title("AI Hiring Intelligence System")
st.caption("AI-assisted resume evaluation | Human review required")

st.info(
    "Upload multiple text-based PDF resumes. "
    "Candidate data will be sent to your n8n workflow."
)

# Candidate analysis form
with st.form("candidate_analysis"):
    position = st.text_input("Position name (optional)")

    jd = st.text_area(
        "Job description",
        height=180,
        placeholder="Paste the role requirements here..."
    )

    resumes = st.file_uploader(
        "Upload Candidate Resumes (PDF)",
        type=["pdf"],
        accept_multiple_files=True
    )

    submit = st.form_submit_button(
        "Analyze Candidates",
        type="primary"
    )

if submit:

    # Validate form
    if not jd.strip() or not resumes:
        st.warning(
            "Please provide a job description "
            "and at least one PDF resume."
        )
        st.stop()

    if any(file.size > 10 * 1024 * 1024 for file in resumes):
        st.error("Each resume must be smaller than 10 MB.")
        st.stop()

    # Get n8n webhook URL
    try:
        webhook = st.secrets["N8N_WEBHOOK_URL"]
    except (KeyError, FileNotFoundError):
        st.error(
            "Configure N8N_WEBHOOK_URL "
            "in your Streamlit secrets first."
        )
        st.stop()

    if not webhook.startswith("https://"):
        st.error("Use an HTTPS n8n production webhook URL.")
        st.stop()

    st.info(f"Analyzing {len(resumes)} resume(s)...")

    # Send all resumes to n8n
    with st.spinner("Analyzing candidates with n8n and Gemini..."):

        try:
            files = [
                (
                    "Resume",
                    (
                        file.name,
                        file.getvalue(),
                        "application/pdf"
                    )
                )
                for file in resumes
            ]

            response = requests.post(
                webhook,
                data={
                    "Job Description": jd,
                    "Position Name": position
                },
                files=files,
                timeout=180
            )

            response.raise_for_status()
            payload = response.json()

        except requests.exceptions.RequestException:
            st.error(
                "Could not connect to the n8n workflow. "
                "Check the webhook URL and n8n execution logs."
            )
            st.stop()

        except ValueError:
            st.error(
                "n8n did not return valid JSON. "
                "Configure a Respond to Webhook node."
            )
            st.stop()

    # Extract candidate results
    if isinstance(payload, list):
        candidates = payload

    elif isinstance(payload, dict):
        candidates = payload.get("candidates")

        if candidates is None:
            candidates = [payload]
    else:
        candidates = []

    if not isinstance(candidates, list) or not candidates:
        st.error("No candidate results were returned.")
        st.stop()

    st.success("Analysis response received!")

    st.subheader("Candidate Evaluation Results")

    # Display each candidate
    for candidate in candidates:

        if not isinstance(candidate, dict):
            continue

        if candidate.get("analysis_failed") or candidate.get("parsing_error"):
            st.error("Candidate analysis failed. Review manually.")
            continue

        with st.container(border=True):

            st.subheader(
                candidate.get(
                    "candidate_name",
                    "Candidate Evaluation"
                )
            )

            st.write(
                "**Degree:**",
                candidate.get("degree", "Not stated")
            )

            st.write(
                "**Experience:**",
                candidate.get(
                    "years_exp",
                    candidate.get(
                        "total_experience",
                        "Not stated"
                    )
                )
            )

            cols = st.columns(5)

            scores = [
                ("Overall", "overall_score"),
                ("Technical", "tech_score"),
                ("Projects", "proj_score"),
                ("Education", "edu_score"),
                ("Experience", "exp_score")
            ]

            for col, (title, key) in zip(cols, scores):
                col.metric(
                    title,
                    candidate.get(key, "—")
                )

            st.write(
                "**Experience Match:**",
                candidate.get(
                    "experience_match",
                    "Not stated"
                )
            )

            st.write(
                "**Recruiter Takeaway:**",
                candidate.get(
                    "recruiter_takeaway",
                    "Not stated"
                )
            )

            for title, field in [
                ("Matched Qualifications", "matched_qualifications"),
                ("Skill Gaps", "skill_gaps")
            ]:

                entries = candidate.get(field, [])

                if isinstance(entries, list) and entries:
                    st.write(f"**{title}:**")

                    for entry in entries:
                        st.write("-", str(entry))

    st.caption(
        "AI scores are decision-support estimates, "
        "not automatic hiring decisions. "
        "Human review is required."
    )
