import spacy
from spacy import displacy

nlp = spacy.load("en_core_web_sm")

multiline_text = "I prefer the morinf flight through Mumbai"

multiline_doc = nlp(multiline_text)

for token in multiline_doc:
    print(
        f"""
TOKEN: {token.text}
=====
{token.tag_ = }
{token.head.text = }
{token.dep_ = }"""
    )

displacy.serve(multiline_doc, style="dep")

