---
layout: default
title: Build a House
platform: minecraft-pi
language: python
level: 3
---
## 2.3 Building a House

In this challenge we will build a simple, single story house with a flat roof. We could
build a house with a loop to place every block but a nice easy way to do it is to use
the setBlocks function to quickly build a solid cube shape of one block type.
This way we can create a solid block then hollow out the insides using the same method
but using an air block to give a living area.


### Extensions

* Change the depth, width and height of the house.
* Change the code to use a different block type.
* Add a door so that the player can go in and out.
* Build the house around the player using their current position.
* Add a pitched roof /\ onto the house using a different block type.
* Add a chimney on the roof.
* Use a house function and a loop to build a whole town.

### Example Solution

Super simple edition

```python

{% include solutions/minecraft-pi/house-easy.py %}

```

Using a house function

```python

{% include solutions/minecraft-pi/house-function.py %}


```
