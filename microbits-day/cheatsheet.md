# BBC micro:bit Cheatsheet


## Import 

Always, always, always:

```python

from microbic import *

```

## Display

### Text 

```python

display.scroll(‘hello there!’)

```

### Image

```python

display.show(Image.HAPPY)

```

```python

diagonal = Image(
		“90000:"
		"09000:"
		"00900:"
		"00090:"
		"00009”
		) # 0 off, 1..9
		
display.show(diagonal)

```

### Read Pixel

```python

brightness = display,get_pixel(x, y)

```

### Change Pixel

```python

display.set_pixel(x, y, brightness)

```

### Clear Display 

```python

display.clear()

```

## Pausing

```python

sleep(500)    # half a second
sleep(2000)   # two seconds

```

## Buttons

```python

if button_a.was_pressed(): # also button_b
	message = “You pressed button A”

```

## Accelerometer

```python

x_tilt = accelerometer.get_x()
y_tilt = accelerometer.get_y()
height_off_ground = accelerometer.get_z()

```

### Gestures

```python

if accelerometer.was_gesture(“shake"):
	message = “Shaking”

```

## Touch Inputs

```python

if pin0.is_touched():  # also pin1 and pin2
	message = “You touched pin 0”

```

## Sound 

### Music

```python

import music

music.play(music.DADADADUM)

tune = ["C4:4", "D4:4", "R:4", "C4:4"]
music.play(tune)

```

### Speech

```python

import speech

speech.say("Hello, World”)

```

## Radio

```python

radio.on()

radio.send(‘shake') # Send a message to others
        
message = radio.receive() # Read any incoming messages.

```
