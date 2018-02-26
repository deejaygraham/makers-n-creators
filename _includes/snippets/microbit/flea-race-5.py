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

