---
layout: default
title: Frozen
platform: minecraft-pi
language: python
level: 2
---
## Frozen

In the Raspberry Pi version of Minecraft we can ask for the player's current position
in the world and find out what kind of block they are standing on. Then we can automate
changing the blocks in the world depending on where the player moves.

Write a program to change any blocks of water that the player stands on into ice. Make sure
you only change water to ice, not every block.



### Extensions

* Change the code to change whatever you walk on to a different block type (e.g. lava is block id 10).
* Change every block except air (id 0) to ice.
* Change the code to change blocks you touch to gold.


### Example Solution

```python

{% include solutions/minecraft-pi/frozen.py %}

```
