from microbit import *
import random

answers = [
    "Without a doubt",
    "Yes, definitely",
    "Most likely",
    "Outlook good",
    "Yes",
    "Signs point to yes",
    "Reply hazy try again",
    "Ask again later",
    "Better not tell you now”,
    "Cannot predict now",
    "Don't count on it”,
    "My reply is no",
    "Very doubtful"
]

while True:
    display.show("8")

    if accelerometer.was_gesture("shake"):
        display.clear()
        sleep(1000)
        display.scroll(random.choice(answers))
