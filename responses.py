import random


RESPONSES = {

    "greetings": [
        "Hello! Nice to meet you.",
        "Hi! How can I help you today?",
        "Hey! I hope you are having a wonderful day.",
        "Hello there! I am happy to talk with you."
    ],


    "morning": [
        "Good morning! I hope you have a productive day.",
        "Good morning! How can I assist you today?"
    ],


    "evening": [
        "Good evening! Hope your day went well.",
        "Good evening! How may I help you today?"
    ],


    "how_are_you": [
        "I am doing great. Thank you for asking.",
        "Everything is working perfectly.",
        "I am always ready to assist you."
    ],


    "abilities": [
        "I can answer questions, remember information, learn new things, manage tasks, reminders, notes, and perform calculations.",
        
        "I am a personal AI assistant built using Python. I can chat with you and help you with daily activities."
    ],


    "thanks": [
        "You are welcome!",
        "Happy to help you.",
        "Glad I could assist you."
    ],


    "jokes": [
        "Why do programmers prefer dark mode? Because light attracts bugs!",
        
        "Why did the computer visit the doctor? Because it caught a virus!",
        
        "Why do Java developers wear glasses? Because they do not C#."
    ],


    "unknown": [
        "Okay, no problem. I will try to learn about this topic in the future.",
        
        "That is an interesting question. I will continue improving my knowledge.",
        
        "I do not know the answer right now, but you can teach me and I will remember it."
    ]

}


def get_response(category):
    """
    Return a random response from a category.
    """

    return random.choice(RESPONSES[category])