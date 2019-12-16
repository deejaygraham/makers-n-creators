---
layout: default
title: Theremin
platform: microbit
language: python
level: 2
---
## Theremin

### Challenge

In this exercise, we are recreating an electronic musical instrument from the 1920s. We will play a
musical note which changes based on how we move the microbit around in space. Wire a speaker or a
pair of headphones between pin 0 and the GND pin on the edge of the microbit before running.


### Requirements

* Crocodile clips and a speaker or headphones to play the music through.


### Notes

* pitch - music.pitch plays a note at a given frequency. A above middle C is 4400Hz.
* accelerometer - the microbit has an accelerometer like you will find in a modern smartphone that enables it to know which way round it is in space - upside down, tipped forward or back and how high above the ground it is.


### Extensions

* Change the starting note
* Play only notes from a scale.
* Change the scaling calculation to change the range of the notes it can play.


### Example Solution

<button id="show" onclick="show_hide_solution()">Show Solution</button>

```python

{% include solutions/microbit/theremin.py %}

```
