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
