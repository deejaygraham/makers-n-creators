from microbit import *
import radio

radio.on()

while True:
    display.show("?")

    message = radio.receive_full()

    if message:
        beacon_id, signal_strength, timestamp = message
        display.scroll(beacon_id)
        percent_strength = ((signal_strength + 255)* 100) / 255
        display.scroll(str(percent_strength))

    sleep(200)
