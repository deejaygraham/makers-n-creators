---
---

# while loops

When you start writing more complicated programs with lots of combinations of input and options for output, while loops are a good way of keeping a program running, giving you the chance to try many options until you are ready to finish.

~~~

name = ''


while name != 'quit':
  name = ask_a_question('what is your name')

  if name == 'Chris':
    print('Hi Chris')

~~~

The loop ends if you type quit instead of a name.
