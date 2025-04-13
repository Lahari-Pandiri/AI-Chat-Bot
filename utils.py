import random

def get_response(tag, intents):
    for intent in intents["intents"]:
        if intent["tag"] == tag:
            return random.choice(intent["responses"])
    return "I don't understand that."
