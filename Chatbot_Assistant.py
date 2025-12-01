import datetime
import time
import random

# Greeting based on time
hour = datetime.datetime.now().hour

if 5 <= hour < 12:
    greet = "Good morning"
elif 12 <= hour < 17:
    greet = "Good afternoon"
elif 17 <= hour < 21:
    greet = "Good evening"
else:
    greet = "Good night"

print(f"{greet} ☀️")
print("🤖 I am your AI Chatbot created to assist you in conversations.\n")

# Ask user name
username = input("What's your name? ")
print(f"Nice to meet you, {username}! Type 'help' to see what I can do.\n")

# Modes
mode = "normal"

# Temporary memory (very simple)
user_emotion = None

# Responses
responses = {
    "hello": ["Hello!", "Hi there!", "Hey!", "Namaste!"],
    "who are you": ["I'm your AI Study Buddy!", "I was created by Madhu Singh ❤️"],
    "motivate": [
        "Keep going, you are improving every day!",
        "Believe in yourself!",
        "One day you will be proud of your hard work 💪"
    ],
    "sad": [
        "Don't worry, tough times never last!",
        "I’m here for you.",
        "It's okay to feel sad sometimes 😊"
    ],
    "happy": [
        "Great! Happiness suits you 😄",
        "Keep smiling!",
        "Awesome! Stay positive!"
    ],
    "python": [
        "Python is simple and powerful.",
        "You can create apps, websites, AI using Python!",
        "Python is great for both beginners and pros."
    ],
    "function": [
        "A function is a block of code that performs a task.",
        "Functions help reduce repetition in code."
    ]
}

unknown_responses = [
    "I didn’t understand that.",
    "Hmm… can you say it differently?",
    "Not sure about that yet!",
    "I will learn this soon!",
    "Try asking in a simple way!"
]

def get_response(user_input):
    user_input = user_input.lower()

    # Detect keywords using simple logic
    for key in responses:
        if key in user_input:
            return random.choice(responses[key])
    return random.choice(unknown_responses)

def typing():
    print("Bot is typing", end="")
    for _ in range(3):
        print(".", end="")
        time.sleep(0.10)
    print()

print("\nChat Started!\n")

while True:
    user_input = input(f"{username}: ").lower()

    # Exit
    if "bye" in user_input:
        print("Bot: Goodbye! Have a great day 😊")
        break

    # Commands
    if user_input == "help":
        print("\nCommands you can use:")
        print("- 'time' → Get current time")
        print("- 'clear' → Clear screen simulation")
        print("- 'change mode to fun'")
        print("- 'change mode to study'")
        print("- 'bye' → Exit chat\n")
        continue

    if user_input == "time":
        now = datetime.datetime.now().strftime("%I:%M %p")
        print("Bot:", now)
        continue

    if user_input == "clear":
        print("\n" * 20)
        print("Screen cleared!\n")
        continue

    # Mode switching
    if "change mode to fun" in user_input:
        mode = "fun"
        print("Bot: Fun mode activated 🎉")
        continue

    if "change mode to study" in user_input:
        mode = "study"
        print("Bot: Study mode activated 📚")
        continue

    # Emotion memory
    if "sad" in user_input:
        user_emotion = "sad"
    elif "happy" in user_input:
        user_emotion = "happy"

    # Typing effect
    typing()

    # Generate reply
    bot_reply = get_response(user_input)

    # Personalization by mode
    if mode == "fun":
        bot_reply += " 😄"
    elif mode == "study":
        bot_reply = "📘 Study Mode: " + bot_reply

    # Emotion-based personalization
    if user_emotion == "sad":
        bot_reply += " (I'm with you 💙)"
    elif user_emotion == "happy":
        bot_reply += " (Keep shining ✨)"

    print("Bot:", bot_reply)
    print()
