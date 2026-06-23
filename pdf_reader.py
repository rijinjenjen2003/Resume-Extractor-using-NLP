from PyPDF2 import PdfReader

pdf=PdfReader("RJ NEW CV.pdf")
text=""
for page in pdf.pages:
    text+=page.extract_text()
print(text)