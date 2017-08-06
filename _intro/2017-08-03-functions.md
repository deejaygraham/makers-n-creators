---
---

# functions

We can also pass a value back from a function.

~~~

def ask_a_question(question):
  reply = input(question + ' ?')
  return reply

name = ask_a_question('what is your name')
age = ask_a_question('how old are you')

~~~

Notice message value changes each time and reply changes.
