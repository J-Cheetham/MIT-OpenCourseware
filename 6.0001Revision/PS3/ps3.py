# 6.0001 Problem Set 3
#
# The 6.0001 Word Game
# Created by: Kevin Luu <luuk> and Jenna Wiens <jwiens>
#
# Name          : <your name>
# Collaborators : <your collaborators>
# Time spent    : <total time>

import math
import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    '*': 0, 'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

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
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq
	

# (end of helper code)
# -----------------------------------

#
# Problem #1: Scoring a word
#
def get_word_score(word, n):
    """
    Returns the score for a word. Assumes the word is a
    valid word.

    You may assume that the input word is always either a string of letters, 
    or the empty string "". You may not assume that the string will only contain 
    lowercase letters, so you will have to handle uppercase and mixed case strings 
    appropriately. 

	The score for a word is the product of two components:

	The first component is the sum of the points for letters in the word.
	The second component is the larger of:
            1, or
            7*wordlen - 3*(n-wordlen), where wordlen is the length of the word
            and n is the hand length when the word was played

	Letters are scored as in Scrabble; A is worth 1, B is
	worth 3, C is worth 3, D is worth 2, E is worth 1, and so on.

    word: string
    n: int >= 0
    returns: int >= 0
    """
    score_part_1 = int(0)
    word_lower = word.lower()

    for i in word_lower:
        score_part_1 += SCRABBLE_LETTER_VALUES[i]

    score_part_2 = (7 * len(word_lower) - (3 * (n - len(word_lower))))
    if score_part_2 < 1:
        score_part_2 = 1

    return score_part_1 * score_part_2

#
# Make sure you understand how this function works and what it does!
#
def display_hand(hand):
    """
    Displays the letters currently in the hand.

    For example:
       display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    
    for letter in hand.keys():
        #looks at value which tells you how many times it occurs.
        for j in range(hand[letter]):
             print(letter, end=' ')      # print all on the same line
    print()                              # print an empty line

#
# Make sure you understand how this function works and what it does!
# You will need to modify this for Problem #4.
#
def deal_hand(n):
    """
    Returns a random hand containing n lowercase letters.
    ceil(n/3) letters in the hand should be VOWELS (note,
    ceil(n/3) means the smallest integer not less than n/3).

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    
    hand={}
    hand.update({'*': 1})
    num_vowels = int(math.ceil(n / 3)) - 1

    for i in range(num_vowels):
        x = random.choice(VOWELS)
        hand[x] = hand.get(x, 0) + 1
    
    for i in range(num_vowels, n):    
        x = random.choice(CONSONANTS)
        hand[x] = hand.get(x, 0) + 1
    
    return hand

#
# Problem #2: Update a hand by removing letters
#
def update_hand(hand, word):
    """
    Does NOT assume that hand contains every letter in word at least as
    many times as the letter appears in word. Letters in word that don't
    appear in hand should be ignored. Letters that appear in word more times
    than in hand should never result in a negative count; instead, set the
    count in the returned hand to 0 (or remove the letter from the
    dictionary, depending on how your code is structured). 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    word = word.lower()
    hand_copy = hand.copy()
    for i in word:
        x = hand_copy.get(i)
        if x is None:
            continue
        else:
            x -= 1
            if x < 1:
                del(hand_copy[i])
            else:
                hand_copy[i] = x
    return hand_copy

#
# Problem #3: Test word validity
#
def is_valid_word(word, hand, word_list):
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or word_list.
   
    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    returns: boolean
    """
    word = word.lower()
    hand_list = []
    for letter in hand.keys():
        #looks at value which tells you how many times it occurs.
        for j in range(hand[letter]):
             hand_list.append(letter)

    for i in word:
        if i not in hand_list:
            return False
        else:
            hand_list.remove(i)

    for i in range(0, len(word_list)):
        if len(word) == len(word_list[i]): #Is the length of the two words the same?
            for j in range(0, len(word)):
                if (word[j] == (word_list[i])[j]) or (word[j] == '*' and (word_list[i])[j] in VOWELS): #Do the letters match?
                    if j == (len(word) - 1): #Is it the end of the word?
                        return True
                else: #If letters don't match, abandon comparison and move onto next word
                    break
    return False

# hand = {'a':1, 'o':1, 'e':2, 'm':1, '*':1}
# word = 'e*m'
# hand = {'a': 1, 'r': 1, 'e': 1, 'j': 2, 'm': 1, '*': 1}
# word = 'c*wz'

#
# Problem #5: Playing a hand
#
def calculate_handlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string-> int)
    returns: integer
    """
    hand_length = sum(hand.values())
    return hand_length

# hand = {'a':1, 'o':1, 'e':1, 'm':3, '*':1}
# calculate_handlen(hand)

def play_hand(hand, word_list):

    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    
    * The user may input a word.

    * When any word is entered (valid or invalid), it uses up letters
      from the hand.

    * An invalid word is rejected, and a message is displayed asking
      the user to choose another word.

    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.

    * The sum of the word scores is displayed when the hand finishes.

    * The hand finishes when there are no more unused letters.
      The user can also finish playing the hand by inputing two 
      exclamation points (the string '!!') instead of a word.

      hand: dictionary (string -> int)
      word_list: list of lowercase strings
      returns: the total score for the hand
      
    """
    hand_length = calculate_handlen(hand)
    player_hand = hand
    hand_score = int(0)
    while hand_length > 0:
        print('Letters in hand:', end = ' ')
        display_hand(player_hand)
        user_guess = input('Please guess a word or enter "!!" to indicate you are finished:')

        if is_valid_word(user_guess, hand, word_list):
            hand_score += get_word_score(user_guess, hand_length)
            print(user_guess, 'is worth', get_word_score(user_guess, hand_length) , 'points!', end = ' ')
            print('Total score', hand_score)
            print()
            player_hand = update_hand(player_hand, user_guess)
            hand_length = calculate_handlen(player_hand)
        elif user_guess == '!!':
            print('Total score:', hand_score)
            return hand_score
        elif not is_valid_word(user_guess, hand, word_list):
            player_hand = update_hand(player_hand, user_guess)
            hand_length = calculate_handlen(player_hand)
            print('Invalid word!')
    print('Ran out of letters. Total score:', hand_score)
    return hand_score

# hand = {'a': 1, 'c': 1, 'i': 1, 'f': 1, '*':1, 't': 1, 'x': 1}
# word_list = load_words()
# play_hand(hand, word_list)


#
# Problem #6: Playing a game
# 


#
# procedure you will use to substitute a letter in a hand
#

def substitute_hand(hand, letter):
    """ 
    Allow the user to replace all copies of one letter in the hand (chosen by user)
    with a new letter chosen from the VOWELS and CONSONANTS at random. The new letter
    should be different from user's choice, and should not be any of the letters
    already in the hand.

    If user provide a letter not in the hand, the hand should be the same.

    Has no side effects: does not mutate hand.

    For example:
        substitute_hand({'h':1, 'e':1, 'l':2, 'o':1}, 'l')
    might return:
        {'h':1, 'e':1, 'o':1, 'x':2} -> if the new letter is 'x'
    The new letter should not be 'h', 'e', 'l', or 'o' since those letters were
    already in the hand.
    
    hand: dictionary (string -> int)
    letter: string
    returns: dictionary (string -> int)
    """
    
    new_hand = hand.copy()
    key_list = new_hand.keys()
    letters = []

    #Create a list of all consonants and vowels
    for i in range(0, len(VOWELS)):
        letters.append(VOWELS[i])
    for i in range(0, len(CONSONANTS)):
        letters.append(CONSONANTS[i])

    #Remove all letters from the list that are already in the hand
    for i in key_list:
        if i in letters:
            letters.remove(i)
        else:
            continue

    letter_instances = new_hand.get(letter)
    new_hand.pop(letter)
    new_letter = random.choice(letters)
    new_hand.update({new_letter: letter_instances})

    return new_hand


letter = 'a'
hand = {'a': 1, 'c': 1, 'i': 1, 'f': 1, '*':1, 't': 1, 'x': 1}
substitute_hand(hand, letter)


def play_game(word_list):
    """
    Allow the user to play a series of hands

    * Asks the user to input a total number of hands

    * Accumulates the score for each hand into a total score for the 
      entire series
 
    * For each hand, before playing, ask the user if they want to substitute
      one letter for another. If the user inputs 'yes', prompt them for their
      desired letter. This can only be done once during the game. Once the
      substitute option is used, the user should not be asked if they want to
      substitute letters in the future.

    * For each hand, ask the user if they would like to replay the hand.
      If the user inputs 'yes', they will replay the hand and keep 
      the better of the two scores for that hand.  This can only be done once 
      during the game. Once the replay option is used, the user should not
      be asked if they want to replay future hands. Replaying the hand does
      not count as one of the total number of hands the user initially
      wanted to play.

            * Note: if you replay a hand, you do not get the option to substitute
                    a letter - you must play whatever hand you just had.
      
    * Returns the total score for the series of hands

    word_list: list of lowercase strings
    """

    rounds = int(0)
    while rounds == 0:
        user_rounds = input('How many rounds do you want to play?')
        if user_rounds.isnumeric() and not 0:
            rounds = int(user_rounds)
        else:
            print('Please enter a number greater than 0.')

    game_total_score = 0
    current_round = int(0)
    sub_counter = int(1)

    while current_round < (rounds):
        first_score = int(0)
        replay_score = int(0)
        current_hand = deal_hand(HAND_SIZE)
        display_hand(current_hand)
        if sub_counter > 0:
            if (input('Do you wish to replace a letter in your hand with a randomly chosen one? y/n') == 'y'):
                letter_to_swap = input('Which letter do you want to change?')
                current_hand = substitute_hand(current_hand,letter_to_swap)
                sub_counter += 1

        first_score += play_hand(current_hand, word_list)
            #TODO implement ability to replay a hand
        if input('Do you wish to replay this hand to try and get a higher score? y/n') == 'y':
            replay_score = play_hand(current_hand, word_list)
        if first_score > replay_score:
            game_total_score += first_score
            print('Your first attempt was better so that score of', first_score, 'has been added to your total score for the game.')
        else:
            game_total_score += replay_score
            print('You scored more on your second attempt! That score of', replay_score, 'has been added to your total score for the game.')

        current_round += 1
    print('Total score over all hands:', game_total_score)
#
# Build data structures used for entire session and play game
# Do not remove the "if __name__ == '__main__':" line - this code is executed
# when the program is run directly, instead of through an import statement
#
if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)

