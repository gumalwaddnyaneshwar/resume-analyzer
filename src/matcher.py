from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from src.process import clean_text

def calculate_match_score(resume_text: str, job_text: str) -> float:
    resume_clean = clean_text(resume_text)
    job_clean = clean_text(job_text)

    vectorizer = TfidfVectorizer()
    tfidf = vectorizer.fit_transform([resume_clean, job_clean])

    score = cosine_similarity(tfidf[0:1], tfidf[1:2])[0][0]
    return round(score * 100, 2)