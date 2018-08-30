---
layout: default
title: Name Badge
platform: microbit
language: python
level: 1
---
## Name Badge

### Challenge

We all have a sticky paper name badge which feels a little bit old fashioned. What we should make is a programmable 
name badge that can show a greeting of your choice.

### Start

First we need to make sure we have access to all the microbit goodness from python. We do that with having an import statement 
at the top of the file. Next we can scroll some text across our badge.

~~~python

{% include snippets/microbit/name-badge-1.py %}

~~~

Notice that it only displays once. To get it to display repeatedly we can use a while loop. Take care that the while has no spaces before it and that true is actual True (with a capital T) and, that there is a colon after the True. This is how python distinguishes the while bit from the chunk of code belonging to the while. On the next line, the display.scroll now has to be indented to make sure that python recognizes that it belongs to the while. 

~~~python

{% include snippets/microbit/name-badge-2.py %}

~~~

Next we can add an introduction and our name. Substitute your own name in the code. Be careful to keep all display.scrolls in line with each other and all still indented under the while.

~~~python

{% include snippets/microbit/name-badge-3.py %}

~~~

Now, how about showing how you are feeling today with a picture? Use display.show() with one of these images - Image.HAPPY, 
Image.HEART, Image.SAD, Image.ASLEEP, Image.SURPRISED, Image.CONFUSED

~~~python

{% include snippets/microbit/name-badge-5.py %}

~~~




