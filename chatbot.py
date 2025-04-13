import json
import random
import pickle
from preprocess import preprocess_text

# ✅ Load trained model, vectorizer, and intents
with open("chat_model.pkl", "rb") as f:
    model, vectorizer, intents = pickle.load(f)

def chat_response(user_input):
    tokens = preprocess_text(user_input)
    input_text = ' '.join(tokens)
    input_vector = vectorizer.transform([input_text])
    prediction = model.predict(input_vector)[0]

    for intent in intents['intents']:
        if intent['tag'] == prediction:
            return random.choice(intent['responses'])

    return "I'm not sure how to respond to that."
