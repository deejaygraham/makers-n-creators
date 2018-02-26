---
layout: default
title: Boom-box/Mbira
platform: microbit
language: python
level: 2
---

## Boom Box

### Challenge
In this exercise, we are going to bring inputs and outputs together to make a musical instrument. Microbit
can play music using the music.play function and can get input from buttons or from the touch inputs on the
edge connector. Wire a speaker or a pair of headphones between pin 0 and and on the edge of the microbit
before running.

### Requirements

* Crocodile clips and a speaker or headphones to play the music through.


### Notes

* play - music.play accepts a list of musical note and duration pairs, use “R” to rest between notes.
* buttons - the microbit has two buttons, a and b, was_pressed can be used to ask if a button has been pressed since the microbit started or the last time you asked.
* pins - the pins 0, 1 and 2 are touch enabled so that the microbit can tell if you touch one of them while touching the gnd pin with your other hand. We are using pin 0 for the loudspeaker output so we only have pins 1 and 2 available for input.


### Extensions

* Change which notes are played
* Play more notes each time a pin is touched.
* Play random notes each time a pin is touched
* Play a random tune using music.play and one of the pre-prepared items like music.NYAN


### Example Solution

```python

{% include solutions/microbit/boom-box-or-mbira.py %}

```
