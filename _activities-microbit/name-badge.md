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

Next week can add an introduction and our name. Substitute your own name in the code. Be careful to keep all display.scrolls in line with each other and all still indented under the while.

~~~python

{% include snippets/microbit/name-badge-3.py %}

~~~

If we wanted to make this a bit easier to change the name we can add an extra line near the top to remember the name.

~~~python

{% include snippets/microbit/name-badge-4.py %}

~~~

In fact, that makes the code look a bit easier to read so we should bring the greeting and the introduction out into variables as well.


### Example Solution

~~~python

{% include solutions/microbit/name-badge.py %} 

~~~
