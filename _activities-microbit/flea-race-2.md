---
layout: default
title: Flea Race
platform: microbit
language: python
level: 3
---

## Flea Race (2)

### Challenge

Racing fleas is a fun pastime. Let's build a game where we can race 5 fleas across the screen and the first flea to reach the right hand edge wins.

### Start

We can show a flea moving about on the microbit screen using a single pixel. Let's create a list of two items that will represent the flea's x and y position on the screen. Remember, the left column is 0 and the right column is number 4.

```python

from microbit import *

flea = [0, 0] # start top left


```

Now we can move our one flea across the screen.


```python

from microbit import *

flea = [0, 0] # x, y

display.set_pixel(flea[0], flea[1], 9)

for x in range(1, 4):
    # turn off current pixel
    display.set_pixel(turtle[0], turtle[1], 0)
    # move
    flea[0] += 1
    display.set_pixel(flea[0], flea[1], 9)
    # wait so we don't move too fast
    sleep(500)        

```

### Randomness

I hope you will agree, that's not very exciting. Each time you run the game, the outcome is the same.

How about if we made the flea behave differently every time? We can use random (and remember to import it at the top) to mix things up a little bit.


```python

from microbit import *
import random

flea = [0, 0]

display.set_pixel(flea[0], flea[1], 9)

for x in range(1, 10):
    # 50 % chance
    if random.randint(0, 1) == 1:
        display.set_pixel(flea[0], flea[1], 0)
        flea[0] += 1
        display.set_pixel(flea[0], flea[1], 9)

    sleep(500)        

```

The random.randint function returns a random value between the two values given (0 and 1 in this case) each time it is called in the for loop and we use that value to see if we have been given a 1 value. If so, we can move the flea forward a little bit. Each flea has about the same opportunity to move, a 50% chance because there are only two values possible from randint in this code.

We need to increase the number of opportunities to move from 4 to 10 in the for loop because we now have a random chance so we may not move all the way across the screen in 4 turns.

There's a problem with this code, though. Can you find it?

### Moving too far

In between moving the flea and actually drawing on the screen, we can make sure we don't go beyond the fourth column by using the min function.

```python

        flea[0] += 1
        flea[0] = min(flea[0], 4)
        display.set_pixel(flea[0], flea[1], 9)

```

Now we have one flea moving with a different outcome every time, we can make preparations to race some fleas.

We do this by creating a collection of fleas and adding our single flea to it. That way, we can write the code to work on the collection and don't have to worry about how many fleas (within reason) we actually race later on.

So after we created a single flea, let's create a collection and add the flea to it.

```python

from microbit import *
import random

flea = [0, 0]
all_fleas = [ flea ]

```

Then we can expand our initial code to draw the fleas at their starting points.

```python

# display.set_pixel(flea[0], flea[1], 9)
for f in all_fleas:
  display.set_pixel(f[0], f[1], 9)

```

And change the main movement and drawing code to use a collection:

```python

# race !
for x in range(1, 10):
    for f in all_fleas:
      # 50 % chance
      if random.randint(0, 1) == 1:
          display.set_pixel(f[0], f[1], 0)
          f[0] += 1
          f[0] = min(f[0], 4)
          display.set_pixel(f[0], f[1], 9)

    sleep(500)        

```

Be careful to keep the sleep in line with the for loop so that the half-second delay is only done once around the loop.


### Race time !

Now that we have things set up, we can add more fleas. Let's given each one a more interesting name:

```python

alice = [0, 0]
bob = [0, 1]
carol = [0, 2]
dave = [0, 3]
eleanor = [0, 4]

all_fleas = [ alice, bob, carol, dave, eleanor ]

```

That's the only change we need to have 5 fleas, each one racing in its own lane (or row - the y coordinate) across the screen.


### Cheating

So that's a nice racing game which should have a different result each time. Each flea has a 50% chance or moving each time around the for loop, with random giving everyone an equal chance of winning, on average.

But what if we wanted to be a bit sneaky and cheat at the race? Could we make sure that one or two fleas would have a better chance than the others?

The critical piece of code is the call to random.randint that always has the same chance for each flea. If we manipulated the range of values available we could change the odds for each competitor. A flea which had a 1 in 4 (25%) chance of advancing would probably not win against a flea which had a 1 in 2 (50%) chance of advancing.

We can use the flea object to store a chance value as well as the x and y coordinates.


```python

alice = [0, 0, 1] # x, y, chance
bob = [0, 1, 2]
carol = [0, 2, 3]
dave = [0, 3, 1]
eleanor = [0, 4, 10]

```

Now we can change the random code to use the new chance value:

```python

    if random.randint(0, f[2]) == 1:
      display.set_pixel(f[0], f[1], 0)
      f[0] += 1
      f[0] = min(f[0], 4)
      display.set_pixel(f[0], f[1], 9)

```

If you run the code again, you should see that alice and dave have the best chance of winning while poor eleanor has the worst (but not impossible) chance of winning with only 1 chance in 10 of moving for each turn.


### Example Solution

```python

from microbit import *
import random

alice = [0, 0, 1]
bob = [0, 1, 2]
carol = [0, 2, 3]
dave = [0, 3, 1]
eleanor = [0, 4, 10]

all_fleas = [ alice, bob, carol, dave, eleanor ]

# line up at start
for f in fleas:
    display.set_pixel(f[0], f[1], 9)

# race !
for x in range(1, 10):
    for f in all_fleas:
        # will this flea move this turn?
       if random.randint(0, f[2]) == 1:
            display.set_pixel(f[0], f[1], 0)
            turtle[0] += 1
            turtle[0] = min(f[0], 4)
            display.set_pixel(f[0], f[1], 9)

    sleep(500)        

```
