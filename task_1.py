# import nltk module
import nltk
from nltk import text

# make variabel text for processing 
text = "learn NLP using Python"

# tokenize & tagging text variabel
tokens = nltk.word_tokenize(text)
tag = nltk.pos_tag(tokens)

# output
print("Output = ",tag)