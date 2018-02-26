from microbit import *
import random

# add a speed field for each flear ?
alice = [0, 0, 1]
bob = [0, 1, 2]
carol = [0, 2, 3]
dave = [0, 3, 4]
eleanor = [0, 4, 5]

turtles = [alice, bob, carol, dave, eleanor]

# line up at start
for turtle in turtles:
    display.set_pixel(turtle[0], turtle[1], 9)


# race !
for x in range(1, 10):
    for turtle in turtles:
        # will this turtle move this turn?
       if random.randint(0, turtle[2]) == 1:
            display.set_pixel(turtle[0], turtle[1], 0)
            turtle[0] += 1
            turtle[0] = min(turtle[0], 4)
            display.set_pixel(turtle[0], turtle[1], 9)

    sleep(500)        

