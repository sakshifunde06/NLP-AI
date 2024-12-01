#import libraries
import spacy

# Load the language model
nlp = spacy.load("en_core_web_sm")

# Define the input text with spaces between sentences
about_text = (
   "india is country."
)

# 1. Tokenization:
about_doc = nlp(about_text)
print("1. Tokenization:")
for token in about_doc:
    print(token, token.idx)

# 2. Stop Words Removal:
about_doc = nlp(about_text)
print("\n2. Stop Words Removal:")
print([token for token in about_doc if not token.is_stop])

# 3. Lemmatization:
about_doc = nlp(about_text)
print("\n3. Lemmatization:")
for token in about_doc:
    if str(token) != str(token.lemma_):
        print(f"{str(token):>20} : {str(token.lemma_)}")

# 4. Part of Speech Tagging:
about_doc = nlp(about_text)
print("\n4. Part of Speech Tagging:")
for token in about_doc:
    print(
        f"""
TOKEN: {str(token)}
=====
TAG: {str(token.tag_):10} POS: {token.pos_}
EXPLANATION: {spacy.explain(token.tag_)}"""
    )
