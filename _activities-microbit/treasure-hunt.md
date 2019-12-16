---
layout: default
title: Treasure Hunt
platform: microbit
language: python
level: 4
---
## Treasure Hunt

### Challenge

This game uses several microbits to create a treasure hunt game. Create a number of clues to the treasure
and put them in the all_clues list. Program all but one of the microbits with the beacon code and set
each one to a different number. Program the final microbit with the receiver code.

You might find that the transmitter beacons have their radio power set too high so that it's too easy to find them. You can make it the hunt harder by reducing the power (see the example solution).

### Requirements

* Lots of microbits.


### Extensions

* Change the receiver to remind you about the last clue
* Draw a starting image
* Draw an image to show when the beacon is broadcasting.
* Change the code to make a Pokemon Go collecting game. Instead of clues, beacons can broadcast an image of a Pokemon and the hunter has to collect them all. Hint: this could be a mash-up of the treasure hunt and the Snapchat examples.

Adjust the power from each beacon to make it more challenging.
If you are playing with more than one group in an area, consider changing the radio channel so
the groups don't interfere with each other.


### Example Solution

#### Beacon

<button id="show" onclick="show_hide_solution()">Show Solution</button>

```python

{% include solutions/microbit/treasure-hunt-beacon.py %}

```

#### Receiver

```python

{% include solutions/microbit/treasure-hunt-receiver.py %}

```
