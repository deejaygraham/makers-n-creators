from microbit import *
import random

rock     = Image("00000:09990:90009:92229:29992")
paper    = Image("99950:90992:90092:90092:99992")
scissors = Image("90009:09090:00900:55055:55055")
rock_paper_scissors = [ rock, paper, scissors ]

display.show(rock_paper_scissors, delay = 500)

display.clear()

while True:

  if accelerometer.was_gesture("shake"):   
	  one_of_them = random.choice(rock_paper_scissors)
		display.show(one_of_them)
		sleep (3000)
    display.clear()
