---
layout: default
title: Magic 8 Ball
platform: microbit
language: python
level: 1
---
Re-create the prediction toy using the microbit’s gesture recognition function. Ask the microbit a question, shake it and read the answer


### Notes

* gestures - gesture names are shortcuts for groups of movements that the microbit recognises without the need to individually record and identify complex 3-d changes.
* random - random.choice picks one item from a list and returns it at “random”. Random is never really random for most computers.
* scroll - the microbit only has room to display one letter at a time (which is why some letters are upper case and others are lower case) display.scroll displays a long string of text letter by letter.


### Extensions

* Add more answers to the list (be careful about quotes and commas) or change the current list


### Example Solution

```python

{% include solutions/microbit/magic-8-ball.py %}

```
