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
