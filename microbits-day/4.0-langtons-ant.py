## 4.0 Langton's Ant

### Challenge

Cellular automata are an interesting set of programs that behave like living
things by following some simple rules. Here, we'll look at implementing
one called [Langton's Ant](https://en.wikipedia.org/wiki/Langton's_ant)


### Start

Langton's ant is a single pixel that draws its way around the screen by following
three simple rules:

* If on a white square, change square to black, turn to left and move forward
* If on a black square, change square to white, turn to right and move forward

Lets start by modelling the ant using x and y coordinates.

```python

from microbit import *

ant = [2, 2] # start in centre


```


### Example Solution

```python

# https://en.wikipedia.org/wiki/Langton's_ant
from microbit import *
import random

def create_new_ant():
    return [random.randint(0, 4), random.randint(0, 4)] # start at a random place on the board

def pick_direction(compass_points):
    return random.choice(compass_points)

# lit pixel -> dark, dark pixel -> lit
def flip_pixel(pixel):
    intensity = display.get_pixel(pixel[0], pixel[1])

    if intensity == 0: intensity = 9
    else: intensity = 0

    display.set_pixel(pixel[0], pixel[1], intensity)

def turn_left(direction, compass_points):
    index = compass_points.index(direction)
    if index == 0:
        index = len(compass_points) - 1
    else:
        index -= 1
    return compass_points[index]

def turn_right(direction, compass_points):
    index = compass_points.index(direction)
    if index == (len(compass_points) -1):
        index = 0
    else:
        index += 1
    return compass_points[index]

def move_forward(ant, heading):
    new_ant = [ant[0] + heading[0], ant[1] + heading[1]]
    return new_ant

def wrap_value_if_required(value):
   if value > 4:
      value = 0
   elif value < 0:
      value = 4
   return value

# Keep the ant on the board. If we go too far one direction,
# wrap the board around and start again on the opposite edge
def wrap_world_edges(ant):
    return [wrap_value_if_required(ant[0]), wrap_value_if_required(ant[1])]

ant = create_new_ant()

north = [1, 0]
east = [0, 1]
south = [-1, 0]
west = [0, -1]

compass_points = [ north, east, south, west ]
direction = pick_direction(compass_points) # start off pointing in a random direction

while True:
    square = display.get_pixel(ant[0], ant[1])

    if square == 0:
        direction = turn_left(direction, compass_points)
    else:
        direction = turn_right(direction, compass_points)

    flip_pixel(ant)
    ant = move_forward(ant, direction)
    ant = wrap_world_edges(ant)
    sleep(500)


```
