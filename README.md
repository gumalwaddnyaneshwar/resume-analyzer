# 📄 AI Resume Analyzer & Job Matching System

## 📌 Problem Statement
Recruiters receive hundreds of resumes for a single job role, making manual screening slow and inefficient.
This project builds an AI-powered system that analyzes resumes and compares them with job descriptions
to generate a resume–job match score.

---

## 🎯 Project Objective
- Automatically analyze resumes using NLP
- Compare resumes with job descriptions
- Generate a resume match percentage
- Support PDF, DOCX, and text input formats
- Provide a simple web interface using Streamlit

---

## 📊 Key Features
- Upload resumes in PDF or DOCX format
- Paste job description text
- Text preprocessing using NLP
- Resume–job similarity score calculation
- Interactive Streamlit web application

---

## 🧠 Approach
1. Extract text from resume files (PDF/DOCX)
2. Clean and preprocess text
3. Apply NLP techniques:
   - Tokenization
   - Stopword removal
   - Lemmatization
4. Convert text to numerical vectors using TF-IDF
5. Calculate similarity using cosine similarity

---

## 🛠 Tech Stack
- Python
- NLTK
- Scikit-learn
- Pandas
- NumPy
- PyPDF2
- python-docx
- Streamlit

---

## 📂 Project Structure

resume-analyzer/
 ├── src/ 
 │   ├── init.py 
 │   ├── process.py 
 │   ├── matcher.py 
 ├── app.py 
 ├── requirements.txt 
 ├── README.md 
 ├── LICENSE 
 └── .gitignore


 ---

## 🚀 How to Run the Project

### 1️⃣ Clone the repository
```bash
git clone https://github.com/gumalwaddnyaneshwar/resume-analyzer.git
cd resume-analyzer


pip install -r requirements.txt

import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')


streamlit run app.py