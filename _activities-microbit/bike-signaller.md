---
title: Bike Signaller
platform: microbit
language: python 
level: 4
---
### Challenge

Bicycles usually have to have lights front and back so that they can be seen by cars when it's dark. What about if you bike could be more like a car and signal left and right and braking?

Write two programs and flash a copy of each one onto two microbits - one at the front of the bike on the handlebars and the other at the back where the rear light sits.

The first program must wait for either of the buttons to be pushed or both of them pushed at the same time. If you push button a, send a radio signal to the other microbit to show a left turn. If you push the button b, send a radio signal to show a right turn. If you push both buttons together, send a signal that you are braking.

The second program must loop waiting for input from the first microbit. If it receives a turn signal (left or right) display a left or right arrow. If it receives a brake (stop) signal light up the full display with a red block like a car brake light.


### Extensions

To put this onto a real bike, we would have to use some wiring so the microbit could get a signal when you press the brakes or when you turn press a button on the handle bars when you want to signal left or right. Maybe a project for another event?


### Example Solution

#### Handlebar Microbit

```python

from microbit import *
import radio

radio.on()

while True:

  # read left, right and stop inputs
  # send the command over the radio...
  # reading the buttons clears the history so read both only once
  left_button = button_a.was_pressed()
  right_button = button_b.was_pressed()

  if left_button and right_button:
    radio.send('stop')
  elif left_button:
    radio.send('left')
  elif right_button:
    radio.send('right')

  sleep(100)

```

#### Rear Microbit

```python

from microbit import *
import radio

radio.on()

# stop image - all leds turned on
stop = Image("99999:99999:99999:99999:99999")

while True:

  display.clear()

  # Read any incoming messages.
  message = radio.receive()

  if message:
      if message == 'left':
        display.show(Image.LEFTARROW)
      elif message == 'right':
        display.show(Image.RIGHTARROW)
      elif message == 'stop'
         display.show(stop)

  sleep(100)

```
