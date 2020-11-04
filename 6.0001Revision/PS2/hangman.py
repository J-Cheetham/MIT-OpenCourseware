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
    for i in secret_word:
        if i not in letters_guessed:
            #print('Secret word has not been guessed')
            return False
    #print('Secret word has been guessed')
    return True


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    secret_word_list = []
    for i in secret_word:
        if i not in letters_guessed:
            secret_word_list.append('_ ')
        else:
            secret_word_list.append(i)
    print(''.join(secret_word_list))
    return''.join(secret_word_list)




def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    letters = string.ascii_lowercase
    letters_list = []

    for i in letters:
        if i not in letters_guessed:
            letters_list.append(i)
    return ''.join(letters_list)


# secret_word = "apple"
# letters_guessed = ['e', 'i', 'k', 'p', 'r', 's',]
# get_available_letters(letters_guessed)
    
def unique_secret_letter(secret_word):
    unique_letter = []
    for i in secret_word:
        if i not in unique_letter:
            unique_letter.append(i)
    return len(unique_letter)


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

    remaining_guesses = int(6)
    letters_guessed = []
    remaining_warnings = int(3)
    vowels = 'aeiou'
    consonants = 'bcdfghjklmnpqrstvwxyz'
    print('Welcome to the game of Hangman! \n I am thinking of a word that is ', len(secret_word), 'letters long')
    while remaining_guesses > 0:
        print('-------------')
        #How many warnings do they have left? Don't show negative warnings.
        print('You have', remaining_guesses, 'guesses left.')
        if remaining_warnings > 0:
            print('You have', remaining_warnings, 'warnings left')
        else:
            print('You have 0 warnings left.')
        print('Available letters: ', get_available_letters(letters_guessed))
        get_guessed_word(secret_word, letters_guessed)
        user_guess = input('Please guess a letter:')

        #is user_guess a letter?
        if not user_guess.isalpha():
            remaining_warnings -= 1
            print('That is not a letter! Please only input letters.')
            if remaining_warnings < 0:
                remaining_guesses -= 1
                print('No more warnings, lose a guess!')
            continue
        elif user_guess.isupper():
            legit_user_guess = user_guess.lower()
        else:
            legit_user_guess = user_guess

        #has user_guess been guessed before?
        if legit_user_guess in letters_guessed:
            remaining_warnings -= 1
            if remaining_warnings < 0:
                remaining_guesses -= 1
                print('No more warnings, lose a guess!')
            print('Letter has already been guessed. Please try again.')
            continue
        else:
            letters_guessed.append(legit_user_guess)

        #is user guess in the secret word?
        if legit_user_guess in secret_word:
            print('Congratulations, that letter is in the secret word.')
        elif legit_user_guess in consonants:
            remaining_guesses -= 1
            print('Unlucky, that consonant is not in the secret word.')
        else:
            remaining_guesses -= 2
            print('Unlucky, that vowel is not in the secret word')

        if is_word_guessed(secret_word, letters_guessed):
            print('You have guessed the secret word!')
            final_score = remaining_guesses * unique_secret_letter(secret_word)
            print('Your final score is:', final_score)
            break

    if remaining_guesses < 1:
        print('Sorry, you did not guess the word in time!')


#secret_word = 'tact'
# hangman(choose_word(wordlist))

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
    stripped_my_word = my_word.replace(" ", "")
    stripped_other_word = other_word.strip()

    if len(stripped_my_word) != len(stripped_other_word):
        return False

    for i in range(len(stripped_my_word)):
        if stripped_my_word[i] == ("_") or stripped_my_word[i] == stripped_other_word[i]:
            continue
        else:
            return False
    return True


my_word = "ta_ t"
other_word = "tact"
#match_with_gaps(my_word, other_word)

def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    matched_words = []
    for i in wordlist:
        if match_with_gaps(my_word, i):
            matched_words.append(i)

    print('Possible word matches are:\n', " ".join(matched_words))


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
    remaining_guesses = int(6)
    letters_guessed = []
    remaining_warnings = int(3)
    vowels = 'aeiou'
    consonants = 'bcdfghjklmnpqrstvwxyz'
    print('Welcome to the game of Hangman! \n I am thinking of a word that is ', len(secret_word), 'letters long')
    while remaining_guesses > 0:
        print('-------------')
        # How many warnings do they have left? Don't show negative warnings.
        print('You have', remaining_guesses, 'guesses left.')
        if remaining_warnings > 0:
            print('You have', remaining_warnings, 'warnings left')
        else:
            print('You have 0 warnings left.')
        print('Available letters: ', get_available_letters(letters_guessed))
        get_guessed_word(secret_word, letters_guessed)
        user_guess = input('Please guess a letter:')

        # is user_guess a letter? Handle * usage
        if user_guess == "*" and user_guess not in letters_guessed:
            legit_user_guess = user_guess
            show_possible_matches(get_guessed_word(secret_word, letters_guessed))
        elif not user_guess.isalpha():
            remaining_warnings -= 1
            print('That is not a letter! Please only input letters.')
            if remaining_warnings < 0:
                remaining_guesses -= 1
                print('No more warnings, lose a guess!')
            continue
        elif user_guess.isupper():
            legit_user_guess = user_guess.lower()
        else:
            legit_user_guess = user_guess

        # has user_guess been guessed before?
        if legit_user_guess in letters_guessed:
            remaining_warnings -= 1
            if remaining_warnings < 0:
                remaining_guesses -= 1
                print('No more warnings, lose a guess!')
            print('Letter has already been guessed. Please try again.')
            continue
        else:
            letters_guessed.append(legit_user_guess)

        # is user guess in the secret word?
        if legit_user_guess in secret_word:
            print('Congratulations, that letter is in the secret word.')
        elif legit_user_guess in consonants:
            remaining_guesses -= 1
            print('Unlucky, that consonant is not in the secret word.')
        elif legit_user_guess in vowels:
            remaining_guesses -= 2
            print('Unlucky, that vowel is not in the secret word')

        if is_word_guessed(secret_word, letters_guessed):
            print('You have guessed the secret word!')
            final_score = remaining_guesses * unique_secret_letter(secret_word)
            print('Your final score is:', final_score)
            break

    if remaining_guesses < 1:
        print('Sorry, you did not guess the word in time!')



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
#
#     secret_word = choose_word(wordlist)
#     hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
