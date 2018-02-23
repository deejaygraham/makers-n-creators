import random

secret_code = ['a', 'b', 'c']
# ascii art from http://www.ascii-art.de/ascii/s/starwars.txt
death_star_plans = '''

      .          .
.          .                  .          .              .
  +.           _____  .        .        + .                    .
.        .   ,-~"     "~-.                                +
         ,^ ___         ^. +                  .    .       .
        / .^   ^.         \\
       Y  l  o  !          Y
.       l_ `.___.'        _,[
       |^~"-----------""~ ^|       +
+       . !                   !     .
    .   \                 /
         ^.             .^            .      "       +.
           "-.._____.,-" .                    .
    +           .                .   +                       .
+          .             +                                  .
    .             .      .



'''

innocent_responses = [
                'beep, boop',
                'I am a robot',
                'How may I help you?',
                'I am not the droid you are looking for',
                'Mr Asimov? Is that you?'
                ]

entered_sequence = []

while True:

  choice = input('Letter ?').lower()
  entered_sequence.append(choice)

  if len(entered_sequence) < len(secret_code):
    # they are still entering values
    pass
  elif len(entered_sequence) == len(secret_code):
    # Empire does not know the password
    matching_sequence = True

    # look for anything that doesn't match ?
    for i in range(len(secret_code)):
      if entered_sequence[i] != secret_code[i]:
          # no match - lock the plans again!
          matching_sequence = False
          break

    if not matching_sequence:
      print(random.choice(innocent_responses))
      # reset input so they can try again.
      entered_sequence = []
    else:
      print('Help me Obi-Wan, you are my only hope!')
      print(death_star_plans)
      break
