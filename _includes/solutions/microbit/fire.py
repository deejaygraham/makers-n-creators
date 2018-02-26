from microbit import *
import random

fire = Image("00000:" * 5) # create an empty image

intensity = 0.5 # start with the fire at medium intensity

while True:
    display.show(fire)
    sleep(100)

    # shake to stoke the fire
    if accelerometer.was_gesture("shake"):
        intensity = 1

    # shift the image up and fade it slightly
    fire = fire.shift_up(1) * intensity

    # let the fire burn down a little (reduce the intensity)
    intensity = intensity * 0.98

    # choose random brightness for bottom row of fire
    for x in range(5):
        fire.set_pixel(x, 4, random.randint(0,9))
