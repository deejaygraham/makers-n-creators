from microbit import *
import radio
import random

# name image pairs
emotions = [
    ['happy',       Image.HAPPY],
    ['sleepy',      Image.ASLEEP],
    ['sad',         Image.SAD],
    ['surprised',   Image.SURPRISED],
    ['confused',    Image.CONFUSED],
    ['meh',         Image.MEH],
    ['duck',        Image.DUCK]
]

emotion_count = len(emotions)
current_emotion = 0

radio.on()

while True:
    display.show(emotions[current_emotion][1])

    # select an emotion
    if button_a.was_pressed():
        current_emotion += 1
        if current_emotion >= emotion_count:
            current_emotion = 0
    # send that emotion
    elif button_b.was_pressed():
        radio.send(emotions[current_emotion][0])

    # Read any incoming messages.
    message = radio.receive()

    find_emotion = 0
    for emotion in emotions:
        if message == emotion[0]:
            current_emotion = find_emotion
            sleep(100)
        find_emotion += 1
