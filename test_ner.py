import spacy

nlp=spacy.load("en_core_web_sm")

text = "Rijin Jenjen studied at KTU University and lives in Kerala."
doc=nlp(text)
for ent in doc.ents:
     print(f"{ent.text} --> {ent.label_}")