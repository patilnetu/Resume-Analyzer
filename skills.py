SKILLS_DB = [
    "pyhton", "java", "c++", "c", "machine learning",
    "data analysis", "flask", "django","sql",
    "html", "css", "javascript", "react",
    "node", "mongodb", "pands", "numpy",
    "excel", "power bi", "deep learning"
]

def extract_skills(text):
    text = text.lower()
    found_skills = []

    for skill in SKILLS_DB:
        if skill in text:
            found_skills.append(skill.title())

    return list(set(found_skills)) if found_skills else ["Not Found"]