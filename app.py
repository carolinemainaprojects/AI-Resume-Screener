import streamlit as st
st.set_page_config(
    page_title="AI Resume Screener",
    page_icon="📄",
    layout="wide"
)
import io
import json
import time
from pypdf import PdfReader
from google import genai

# ==========================================
# PAGE SETTINGS
# ==========================================

st.set_page_config(
    page_title="AI Resume Screener",
    page_icon="📄",
    layout="centered"
)

# ==========================================
# GEMINI CLIENT
# ==========================================

try:
    client = genai.Client(
        api_key=st.secrets["GEMINI_API_KEY"]
    )
except Exception:
    st.error("Gemini API key is not configured yet.")
    st.stop()

# ==========================================
# TITLE
# ==========================================

st.title("📄 AI Resume Screener")

st.write(
    "Upload your resume and compare it with a job description "
    "using Gemini AI."
)

st.divider()

# ==========================================
# RESUME UPLOAD
# ==========================================

st.subheader("📄 Step 1 — Upload Resume")

resume_file = st.file_uploader(
    "Choose your resume (PDF)",
    type=["pdf"]
)

# ==========================================
# JOB INFORMATION
# ==========================================

st.subheader("💼 Step 2 — Job Information")

job_title = st.text_input(
    "💼 Job Title",
    placeholder="Example: Program Officer"
)

job_description = st.text_area(
    "📝 Job Description",
    placeholder="Paste the job description here...",
    height=200
)

# ==========================================
# ANALYZE BUTTON
# ==========================================

analyze_button = st.button(
    "🤖 Analyze Resume",
    type="primary",
    use_container_width=True
)

# ==========================================
# ANALYSIS
# ==========================================

if analyze_button:

    if resume_file is None:
        st.warning("⚠️ Please upload a PDF resume first.")
        st.stop()

    if not job_title.strip():
        st.warning("⚠️ Please enter a job title.")
        st.stop()

    if not job_description.strip():
        st.warning("⚠️ Please enter a job description.")
        st.stop()

    try:

        with st.spinner("🤖 Analyzing your resume..."):

            # ----------------------------------
            # EXTRACT PDF TEXT
            # ----------------------------------

            pdf_data = resume_file.read()

            reader = PdfReader(io.BytesIO(pdf_data))

            resume_text = ""

            for page in reader.pages:
                text = page.extract_text()

                if text:
                    resume_text += text + "\n"

            if not resume_text.strip():
                st.error("❌ No readable text was found in this PDF.")
                st.stop()

            # ----------------------------------
            # GEMINI PROMPT
            # ----------------------------------

            prompt = f"""
You are an expert Applicant Tracking System
and professional recruiter.

Analyze the resume and compare it with the job description.

Return ONLY valid JSON.

Do not include markdown.
Do not include code fences.
Do not include explanations outside the JSON.

Use exactly this structure:

{{
    "resume_score": 0,
    "job_match_score": 0,
    "top_skills": [],
    "strengths": [],
    "weaknesses": [],
    "matching_skills": [],
    "missing_skills": [],
    "suitable_roles": [],
    "improvement_suggestions": [],
    "summary": "",
    "recommendation": ""
}}

RESUME:
{resume_text}

JOB TITLE:
{job_title}

JOB DESCRIPTION:
{job_description}
"""

            # ----------------------------------
            # CALL GEMINI
            # ----------------------------------

                        response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents=prompt
            )

            response_text = response.text.strip()

            # ----------------------------------
            # CLEAN JSON RESPONSE
            # ----------------------------------

            if response_text.startswith("```"):
                response_text = response_text.replace(
                    "```json", ""
                )
                response_text = response_text.replace(
                    "```", ""
                )
                response_text = response_text.strip()

            analysis = json.loads(response_text)

        # ======================================
        # DISPLAY RESULTS
        # ======================================

        st.success("🎉 Complete AI analysis finished!")

        st.divider()

        st.header("📊 AI Resume Screening Report")

        st.subheader("⭐ Resume Score")
        st.metric(
            "Resume Score",
            f"{analysis['resume_score']}/100"
        )

        st.subheader("🎯 Job Match Score")
        st.metric(
            "Job Match",
            f"{analysis['job_match_score']}/100"
        )

        st.subheader("💼 Job")
        st.write(job_title)

        st.subheader("🎯 Recommendation")
        st.write(analysis["recommendation"])

        st.subheader("🛠️ Top Skills")
        for item in analysis["top_skills"]:
            st.write(f"• {item}")

        st.subheader("💪 Strengths")
        for item in analysis["strengths"]:
            st.write(f"• {item}")

        st.subheader("⚠️ Weaknesses")
        for item in analysis["weaknesses"]:
            st.write(f"• {item}")

        st.subheader("✅ Matching Skills")
        for item in analysis["matching_skills"]:
            st.write(f"• {item}")

        st.subheader("❌ Missing Skills")
        for item in analysis["missing_skills"]:
            st.write(f"• {item}")

        st.subheader("💼 Suitable Roles")
        for item in analysis["suitable_roles"]:
            st.write(f"• {item}")

        st.subheader("💡 Improvement Suggestions")
        for item in analysis["improvement_suggestions"]:
            st.write(f"• {item}")

        st.subheader("📝 Professional Summary")
        st.write(analysis["summary"])

        # ======================================
        # DOWNLOAD REPORT
        # ======================================

        report = f"""
AI RESUME SCREENING REPORT
==========================

JOB TITLE
{job_title}

RESUME SCORE
{analysis["resume_score"]}/100

JOB MATCH SCORE
{analysis["job_match_score"]}/100

RECOMMENDATION
{analysis["recommendation"]}

TOP SKILLS
{chr(10).join("- " + x for x in analysis["top_skills"])}

STRENGTHS
{chr(10).join("- " + x for x in analysis["strengths"])}

WEAKNESSES
{chr(10).join("- " + x for x in analysis["weaknesses"])}

MATCHING SKILLS
{chr(10).join("- " + x for x in analysis["matching_skills"])}

MISSING SKILLS
{chr(10).join("- " + x for x in analysis["missing_skills"])}

SUITABLE JOB ROLES
{chr(10).join("- " + x for x in analysis["suitable_roles"])}

IMPROVEMENT SUGGESTIONS
{chr(10).join("- " + x for x in analysis["improvement_suggestions"])}

PROFESSIONAL SUMMARY
{analysis["summary"]}

==========================
SCREENING COMPLETED
==========================
"""

        st.download_button(
            label="📥 Download Complete Report",
            data=report,
            file_name="AI_Resume_Screener_Report.txt",
            mime="text/plain",
            use_container_width=True
        )

    except json.JSONDecodeError:
        st.error(
            "❌ Gemini returned an invalid response. "
            "Please try the analysis again."
        )

    except Exception as error:
        st.error("❌ Something went wrong.")
        st.write(f"Error: {type(error).__name__}")
        st.write(f"Details: {error}")

st.divider()

st.caption("🤖 Powered by Gemini AI")
