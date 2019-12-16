from microbit import *
import radio

beacon_count = 5
beacon_id = 1

# Lowest power transmit
radio.config(power=0) # power is 0 -> 7
radio.on()

while True:
    # decrease beacon_id
    if button_a.was_pressed():
        beacon_id = max(beacon_id - 1, 1)
   # increase beacon_id
    elif button_b.was_pressed():
        beacon_id = min(clue +  1, beacon_id)

    # broadcast the current beacon_id
    else:
        radio.send(str(beacon_id))

    display.show(str(beacon_id))
    sleep(1000)
