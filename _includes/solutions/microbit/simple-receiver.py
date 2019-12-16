from microbit import *
import radio

radio.on()

while True:
    display.show("?")

    message = radio.receive_full()

    if message:
        beacon_id, signal_strength, timestamp = message
        display.scroll(beacon_id)
        display.scroll(str(signal_strength))
        
    sleep(200)
