import streamlit as st
from src.matcher import calculate_match_score
from src.process import (
    extract_text_from_pdf,
    extract_text_from_docx
)

st.title("📄 Resume Analyzer")
st.write("Compare Resume with Job Description using NLP")

# Resume upload
resume_file = st.file_uploader(
    "Upload Resume (PDF or DOCX)",
    type=["pdf", "docx"]
)

# Job description upload
jd_file = st.file_uploader(
    "Upload Job Description (PDF or DOCX)",
    type=["pdf", "docx"]
)

resume_text = ""
jd_text = ""

if resume_file:
    if resume_file.name.endswith(".pdf"):
        resume_text = extract_text_from_pdf(resume_file)
    elif resume_file.name.endswith(".docx"):
        resume_text = extract_text_from_docx(resume_file)

if jd_file:
    if jd_file.name.endswith(".pdf"):
        jd_text = extract_text_from_pdf(jd_file)
    elif jd_file.name.endswith(".docx"):
        jd_text = extract_text_from_docx(jd_file)

# Optional editable text
resume_text = st.text_area("Resume Text (editable)", resume_text, height=200)
jd_text = st.text_area("Job Description Text (editable)", jd_text, height=200)

if st.button("Analyze Match"):
    score = calculate_match_score(resume_text, jd_text)
    st.success(f"Match Score: {score}%")