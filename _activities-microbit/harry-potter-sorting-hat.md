---
layout: default
title: The Harry Potter Sorting Hat
platform: microbit
language: python
level: 2
---
## Harry Potter Sorting Hat 

### Challenge

From the Harry Potter films, the Hogwarts Sorting Hat. Concentrate hard on the house you want to be
sorted into, shake the microbit, then read the hat’s decision. Uses the display.show function to
show customised images.


### Notes

* gestures - gesture names are shortcuts for groups of movements that the microbit recognises without the need to individually record and identify complex 3-d changes.
* random - random.choice picks one item from a list and returns it at “random”. Random is never really random for most computers.
* scroll - the microbit only has room to display one letter at a time (which is why some letters are upper case and others are lower case) display.scroll displays a long string of text letter by letter.
* image - Images are strings of text, separated by colons to split them into rows, and represent the brightness of each LED in the 5x5 matrix. 0 is off, 9 is fully on.


### Example Solution

<button onclick="show_hide_solution()">Show Solution</button>

```python

{% include solutions/microbit/harry-potter-sorting-hat.py %}

```
