---
layout: default
title: Storm Distance Calculator
platform: microbit
language: python
level: 2
---
## Storm Distance Calculator

### Challenge

During a thunderstorm, measuring the time between a lightning flash and the sound of thunder tells
you roughly how far away the storm is. Here we will write a program to wait for lightning, then wait for
thunder and then calculate an approximate distance to the storm.


### Notes

* functions - the def keyword at the top of the file starts a function definition, a way of packing a piece of code that can be re-used in several places.
* buttons - the microbit has two buttons, a and b, was_pressed can be used to ask if a button has been pressed since the microbit started or the last time you asked.
* image - Images are strings of text, separated by colons to split them into rows, and represent the brightness of each LED in the 5x5 matrix. 0 is off, 9 is fully on.


### Extensions

* We calculate the distance in metres. Can we make the display better if it’s more than 1km away?


### Example Solution

<button id="show" onclick="show_hide_solution()">Show Solution</button>

```python

{% include solutions/microbit/storm-distance-calculator.py %}

```
