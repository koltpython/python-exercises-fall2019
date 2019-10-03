from random import randint

print('Hi Bool, ready to play rock-paper-scissors')
#create a list of play options
t = ["Rock", "Paper", "Scissors"]

#assign a random play to the computer
cool = t[randint(0,2)]
player = input("Rock, Paper, Scissors?")

# the boolean to hold player's winning stats
win = False
tie = False

# implement the rock-paper-scissors game here
tie = cool == player
if (cool == 'Rock'):
  win = (player == 'Paper')
elif (cool == 'Paper'):
  win = (player == 'Scissors')
else:
  win = (player == 'Rock')

if (tie):
  print('Tie!')
elif (win):
  print(f'Bool wins, Cool said {cool}')
else:
  print(f'Bool loses, Cool said {cool}')
