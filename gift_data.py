"""All the words live here. Edit freely; app.py just displays them.
Anything in [square brackets] is a placeholder for you to replace."""

NAME = "Chhaya"
MOM_PHONE = "1234567890"  # <- replace with her mom's number, digits only (e.g. +919876543210)

SPLASH_TITLE = "Happy Birthday, Chhaya 🎂"
SPLASH_LINE = [
    "This little corner is just for you. Open it on your birthday, or on any day you need a soft place to land.",
    "I'm glad it's you. Really.",
]

ENVELOPES = [
    {
        "title": "💌 Open when you feel low",
        "lines": [
            "Hey you. If you're here, I just want you to know you're not alone right now.",
            "You carry a lot quietly, and you do it so well. But you don't have to carry all of it today.",
            "Put it down for a little while. I'm here. We don't even have to talk, we can just sit in the same quiet.",
        ],
    },
    {
        "title": "💌 Open when you miss me",
        "lines": [
            "Main yahin hoon. A message or a call away.",
            "I'm so glad it's you. I'm choosing this, one day at a time.",
            "Drink some water, and text me when you're ready.",
        ],
    },
    {
        "title": "💌 Open when you can't sleep",
        "lines": [
            "Phone neeche rakh do, okay?",
            "Breathe in slowly for four, out for six. A few rounds is enough.",
            "You're safe here. The day is done and nothing needs solving at this hour. I'll be here in the morning.",
        ],
    },
    {
        "title": "💌 Open when you doubt yourself",
        "lines": [
            "You're an MSc student at IIT Bombay. You didn't get there by luck.",
            "You're highly capable, even on the days it doesn't feel like it. I believe in you.",
        ],
    },
    {
        "title": "💌 Open when you need a smile",
        "lines": [
            "Samir Hill. You said yes, we walked out of the library, and then you did an instant U-turn. 'Nahi, I'm not going.' Complete reverse gear. 😂",
            "And the Kanjurmarg book stall saga. Remember how seriously you bargained?",
            "Okay, smiling now? Good.",
        ],
    },
    {
        "title": "💌 Open when you want to talk to Mom",
        "lines": [
            "You don't have to be perfect to call your mom. You don't need a big reason either.",
            "If you don't know how to start, try this: **\"Maa, I've been having a rough time lately.\"**",
            "That's enough. The rest usually follows on its own.",
        ],
        "show_call": True,
    },
]

VOICE_NOTES = [
    {
        "title": "🎧 Happy Birthday",
        "file": "audio/birthday.mp3",
        "script": "Happy birthday, Chhaya. [Add what you say in the recording, 2-4 sentences.]",
    },
    {
        "title": "🎧 A funny memory",
        "file": "audio/funny.mp3",
        "script": "[Retell one funny memory, maybe the Samir Hill U-turn, in your own words.]",
    },
    {
        "title": "🎧 You're not alone",
        "file": "audio/not_alone.mp3",
        "script": "I'm here. [A few calm lines in your own voice.]",
    },
]

MEMORIES = [
    ("🕶️ Kanjurmarg", "We went for specs and ended up at a book stall. You bargained, checked prices online, scolded me, and the price came down. Fully your win."),
    ("⛰️ Samir Hill", "After the library, you said yes, then did an instant U-turn. Fastest change of mind in history."),
    ("🎬 Movies", "Spider-Man. Avengers. Popcorn, shared seats, and quiet happiness."),
    ("🌙 The unplanned night", "Late dinner, no cabs anywhere, so we booked a hotel at the last minute. A very us kind of night."),
    ("🐚 Oceanos", "Collecting little things together. Small stuff, but I remember all of it."),
]

GRATEFUL_INTRO = "Some things I never want to forget to say thank you for:"
GRATEFUL = [
    "You ordered from Flipkart for me, just like that.",
    "You made paneer and paratha for me, more than once.",
    "When I needed help with money, you didn't hesitate.",
    "The way you keep going at IIT. That strength is real.",
]
LOVE_LIST_TITLE = "Three things I love about you"
LOVE_LIST = [
    "Your laugh: [add why]",
    "Your calmness in a crisis: [add why]",
    "[Your own third thing]",
]

NEXT_UP = [
    "A quiet movie night",
    "An unplanned evening walk",
    "Me trying to cook paneer paratha for you (hopefully not burning it)",
    "Booking a cab before dinner this time",
    "Studying together",
]
NEXT_UP_DONE = "That's the whole list. Let's go do them. 💗"

SMILE_MEMORIES = [
    "Samir Hill: 'Yes, let's go!' ...two minutes later... 'No.' 😂",
    "Kanjurmarg: she scolded me AND got the price lowered. Legend.",
    "The cab-less night: no cabs, one last-minute hotel, zero plans.",
    "[Add another funny memory here]",
    "[And one more]",
]

WISHES = [
    ("🌿 Rest", "May you get real rest, the kind that makes the world feel lighter."),
    ("🤍 Being heard", "May you always feel heard, even in the small things."),
    ("🌸 Good people", "May the people around you be kind and easy to be with."),
    ("✨ Small joys", "May each day hold at least one small joy, like chai, sunshine, or a good laugh."),
]

PHOTOS = [f"assets/us{i}.jpg" for i in range(1, 7)]

CLOSING = [
    "Happy birthday, Chhaya. Thank you for being you.",
    "Come back to this page whenever you like.",
]
CLOSING_LINE = "I'm always just a call away. 💗"

# ---------- Password screen ----------
PASSWORD = "15/06/2026"  # day/month/year; "15-6-2026" also works
LOCK_HINT = "Hint: when I first texted you (dd/mm/yyyy)"
HEART_CAPTION = "Touch the heart 💗"
