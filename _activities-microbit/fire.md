---
layout: default
title: Fire Simulator
platform: microbit
language: python
level: 4
---
## Fire Simulator

### Challenge

Experiment with the Image class, create a blank image then build a simulated fire by
creating a layer of pixels of random light intensity along the bottom of the screen. To simulate
the flames moving upwards, shift the image up the screen as time passes, making room
for new random layers at the bottom of the screen. As the image moves up the screen,
it should fade out (intensity -> 0).

Used with thanks from: http://blog.withcode.uk/2016/06/microbit-python-tutorial-shake-n-burn-fire-simulator/

### Extensions

Eventually the fire will "burn out" as the intensity decreases gradually. Use the accelerometer to wake the fire up by shaking the microbit.


### Example Solution

<button onclick="show_hide_solution()">Show Solution</button>

```python

{% include solutions/microbit/fire.py %}

```
