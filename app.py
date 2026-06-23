import streamlit as st
import spacy
from PyPDF2 import PdfReader
from skills import skills
from extractor import extract_email, extract_phone

st.set_page_config(page_title="Resume Extractor", page_icon="📄")

st.title("📄 Resume Extractor")

uploaded_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])

if uploaded_file is not None:

    # Load spaCy model
    nlp = spacy.load("en_core_web_sm")

    # Read PDF
    pdf = PdfReader(uploaded_file)

    text = ""

    for page in pdf.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + "\n"

    # Extract Name (First line approach)
    lines = [line.strip() for line in text.split("\n") if line.strip()]

    if lines:
        name = lines[0]
    else:
        name = "Not Found"

    # Extract Email
    email = extract_email(text)

    # Extract Phone
    phone = extract_phone(text)

    # Extract Skills
    found_skills = []

    for skill in skills:
        if skill.lower() in text.lower():
            found_skills.append(skill)

    # Apply NER
    doc = nlp(text)

    # Display Results
    st.success("Resume Processed Successfully!")

    st.subheader("👤 Name")
    st.write(name)

    st.subheader("📧 Email")
    st.write(email if email else "Not Found")

    st.subheader("📱 Phone")
    st.write(phone if phone else "Not Found")

    st.subheader("🛠 Skills Found")

    if found_skills:
        for skill in found_skills:
            st.write(f"✅ {skill}")
    else:
        st.write("No skills found")

    st.subheader("🏷 Named Entities")

    entities_found = False

    for ent in doc.ents:
        st.write(f"**{ent.text}** → {ent.label_}")
        entities_found = True

    if not entities_found:
        st.write("No entities found")

    st.subheader("📄 Resume Text")

    with st.expander("View Extracted Text"):
        st.text(text)

else:
    st.info("Please upload a PDF resume.")