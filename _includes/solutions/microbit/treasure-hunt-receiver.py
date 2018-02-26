# Read clues by finding (being near to) each beacon in turn, 1 upwards until you
# have found the full set.

from microbit import *
import radio

# starting clue
clue = "hint: Walk around to find the first clue"
display.scroll(clue)
next_clue = 1

radio.on()

while True:
    display.show("?")

    # are we near any clue beacons?
    message = radio.receive()

    if message:
        # picked up a clue !
        number, text = message.split(":")
        # is it the one we want?
        if int(number) == next_clue:
            clue = "clue " + str(number) + ":" + text
            next_clue += 1
            display.scroll(clue)

    sleep(100)
