from microbit import *
import radio

radio.on()

while True:

    radio.send('ping')
    sleep(500)
