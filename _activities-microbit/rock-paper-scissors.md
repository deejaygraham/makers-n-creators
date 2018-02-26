---
layout: default
title: Rock Paper Scissors
platform: microbit
language: python
level: 1
---
In this game, we’ll learn one way to implement the Rock Paper Scissors game for the micro:bit. We’ll
draw images for each of the objects, react to a gesture from the play then use the python random
function to pick one of the objects. In this version the micro:bits are not aware of each other’s
selection so it is up to the players to decide who wins.


### Notes

* gestures - gesture names are shortcuts for groups of movements that the microbit recognises without the need to individually record and identify complex 3-d changes.
* random - random.choice picks one item from a list and returns it at “random”. Random is never really random for most computers.
* image - Images are strings of text, separated by colons to split them into rows, and represent the brightness of each LED in the 5x5 matrix. 0 is off, 9 is fully on.


### Extensions

* Make the images better
* Extend the game to play Rock, Paper, Scissors, Lizard, Spock


### Example Solution

```python

{% include solutions/microbit/rock-paper-scissors.py %}

```
