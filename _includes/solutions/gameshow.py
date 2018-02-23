
from random import *

print('''
Gameshow!
=========

There's a prize behind one of the 3 doors!
Guess the correct door to win the prize!
  _____   _____   _____
 |     | |     | |     |
 | [1] | | [2] | | [3] |
 |   o | |   o | |   o |
 |_____| |_____| |_____|

Choose a door (1, 2 or 3):
''')

winningDoor = randint(1,3)

chosenDoor = input()
chosenDoor = int(chosenDoor)

print("The chosen door is", chosenDoor)
print("The winning door is", winningDoor)

if chosenDoor == winningDoor:
    print("Well done!")
else:
    print("Unlucky, better luck next time!")

