import streamlit as st
import PyPDF2

# ----------- Skills Database -----------
skills_list = [
    "python","java","c++","html","css","javascript",
    "sql","machine learning","ai","data analysis"
]

# ----------- Job Database -----------
job_roles = {
    "Python Developer": ["python", "sql"],
    "Data Analyst": ["python", "sql", "data analysis"],
    "ML Engineer": ["python", "machine learning", "ai"],
    "Web Developer": ["html", "css", "javascript"],
    "Java Developer": ["java"]
}

# ----------- Extract Text -----------
def extract_text(file):
    pdf = PyPDF2.PdfReader(file)
    text = ""
    for page in pdf.pages:
        text += page.extract_text()
    return text.lower()

# ----------- Resume Analysis -----------
def analyze_resume(text):
    found_skills = []
    
    for skill in skills_list:
        if skill in text:
            found_skills.append(skill)
    
    score = len(found_skills) * 10
    
    return found_skills, score

# ----------- Job Recommendation Logic -----------
def recommend_job(skills):
    best_match = ""
    max_match = 0
    
    for job, required_skills in job_roles.items():
        match_count = len(set(skills) & set(required_skills))
        
        if match_count > max_match:
            max_match = match_count
            best_match = job
    
    return best_match

# ----------- UI -----------
# ----------- UI -----------
st.set_page_config(page_title="AI Resume Analyzer", page_icon="📄", layout="wide")

st.title("📄 AI Resume Analyzer & Job Recommender")

st.sidebar.header("About Project")
st.sidebar.write("""
This AI project analyzes resumes using NLP 
and recommends suitable job roles.
Developed using Python & Streamlit.
""")

uploaded_file = st.file_uploader("Upload Resume (PDF only)", type="pdf")

if uploaded_file:
    
    text = extract_text(uploaded_file)
    skills, score = analyze_resume(text)
    job = recommend_job(skills)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🔎 Skills Found")
        st.success(skills)
    
    with col2:
        st.subheader("📊 Resume Score")
        st.progress(score)
        st.write(f"{score} / 100")
    
    st.subheader("💼 Recommended Job Role")
    st.warning(job)
    
    st.markdown("---")
    st.caption("Developed by Vaibhav 🚀")