---
layout: default
title: Creeper
platform: minecraft-pi
language: python
level: 3
---
## Creeper

### Challenge

In honour of Halloween, we will create a spooky block that follows us around.
Once you have the code working, you can build on the basic spooky block and make it
into a minecraft creeper, a weeping angel from Dr Who or a ghost.

Write a program to create a block a little bit away from your player's current
position. Each time you move, have the spooky block move a little bit closer to
where you are.

Hint: Easiest way follow is to change remove the block at the current position by
changing it to "air" and rebuild the block at the new location.

### Extensions

* Add more blocks to make a recognizable spooky figure to follow you around.
* Remember to erase the old blocks before building the figure with the new blocks

### Example Solution

```python

{% include solutions/minecraft-pi/creeper.py %}

```
