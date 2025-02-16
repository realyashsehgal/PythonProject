from DbManager import get_db_connection
import re


# Master skill list for better extraction
MASTER_SKILLS = [
    "python", "java", "c++", "sql", "machine learning", "deep learning",
    "data analysis", "excel", "flask", "django", "html", "css", "javascript",
    "react", "node.js", "tensorflow", "pandas", "numpy", "scikit-learn", "git"
]

def extract_skills_from_resume(resume_text):
    """
    Extracts relevant skills from the resume text by matching against MASTER_SKILLS.
    """
    resume_words = set(re.findall(r'\b\w+\b', resume_text.lower()))  # Extract words
    matched_skills = {skill for skill in MASTER_SKILLS if skill in resume_words}

    print(f"Extracted Resume Words: {resume_words}")  # Debugging
    print(f"Matched Skills: {matched_skills}")  # Debugging

    return matched_skills


def job_match(resume_text):
    """
    Matches extracted resume skills with job postings in the database.
    """
    db = get_db_connection()
    cursor = db.cursor()

    # Extract skills from resume
    resume_skills = extract_skills_from_resume(resume_text)

    # Fetch jobs from database
    cursor.execute("SELECT id, title, skills_req, description, date_posted, link FROM jobs")
    jobs = cursor.fetchall()

    matching_jobs = []

    for job in jobs:
        job_id, job_title, job_skills, job_desc, job_date, job_link = job

        # Convert job skills to lowercase and split into words
        job_skills_set = {skill.strip().lower() for skill in job_skills.split(',')}

        print(f"Job Title: {job_title}")  # Debugging
        print(f"Resume Skills: {resume_skills}")  # Debugging
        print(f"Job Skills: {job_skills_set}")  # Debugging
        print(f"Matched Skills: {resume_skills & job_skills_set}\n")  # Debugging

        # Check if at least one skill in resume matches job skills
        if resume_skills & job_skills_set:  # Intersection check
            matching_jobs.append({
                "title": job_title,
                "description": job_desc,
                "link": job_link
            })

    db.close()
    return matching_jobs