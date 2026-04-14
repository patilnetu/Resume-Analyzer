import PyPDF2
import docx
import re
import spacy

nlp = spacy.load("en_core_web_sm")

# ------------------------------
# TEXT EXTRACTION
# -----------------------------
def extract_text(file_path):
    if file_path.endswith('.pdf'):
          return extract_pdf(file_path)
    elif file_path.endswith('.docx'):
         return extract_docx(file_path)
    elif file_path.endswith('.txt,'):
         with open(file_path, 'r', encoding= 'utf-8') as f:
           return f .read()
    return ""    
    

def extract_pdf(path):
     text =""
     with open(path,'rb)') as file:
          reader = PyPDF2.PdfReader(file)
          for page in reader .pages:
               content = page .extract_text()
               if content:
                    text += content + "\n"
     return text


def extract_docx(path):
     doc = docx.Document(path)
     return"\n" .join([para.text for para in doc.paragraphs])


# ------------------------------
# EMAIL
# ------------------------------
def extract_email(text):
     emails = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-z]{2,}',text)
     return emails[0] if emails else "not found"


# -------------------------------
#PHONE (INDIA + GENERAL)
# -------------------------------
def extract_phone(text):
     phones = re. findall(r'(+91[\-s]?)?[6-9]\d{9}', text)
     return phones[0] if phones else "Not Found"


# ---------------------------------
# NAME(HYBRAD METHOD)
# ----------------------------------
def extract_name(text):
     lines = text.strip().split("\n")

     for line in lines[:5]:
          line = lines.strip()
          if 2 < len(line) < 40:
               if re.match(r'^[A-ZA-Z ]+$', line):
                    return line 
               
     doc = nlp(text[:1000])
     for ent in doc.ents:
          if ent.label_ == "PERSON":
              return ent.text 
     
     return "Not Found"


# ---------------------------------
# EDUCATION (SMART)
# ---------------------------------

def extract_education(text):
     degrees = [
          "b.tch", "m.tech", "bachelor", "master",
          "bsc", "msc", "phd","mba", "be", "me"
     ]

     found = []
     text_lower = text.lower()

     for deg in degrees:
          if deg in text_lower:
               found.append(deg.upper())

     return list(set(found)) if found else ["Not Found"]



# -------------------------------
# EXPERIENCE (SMART)
# -------------------------------
def extract_experience(text):
     patterns = [
          r'(\d+)\+?\s+years?'
          r'(\d+)\+?\s+months?'
          r'(\d+\.d+)\s+years?'
     ]

     found = []

     for pattern in patterns:
          matches = re.findall(pattern, text.lower())
          for m in matches:
               found.append(f"{m} years")

     return list(set(found)) if found else ["Not Found"]         