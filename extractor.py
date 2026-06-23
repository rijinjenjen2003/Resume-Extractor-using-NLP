import re

def extract_email(text):
    emails = re.findall(r'[\w\.-]+@[\w\.-]+\.\w+', text)
    return emails

def extract_phone(text):
    phones = re.findall(r'\+?\d[\d\s\-]{8,15}', text)
    return phones