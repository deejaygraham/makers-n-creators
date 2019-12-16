from microbit import *
import radio

beacon_id = 1

# Lowest power transmit
radio.config(power=0) 
radio.on()

while True:

    radio.send(str(beacon_id))
    display.show(str(beacon_id))

    sleep(1000)
