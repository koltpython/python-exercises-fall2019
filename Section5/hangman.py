import random

def pick_random_word():
    """Returns a random word from a list of predefined options"""
    word_list = ['POTATO', 'PUMPKIN', 'QUEEN', 'ISTANBUL', 'PENINSULA', 'ARCHIPELAGO', 'COFFEE', 'ADDICTION', 'CHARISMA', 'KUCU']
    ## Your code starts here
    
    # Hint: use random.randint function, which has the docstring
    # Return random integer in range [a, b], including both end points.
    
    # random_index = random.randint(a, b)
    random_index = random.randint(0, len(word_list)-1)
    return word_list[random_index]
    ## Your code ends here
    
def input_guess_letter():
  """Takes and returns guess letter from user. Continues to ask for new letter if user enters invalid letter (length != 1)."""
  ## Your code starts here
  guess_letter = input('Your guess: ')
  while (len(guess_letter) != 1):
    guess_letter = input('Please enter a letter: ')
  return guess_letter
   ## Your code ends here
    
    
def update_display_string(correct_word, display_string, guess_letter):
  """ Do stuff """
  ## Your code starts here
  if guess_letter in correct_word:
    for ind in range(len(correct_word)):
      if guess_letter == correct_word[ind]:
        display_string = display_string[:ind] + guess_letter + display_string[ind+1:]
  return display_string
  ## Your code ends here
    
lives = 6
random_word = pick_random_word()
display_string = '_' * len(random_word)
print(f'Welcome to Hangman! You have {lives} lives to correctly guess the word.')

while lives > 0 and random_word != display_string:
    print(display_string)
    guess_letter = input_guess_letter() 
    new_display_string = update_display_string(random_word, display_string, guess_letter)
    if display_string == new_display_string:
        lives -= 1
    else:
        display_string = new_display_string


if lives > 0:
    print('Congratulations, you won!')
else:
    print(f'You run out of lives, the correct word was: {random_word}')
    
    

