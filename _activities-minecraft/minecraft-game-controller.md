---
layout: default
title: Minecraft Game Controller
platform: minecraft-pi
language: python
level: 4
---
## Minecraft Game Controller

### Challenge

We've seen how awesome the microbit is and how to run python scripts on the pi to control Minecraft. What about
if we could connect the two together and have the microbit send commands to Minecraft?


### Printing

All the examples we have seen so far have been putting information on the microbit's "screen" (the 5x5 LED matrix). We have
to use display.show() or display.scroll() to show text. In some of the earlier examples on the laptops, we used
python's print function. Could we use the print function on the microbit? Where would the text go?

The print function is actually wired up to the USB serial port so

```python

print('hello world')

```

...is sent to whatever is connected to the other end of the USB cable (if it can read it).


#### Microbit

On the microbit we can write some code to check position of the accelerometer and if any buttons have been pressed. Then we
can use the print function to send that data to the USB port.

```python

{% include solutions/microbit/minecraft-game-controller.py %}

```

### Communication

To get the Pi and the microbit to talk together they both need to share the same settings
and know about each other. When we plug them together with a USB cable, the Pi
will assign a name to the microbit that might not be obvious (it doesn't really know it's
a microbit). We need to do some investigation to work out what the Pi calls the microbit
when it's plugged in.


### Raspberry Pi

First, you will need to install pySerial using:


```console

sudo apt-get install python-serial

```

or by downloading from [here](https://pypi.python.org/pypi/pyserial). With nothing connected to the Pi, open a
terminal window and run this command:


```console

ls /dev/ttyA*

```

and make a note of all the results (if any). Next connect the microbit to the Pi by the USB cable and
run the command again and look for something like dev/ttyACM1:


```console

ls /dev/ttyA*

dev/ttyACM1


```

or run the command:


```console

dmesg

171769.685287] cdc_acm 1-1.2:1.1: ttyACM0: USB ACM device

```

Once we know what these details we can change the code to make sure we are using the right name. We need to write code to run
on both sides - the Pi and the microbit - to communicate correctly.


### Example Solution

#### Pi

On the raspberry pi, this is the code that will read the data from the USB port and decode it.

```python

{% include solutions/minecraft-pi/minecraft-game-controller.py %}

```

### Extensions

* Print the values read from the microbit and work out how moving the microbit changes the data.
* Move the player according to how much you tip the controller forward or back.
* Move the player left or right depending on the movement of the controller.
* How could you use the a or b button presses in the game?
