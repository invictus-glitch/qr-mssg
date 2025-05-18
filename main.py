from flask import Flask
import random

app = Flask(__name__)

messages = [
    # Motivational
    "You're awesome!",
    "Keep going, you're doing great!",
    "Smile — it looks good on you!",
    "Why not you? Why not now?",
    "You've got this!",

    # Funny
    "I'm not lazy, I'm on energy-saving mode.",
    "404: Motivation not found.",
    "If Monday had a face, I would punch it.",
    "You have something on your chin... no, the third one down.",
    "You’re not weird, you’re limited edition.",

    # Sarcastic
    "Oh wow, you're still trying? Adorable.",
    "Sure, Jan.",
    "Don’t worry, failure builds character. You must be *overflowing* with it.",
    "You deserve a round of applause... for surviving yourself.",
    "Great job... for someone with your skillset.",

    # Flirty
    "Are you a magician? Because whenever I look at you, everyone else disappears.",
    "Do you believe in love at first scan?",
    "You just scanned the best decision of your day.",
    "Do you have a map? Because I just got lost in your QR code.",
    "I wasn’t staring… I was just admiring greatness.",

    # Beizzati
    "You're the reason shampoo has instructions.",
    "You're not ugly… you’re just creatively challenged.",
    "You're proof that evolution can go in reverse.",
    "If I had a dollar for every smart thing you said, I’d be broke.",
    "You bring everyone so much joy... when you leave the room."
]

@app.route('/')
def home():
    return f"<h1 style='font-family:sans-serif;text-align:center;margin-top:20%'>{random.choice(messages)}</h1>"

if __name__ == '__main__':
    app.run()
