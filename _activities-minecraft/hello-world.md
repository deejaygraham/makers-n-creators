---
layout: default
title: Hello World
platform: minecraft-pi
language: python
level: 1
---
## Hello world

In order to be considered professional python programmers on the Raspberry Pi, we have to
do the time-honored hello world in Minecraft.

Start up an instance of Pi Minecraft and a terminal window. Write a program to send a
hello world message to the minecraft console.


### Extensions

* Change the code to read in a message from the console
* Ask for the player's name and write that out in the message.
* Use a while loop to keep writing messages to the chat window.

Inspired by https://arghbox.files.wordpress.com/


### Example Solution

```python

{% include solutions/minecraft-pi/hello-world.py %}

```

### Read message from console

```python

message = raw_input("enter a message") # or input in Python 3.x

```
