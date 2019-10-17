import random
# random 4 digit number in string format
number = str(random.randint(1000, 9999))

print('Let\'s play a game of Cowbull!')
print('I will generate a number, and you have to guess the numbers one digit at a time.')
print('For every number in the wrong place, you get a cow. For every one in the right place, you get a bull.')
print('The game ends when you get 4 bulls!')
print('Type exit at any prompt to exit.')

# Your code starts here
guess = input('Enter a number: ')
num_guesses = 0

while guess != number and guess != 'exit':
    num_guesses += 1

    bulls = 0
    cows = 0
    # copy number since we need the original value
    number_copy = number

    # Calculate bulls
    for index in range(len(number_copy)):
      # Replace matched characters with Xs and Ys to exclude from cow calculation
        if number_copy[index] == guess[index]:
            bulls += 1
            number_copy = number_copy[:index] + 'X' + number_copy[index+1:]
            guess = guess[:index] + 'Y' + guess[index+1:]

    # Calculate cows
    for character in guess:
        if character in number_copy:
            cows += 1
            first_index = number_copy.index(character)
            number_copy = number_copy[:first_index] + \
                'X' + number_copy[first_index+1:]
    print(f'{cows} cows, {bulls} bulls')
    guess = input('> ')

if guess == 'exit':
    print(
        f'You gave up after {num_guesses} guesses, the correct answer was {number}')
else:
    print(f'You win the game after {num_guesses} guesses')
