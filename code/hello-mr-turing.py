
import random
import time

print('Hello')
time.sleep(2)

# ask a question and store the answer
name = input('what is your name ?')
# pause before answering, a real person would need time to type.
time.sleep(2)

# personalize the greeting
print('Hello ' + name)

# how are they feeling ?
feeling = input('how are you today ?')
time.sleep(2)

if 'good' in feeling:
    print("I'm feeling good too!")
else:
    print("I'm sorry to hear that!")

colour = input('What is your favourite colour? ')
time.sleep(2)

# pick a random favourite colour for us to say
colours = ["Red","Green","Blue", "Yellow"]
my_colour = random.choice(colours)

if colour == my_colour:
  print("We both like " + colour + " :)")
else:  
  print("My favourite colour is " + my_colour)

