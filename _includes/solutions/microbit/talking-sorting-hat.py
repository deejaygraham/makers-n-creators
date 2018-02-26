from microbit import *
import speech

# using default speech settings
speech.say("I am the sorting hat")
# set individual speech qualities - values 0 to 255
speech.say("I am the sorting hat", speed=82, pitch=72, throat=110, mouth=105)
