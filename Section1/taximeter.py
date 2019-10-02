name = input('Welcome, what is your name: ')
loc = input(f'Hi, {name}! Where are you going from?')
dest = input('And, where are we going?')
dist = float(input('What is the total distance in km?'))

total = 4 + 1.15*dist
print(f'Okay, {name}. You are travelling from {loc} to {dest} which is {dist} kms and your total is {total}')

