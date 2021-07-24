# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    for char in secret_word:
      if char not in letters_guessed:
        return False
    return True

# secret_word = 'apple' 
# letters_guessed = ['e', 'l', 'a', 'p'] 
# print(is_word_guessed(secret_word, letters_guessed))

def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    str = ""
    for char in secret_word:
      if char not in letters_guessed:
        str += "_ "
      else:
        str += char
    return str

# secret_word = 'apple' 
# letters_guessed = ['e', 'i', 'a', 'p'] 
# print(get_guessed_word(secret_word, letters_guessed))

def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    str = ""
    for char in string.ascii_lowercase:
      if char not in letters_guessed:
        str += char
    return str
    
letters_guessed = ['e', 'i', 'k', 'p', 'r', 's'] 
print(get_available_letters(letters_guessed))

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    number_of_guesses_left = 6
    number_of_warnings_left = 3
    letters_guessed = []
    hasLost = False

    print("Loading word list from file...\n55900 words loaded.\nWelcome to the game Hangman!")
    print("I am thinking of a word that is "+ len(secret_word) + " letters long.\n-------------\n")
    
    while hasLost == False:
      print("You have " + number_of_guesses_left + " guesses left.")
      print('Available letters: {}'.format(get_available_letters(letters_guessed)))
    
      letter_guessed = input("Please enter a letter: ")
      guessed_word = get_guessed_word(secret_word, letters_guessed)

      if letter_guessed().isalpha():
        if letter_guessed not in letters_guessed:   
          letters_guessed.append(letter_guessed)
          guessed_word = get_guessed_word(secret_word, letters_guessed)
              
          if letter_guessed in secret_word:
            print("Good guess: " + guessed_word)
          else:
            if letter_guessed in 'aeiou':
                number_of_guesses_left -= 2
            else:
                number_of_guesses_left -= 1  
            print("Oops! That letter is not in my word: " + guessed_word)
          
      else:
        if number_of_warnings_left > 0:
          number_of_warnings_left -= 1
          print("Oops! That is not a valid letter. You have " + number_of_warnings_left + " warnings left: " + guessed_word)
        else:
          number_of_guesses_left -= 1
          print("Oops! You\'ve already guessed that letter. You now have no warnings left so you lose one guess: " + guessed_word)
      if is_word_guessed(secret_word, letters_guessed):
          unique_letters_in_secret_word = ""
          for char in secret_word:
              if char not in unique_letters_in_secret_word:
                  unique_letters_in_secret_word += char
          
          score = len(unique_letters_in_secret_word) * number_of_guesses_left
          print("Congratulations, you won!")
          print("Your total score for this game is " + score)
          hasLost = True
  
      if number_of_guesses_left <= 0:
          print("Sorry, you ran out of guesses. The word was " + secret_word)
          hasLost = True



# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    letters_guessed = []
    no_space_word = ""
    for char in my_word:
      if char != " ":
        no_space_word += char
      if char.isalpha():
        letters_guessed.append(char)
        
    if len(no_space_word.strip()) != len(other_word.strip()):
        return False
    
    for i in range(len(no_space_word)):
        current_letter =  no_space_word[i]
        other_letter = other_word[i]
        if current_letter.isalpha():
            has_same_letter = current_letter == other_letter
            if not has_same_letter:
                return False
        else:
            if current_letter == '_' and other_letter in letters_guessed:
                return False
            
    return True




def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    match_words = []
    for word in wordlist:
        if match_with_gaps(my_word, word):
            match_words.append(word)
    
    if len(match_words) > 0:
        for word in match_words:
            print(word, end=' ')
        print()
    else:
        print('No matches found')



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    number_of_guesses_left = 6
    number_of_warnings_left = 3
    letters_guessed = []
    hasLost = False

    print("Loading word list from file...\n55900 words loaded.\nWelcome to the game Hangman!")
    print("I am thinking of a word that is "+ len(secret_word) + " letters long.\n-------------\n")
    
    while hasLost == False:
      print("You have " + number_of_guesses_left + " guesses left.")
      print('Available letters: {}'.format(get_available_letters(letters_guessed)))
    
      letter_guessed = input("Please enter a letter: ")
      guessed_word = get_guessed_word(secret_word, letters_guessed)

      if letter_guessed().isalpha():
        if letter_guessed not in letters_guessed:   
          letters_guessed.append(letter_guessed)
          guessed_word = get_guessed_word(secret_word, letters_guessed)
              
          if letter_guessed in secret_word:
            print("Good guess: " + guessed_word)
          else:
            if letter_guessed in 'aeiou':
                number_of_guesses_left -= 2
            else:
                number_of_guesses_left -= 1  
            print("Oops! That letter is not in my word: " + guessed_word)
      elif letter_guessed == '*':
        print('Possible word matches are: ')
        show_possible_matches(guessed_word)  
      else:
        if number_of_warnings_left > 0:
          number_of_warnings_left -= 1
          print("Oops! That is not a valid letter. You have " + number_of_warnings_left + " warnings left: " + guessed_word)
        else:
          number_of_guesses_left -= 1
          print("Oops! You\'ve already guessed that letter. You now have no warnings left so you lose one guess: " + guessed_word)
      if is_word_guessed(secret_word, letters_guessed):
          unique_letters_in_secret_word = ""
          for char in secret_word:
              if char not in unique_letters_in_secret_word:
                  unique_letters_in_secret_word += char
          
          score = len(unique_letters_in_secret_word) * number_of_guesses_left
          print("Congratulations, you won!")
          print("Your total score for this game is " + score)
          hasLost = True
  
      if number_of_guesses_left <= 0:
          print("Sorry, you ran out of guesses. The word was " + secret_word)
          hasLost = True



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    secret_word = choose_word(wordlist)
    hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    #secret_word = choose_word(wordlist)
    #hangman_with_hints(secret_word)
