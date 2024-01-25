
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "word_list.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Reading word_list file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # word_list: list of strings
    word_list = line.split()
    print(len(word_list), "words found")
    return word_list

def choose_word(word_list):
    """
    word_list (list): list of words (strings)

    Returns a word from word_list at random
    """
    return random.choice(word_list)

# end of helper code
# -----------------------------------

# Load the list of words into the variable word_list
# so that it can be accessed from anywhere in the program
word_list = load_words()

def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    for letter in secret_word:
      if letter not in letters_guessed:
        return False
    
    return True


    pass


### Testcases
# print(is_word_guessed('apple', ['a', 'e', 'i', 'k', 'p', 'r', 's']))
# print(is_word_guessed('durian', ['h', 'a', 'c', 'd', 'i', 'm', 'n', 'r', 't', 'u']))
# print(is_word_guessed('pineapple', []))

print('')
print("-----")
print('')
def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    result = ''
    for letter in secret_word:
      if letter in letters_guessed:
        result += letter
      else:
          result += ' _ '
    return result
    
    
    
    
      
#Testcases
# print(get_guessed_word('apple', ['e', 'i', 'k', 'p', 'r', 's']))
# print(get_guessed_word('durian', ['a', 'c', 'd', 'h', 'i', 'm', 'n', 'r', 't', 'u']))

def get_available_letters(letters_guessed):
    '''
    letters_guessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...   
    available_letter = string.ascii_lowercase
    for character in letters_guessed:
       if character in available_letter:
          available_letter = available_letter.replace(character, '')
    return available_letter
    



#Testcases 
# print( get_available_letters(['e', 'i', 'k', 'p', 'r', 's']) )
# print(get_available_letters(['p', 'r', 'f', 'd', 'k', 'h', 'c', 'a', 'i', 'y', 'w', 'b']))
  
def game_loop(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Starts up an interactive game.

    * At the start of the game, let the user know how many 
      letters the secret_word contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    number_of_guess = 8
    # FILL IN YOUR CODE HERE...
    letter_guess = ['']
    print ('Let the game begin!')
    print ('I thinking of a ' + str(len(secret_word)) + ' letters word.')
    print ('You have ' + str(number_of_guess) + ' guess remaining')
    end_game = False
    while end_game == False:
      if number_of_guess > 0:
        character = input('Enter a Letter: ').lower()
        if character in letter_guess:
          print()
          print("Fool, you already use this letter!")
          print( get_guessed_word(secret_word, letter_guess))
          
        elif character in secret_word:
          letter_guess.append(character)
          print('')
          print('Correct: ' + get_guessed_word(secret_word, letter_guess))
          
        elif character not in secret_word:
          letter_guess.append(character)
          print('')
          number_of_guess -= 1
          print('Incorrect: ' + get_guessed_word(secret_word, letter_guess))

        print('Available Letters: ' + get_available_letters(letter_guess))
        print ('You have ' + str(number_of_guess) + ' guesses remaining')


        if (is_word_guessed(secret_word, letter_guess)) == True:
            print("")
            print('!Congratulation you win!')
            end_game = True
        elif number_of_guess == 0:
          end_game = True
          print('------')
          print('Game over. The word was "' + secret_word + '"')
    

    





def main():
    secret_word = choose_word(word_list)
    game_loop(secret_word)

# Testcases
# you might want to pick your own
# secret_word while you're testing


if __name__ == "__main__":
    main()