import nltk
from nltk.chat.util import Chat, reflections

pairs = [
    (r"hi|hello", ["Hello!", "Hi there!"]),
    (r"what is your name?", ["I am a Python chatbot"]),
    (r"how are you?", ["I'm doing great!"]),
    (r"bye", ["Goodbye!"])
]

chatbot = Chat(pairs, reflections)
print("🤖 Chatbot: Hello! Type 'bye' to exit.")
chatbot.converse()
