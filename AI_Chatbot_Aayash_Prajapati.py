
# --------------------------------------------
# AI Chatbot using Python (NLTK-based)
# Author: Aayash Prajapati
# --------------------------------------------

import nltk
import random
import string

# Download NLTK data (only first time)
# Uncomment the lines below the first time you run the code
# nltk.download('punkt')
# nltk.download('wordnet')

from nltk.corpus import wordnet
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

# Initialize lemmatizer
lemmatizer = WordNetLemmatizer()

# Sample responses for chatbot
responses = {
    "hello": ["Hello there!", "Hi! How can I assist you today?", "Hey! Nice to see you 😊"],
    "how are you": ["I'm doing great! How about you?", "I'm fine, thanks for asking!", "Always ready to chat!"],
    "your name": ["I'm Aayash's AI Chatbot 🤖", "You can call me ChatBot!", "I'm a simple Python AI assistant."],
    "python": ["Python is a powerful programming language for AI, automation, and more."],
    "ai": ["AI stands for Artificial Intelligence — making machines think like humans!"],
    "cyber security": ["Cyber Security protects systems and data from digital attacks."],
    "bye": ["Goodbye! Have a nice day 😊", "See you later!", "Take care!"]
}

# Preprocessing function
def preprocess(sentence):
    tokens = word_tokenize(sentence.lower())
    tokens = [lemmatizer.lemmatize(word) for word in tokens if word.isalnum()]
    return tokens

# Find best matching response
def get_response(user_input):
    tokens = preprocess(user_input)
    for key in responses:
        if key in user_input.lower():
            return random.choice(responses[key])
    return "I'm not sure I understand that. Can you explain more?"

# Main Chat Loop
print("🤖 Aayash's AI Chatbot (type 'bye' to exit)\n")

while True:
    user_input = input("You: ")
    if "bye" in user_input.lower():
        print("Bot:", random.choice(responses["bye"]))
        break
    print("Bot:", get_response(user_input))
