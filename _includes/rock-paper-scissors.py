from random import randint

player = input('Pick from rock (r), paper (p) or scissors (s)?')

if player == 'r':
  print('O')
elif player == 'p':
  print('___')
elif player == 's':
  print('>8')
else:
  print('??')

print('vs')

computer = randint(1,3)

if computer == 1:
  computer = 'r'
  print('O')
elif computer == 2:
  computer = 'p'
  print('___')
else:
  computer = 's'
  print('>8')

if player == computer:
  print('DRAW!')
elif player == 'r' and computer == 's':
  print('Player wins!')
elif player == 'r' and computer == 'p':
  print('Computer wins!')
elif player == 'p' and computer == 'r':
  print('Player wins!')
elif player == 'p' and computer == 's':
  print('Computer wins!')
elif player == 's' and computer == 'p':
  print('Player wins!')
elif player == "s" and computer == 'r':
  print('Computer wins!')
else:
  print('Huh?')

