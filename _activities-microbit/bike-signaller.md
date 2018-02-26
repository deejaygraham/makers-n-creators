---
layout: default
title: Bike Signaller
platform: microbit
language: python
level: 4
---
## Bike Signaller

### Challenge

Bicycles usually have to have lights front and back so that they can be seen by cars when it's dark. What about if you bike could be more like a car and signal left and right and braking?

Write two programs and flash a copy of each one onto two microbits - one at the front of the bike on the handlebars and the other at the back where the rear light sits.

The first program must wait for either of the buttons to be pushed or both of them pushed at the same time. If you push button a, send a radio signal to the other microbit to show a left turn. If you push the button b, send a radio signal to show a right turn. If you push both buttons together, send a signal that you are braking.

The second program must loop waiting for input from the first microbit. If it receives a turn signal (left or right) display a left or right arrow. If it receives a brake (stop) signal light up the full display with a red block like a car brake light.


### Extensions

To put this onto a real bike, we would have to use some wiring so the microbit could get a signal when you press the brakes or when you turn press a button on the handle bars when you want to signal left or right. Maybe a project for another event?


### Example Solution

#### Handlebar Microbit

```python

{% include solutions/microbit/bike-signaller-handlebars.py %}

```

#### Rear Microbit

```python

{% include solutions/microbit/bike-signaller-rear.py %}

```
