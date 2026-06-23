import spacy
from PyPDF2 import PdfReader
from skills import skills
from extractor import extract_email, extract_phone

# Load NER model
nlp = spacy.load("en_core_web_sm")

# Read PDF
pdf = PdfReader("RJ NEW CV.pdf")

text = ""

for page in pdf.pages:
    page_text = page.extract_text()

    if page_text:
        text += page_text

# Apply NER
doc = nlp(text)
print("\n===== EMAIL =====\n")
print(extract_email(text))

print("\n===== PHONE =====\n")
print(extract_phone(text))
found_skills = []

for skill in skills:
    if skill.lower() in text.lower():
        found_skills.append(skill)

print("\n===== SKILLS FOUND =====\n")

for skill in found_skills:
    print(skill)

print("\n===== ENTITIES FOUND =====\n")

for ent in doc.ents:
    print(f"{ent.text} --> {ent.label_}")