from spacy.lang.en import English

nlp = English()

doc = nlp('Hello world!')

for token in doc:
    print(token.text)

token = doc[-1]
print (type(token.text))


