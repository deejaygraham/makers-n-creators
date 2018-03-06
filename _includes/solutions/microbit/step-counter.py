from microbit import *

steps = 0

while True:

  if accelerometer.was_gesture("shake"):
    steps += 1
    display.show(IMAGE.Happy)
    sleep(100)
    display.clear()
    
  # more accurate
  y = accelerometer.get_y()
  
  if y < 0:
    sleep(100)
    y = accelerometer.get_y()
    
    if y > 0:
      steps += 1
      display.show(IMAGE.Happy)
      sleep(100)
      display.clear()
      
  if button_a.was_pressed():
    display.scroll(to_s(count))
