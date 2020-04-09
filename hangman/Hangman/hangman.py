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
    #print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    #print("  ", len(wordlist), "words loaded.")
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
#print(wordlist)

def is_word_guessed(secret_word, letters_guessed):

    count_of_guessed_letters = 0
    for letters in secret_word:
        if letters in letters_guessed:
            count_of_guessed_letters += 1
    if count_of_guessed_letters == len(secret_word):
        return True
    else:
        return False

    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    #pass

def get_guessed_word(secret_word, letters_guessed):

    guessed_word = ""
    for letter in secret_word:
        if letter in letters_guessed:
            guessed_word += letter
        else:
            guessed_word += '_ '
    return guessed_word
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    #pass

def get_available_letters(letters_guessed):

    available_letters = ""
    for letter in string.ascii_lowercase:
        if letter in letters_guessed:
            continue
        else:
            available_letters += letter
    return available_letters


    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    #pass
    
def hangman(secret_word):
    """
    #     secret_word: string, the secret word to guess.
    #
    #     Starts up an interactive game of Hangman.
    #
    #     * At the start of the game, let the user know how many
    #       letters the secret_word contains and how many guesses s/he starts with.
    #
    #     * The user should start with 6 guesses
    #
    #     * Before each round, you should display to the user how many guesses
    #       s/he has left and the letters that the user has not yet guessed.
    #
    #     * Ask the user to supply one guess per round. Remember to make
    #       sure that the user puts in a letter!
    #
    #     * The user should receive feedback immediately after each guess
    #       about whether their guess appears in the computer's word.
    #
    #     * After each guess, you should display to the user the
    #       partially guessed word so far.
    #
    #     Follows the other limitations detailed in the problem write-up.
    #     """
    # FILL IN YOUR CODE HERE AND DELETE "pass"

    print('Welcome to the game Hangman!')
    print('I am thinking of a word that is', len(secret_word) , 'letters long.')

    guessed_letters = []
    all_entered_letters = []
    chance = 6
    warning = 3

    while(chance > 0 ):

       if secret_word != get_guessed_word(secret_word,guessed_letters):

            print('----------------------')
            print('You have', warning, 'warnings left.')
            print('You have', chance, 'guesses left.')
            print('Available letters:', get_available_letters(all_entered_letters))

            guess_letter = input('Please guess the letter :').lower()

            if guess_letter.isalpha():
                if guess_letter in secret_word:

                    all_entered_letters.append(guess_letter)
                    guessed_letters.append(guess_letter)
                    list_of_guessed_letters = get_guessed_word(secret_word,guessed_letters)
                    print('Good guess : ',list_of_guessed_letters)

                elif guess_letter in guessed_letters:
                    print('You are already guessed this letter!')

                    if warning > 0:
                        warning -= 1
                    else:
                        chance -= 1
                        print(' There are no warnings left, so you lose one guess.')


                elif guess_letter in all_entered_letters:
                    print('You are already entered this letter!')

                    if warning > 0:
                        warning -= 1
                    else:
                        chance -= 1
                        print(' There are no warnings left, so you lose one guess.')
                else:
                    list_of_guessed_letters = get_guessed_word(secret_word,guessed_letters)
                    print('Oops! That letter is not in my word : ',list_of_guessed_letters)
                    all_entered_letters.append(guess_letter)

                    if warning > 0:
                        warning -= 1
                    else:
                        chance -= 1
                        print(' There are no warnings left, so you lose one guess.')
            else:
                print("Oops! That is not a valid letter.")
                if warning > 0:
                     warning -= 1
                else:
                     chance -= 1
                     print('There are no warnings left, so you lose one guess.')

            if  is_word_guessed(secret_word, guessed_letters):
                print('Congratulations! You won!')
                break
    if chance <= 0:
            print('Game over')
            print('The secret word was - ', secret_word)
pass
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
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    without_spaces = my_word.replace(" ","")

    my_word_letters = list(without_spaces)

    if len(other_word) == len(without_spaces):
        for i in range(len(without_spaces)):
            if without_spaces[i] == other_word[i]:
               continue
            elif  without_spaces[i] == "_" and other_word[i] not in my_word_letters:
               continue
            else:
               return False
        return True
    else:
        return False

def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    possible_matches = ""

    for other_word in wordlist:
        if match_with_gaps(my_word, other_word):
            possible_matches += (other_word + " ")
        else:
            continue
    if possible_matches == "":
        print("No matches found")
    else:
        print(possible_matches)

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
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    length = len(secret_word)
    guesses = 6
    warnings = 3
    letters_guessed = []

    vowels = ["a", "e", "i", "o", "u"]

    print('Welcome to the game Hangman!')
    print('I am thinking of a word that is', length , 'letters long.')
    print("Press * if you need a hint.")


    while guesses > 0:
        print("-----------------")
        print("You have", warnings, "warnings remaining.")
        print("You have", guesses, "guesses remaining.")
        print("Available letters:", get_available_letters(letters_guessed))

        letter = input("Please guess a letter: ").lower()

        if letter == '*':
            print("Possible word matches are:")
            show_possible_matches(get_guessed_word(secret_word, letters_guessed))
            continue
        elif str.isalpha(letter) == False:
            print("Oops! That is not a valid letter.")
            if warnings > 0:
                warnings -= 1
                print('You have', warnings, 'warnings left:', get_guessed_word(secret_word, letters_guessed))
            else:
                guesses -= 1
                print('There are no warnings left, so you lose one guess.')

        elif letter in letters_guessed:
            if warnings > 0:
                print('You have already guessed that letter.')
                warnings -= 1
                print('You have', warnings, 'warnings left:', get_guessed_word(secret_word, letters_guessed))
            else:
                guesses -= 1
                print('There are no warnings left, so you lose one guess.')

        else:
            letters_guessed.append(letter)

        if letter in secret_word:
            print("Good guess:", get_guessed_word(secret_word, letters_guessed))
        else:
            print("That letter is not in my word:", get_guessed_word(secret_word, letters_guessed))
            if letter in vowels:
                guesses -= 2
            else:
                guesses -= 1

        if is_word_guessed(secret_word, letters_guessed):
            total_score = guesses * length
            print("Congratulations, you won!\nYour total score for this game is:", total_score)
            break

        else:
            continue

    if guesses <= 0:
        print('Game over')
        print('The secret word was - ', secret_word)

# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    #secret_word = choose_word(wordlist)
    #hangman(secret_word)


###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
