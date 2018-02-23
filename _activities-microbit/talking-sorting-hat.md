---
title: Talking Sorting Hat
platform: microbit
language: python 
level: 3
---
In the Harry Potter films, the actor Leslie Phillips voiced the sorting hat. Modify the
sorting hat code to speak aloud what it’s thinking before announcing to the student instead of writing
scrolling text on the screen. Most text should translate immediately but you may need to investigate
phonemes to pronounce the Hogwarts houses correctly.

### Requirements

* Crocodile clips and a speaker or headphones to play the music through.


### Extensions

* Change the voice of the sorting hat
* Use the sing function to make the sorting hat sing a song
* Use the pronounce function to better control the pronunciation of the words.

Refer to the speech API for details: https://microbit-micropython.readthedocs.io/en/latest/speech.html


### Example Solution

```python

from microbit import *
import speech

# using default speech settings
speech.say("I am the sorting hat")
# set individual speech qualities - values 0 to 255
speech.say("I am the sorting hat", speed=82, pitch=72, throat=110, mouth=105)

```
