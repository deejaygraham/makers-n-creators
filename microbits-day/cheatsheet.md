# BBC micro:bit Cheatsheet


## Import 

Always, always, always:

from microbic import *


## Display

### Text 

display.scroll(‘hello there!’)


### Image

display.show(Image.HAPPY)

diagonal = Image(“90000:09000:00900:00090:00009”) # 0 off, 1..9
display.show(diagonal)


### Read Pixel

brightness = display,get_pixel(x, y)


### Change Pixel

display.set_pixel(x, y, brightness)


### Clear Display 

display.clear()


## Pausing

sleep(500)    # half a second
sleep(2000)   # two seconds


## Buttons

if button_a.was_pressed(): # also button_b
	message = “You pressed button A”



## Accelerometer

x_tilt = accelerometer.get_x()
y_tilt = accelerometer.get_y()
height_off_ground = accelerometer.get_z()


### Gestures

if accelerometer.was_gesture(“shake"):
	message = “Shaking”


## Touch Inputs

if pin0.is_touched():  # also pin1 and pin2
	message = “You touched pin 0”


## Sound 

### Music

import music

music.play(music.DADADADUM)

tune = ["C4:4", "D4:4", "R:4", "C4:4"]
music.play(tune)


### Speech

import speech

speech.say("Hello, World”)


## Radio


radio.on()

radio.send(‘shake') # Send a message to others
        
message = radio.receive() # Read any incoming messages.
