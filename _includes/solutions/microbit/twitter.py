from microbit import *
import radio

radio.on()

your_tweet = 'hi'

while True:
    if button_a.was_pressed():
	   radio.send(your_tweet)

    received_tweet = radio.receive()

    if received_tweet:
        display.scroll(received_tweet)

    sleep(100)