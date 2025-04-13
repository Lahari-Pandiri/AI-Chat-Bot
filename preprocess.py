import nltk

nltk.download("punkt")  # only once, can be removed after

from nltk.tokenize import word_tokenize

def preprocess_text(text):
    return word_tokenize(text.lower())


