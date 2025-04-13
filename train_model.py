import json
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from preprocess import preprocess_text

# ✅ Load the intents data from JSON
with open("intents.json", "r", encoding="utf-8") as f:
    intents = json.load(f)

# ✅ Prepare training data
X = []
y = []

for intent in intents["intents"]:
    for pattern in intent["patterns"]:
        tokens = preprocess_text(pattern)
        text = " ".join(tokens)
        X.append(text)
        y.append(intent["tag"])

# ✅ Vectorize text data
vectorizer = CountVectorizer()
X_vectorized = vectorizer.fit_transform(X)

# ✅ Train Naive Bayes model
model = MultinomialNB()
model.fit(X_vectorized, y)

# ✅ Save model, vectorizer, and intents
with open("chat_model.pkl", "wb") as f:
    pickle.dump((model, vectorizer, intents), f)

print("✅ Model trained and saved successfully.")
