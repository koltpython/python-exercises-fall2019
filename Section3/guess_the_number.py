from random import randint

target = randint(1,100)

#Your code starts here
lives = 6
guess = ''

while lives >= 0 and guess != target:
  guess = int(input('Your guess: '))
  
  if guess == target:
    print('Congrats!')
  else:
    if guess < target:
      print('Your guess is less than the number')
    else:
      print('Your guess is higher than the number')
    lives -= 1

if lives < 0 and guess != target:
  print(f'You lost, the number was {target}')

