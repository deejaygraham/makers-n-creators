---
layout: default
title: Flea Race
platform: microbit
language: python
level: 0
---
## Flea Race 

### Challenge

Racing fleas is a fun pastime. Let's build a game where we can race 5 fleas across the screen with the first flea to reach the right hand edge wins.

### Start

We can represent a flea moving about on the micro:bit screen using a single pixel. Let's create a list of two items that will represent the flea's x and y position on the screen. Remember, the left column is 0 and the right column is number 4.

```python

{% include snippets/microbit/flea-race-1.py %}

```

Now we can race one flea across the screen.


```python

{% include snippets/microbit/flea-race-2.py %}

```

### Randomness

I hope you will agree, that's not very exciting because each time you run the game, the outcome is the same.

What about if we made it different every time? We can use random (and remember to import it at the top) to mix things up a little bit.


```python

{% include snippets/microbit/flea-race-3.py %}

```

We increase the number of opportunities to move from 4 to 10 because we have the random chance where we may not move in 4 turns.

There's a problem with this code, you

```python

{% include snippets/microbit/flea-race-4.py %}

```

Now we have one flea racing with a different outcome every time, we can make preparations to race a lot of fleas.

We can do this by creating a collection of fleas and adding our single flea to it. That way we can write the code to work on the collection and don't have to worry about how many fleas (within reason) we actually create later.

So after we created a single flea, let's create a collection and add the flea to it.


```python

{% include snippets/microbit/flea-race-5.py %}

```

And change the main movement and drawing code to use a collection:

```python

{% include snippets/microbit/flea-race-6.py %}

```

Be careful to keep the sleep in line with the for loop so that the half-second delay is only done once around the loop.

Now that we have things set up, we can add more fleas. Let's given them more descriptive names:

```python

{% include snippets/microbit/flea-race-7.py %}

```

That's the only change we need to have 5 fleas, all racing in their own lane (y coordinate).


### Cheating

```python

{% include snippets/microbit/flea-race-8.py %}

```


### Example Solution

```python

{% include solutions/microbit/flea-race.py %}

```
