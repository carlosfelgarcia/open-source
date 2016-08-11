'''
Created on 16/09/2012

@author: carlosfelgarcia
'''

# 6.00 Problem Set 3A Solutions
#
# The 6.00 Word Game
# Created by: Kevin Luu <luuk> and Jenna Wiens <jwiens>
#
#

import random
import string
from perm import *

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
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
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print "  ", len(wordlist), "words loaded."
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
    
   
    total = 0
   
    for letter in word:
        total = total + SCRABBLE_LETTER_VALUES[letter]
        
    if n==len(word):
        total = (total * len(word) ) + 50
       
    else:
        total = total * len(word)
        
    return total
  
    
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
        for j in range(hand[letter]):
             print letter,              # print all on the same line
    print                              # print an empty line

#
# Make sure you understand how this function works and what it does!
#
def deal_hand(n):
    """
    Returns a random hand containing n lowercase letters.
    At least n/3 the letters in the hand should be VOWELS.

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    hand={}
    num_vowels = n / 3
    
    for i in range(num_vowels):
        x = VOWELS[random.randrange(0,len(VOWELS))]
        hand[x] = hand.get(x, 0) + 1
        
    for i in range(num_vowels, n):    
        x = CONSONANTS[random.randrange(0,len(CONSONANTS))]
        hand[x] = hand.get(x, 0) + 1
        
    return hand

#
# Problem #2: Update a hand by removing letters
#
def update_hand(hand, word):
    
    retHand = {}
    keys = hand.keys()
    
    for key in keys:
        if key in word:
            number = 0
            for j in word:
                if j == key:
                    number = number + 1
            
            if hand.get(key, 0) - number != 0:
                retHand[key] = hand.get(key, 0) - number
        else:
            retHand[key] = hand.get(key, 0)
    
   
    return retHand
   

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
    """
    valid=True
    tempDic = {}
    if word in word_list:
        for letter in word:
            if hand.has_key(letter):
                if tempDic.has_key(letter):
                    if tempDic.get(letter) > 0:
                        tempDic[letter] = tempDic.get(letter, 0) - 1
                    else:
                        valid = False
                        break
                else:
                    tempDic[letter] = hand.get(letter, 0) - 1
            else:
                valid = False
                break
    else:
        valid = False
                

    return valid

#
# Calculate the lenght of the hand
#
def calculate_handlen(hand):
    handlen = 0
    for v in hand.values():
        handlen += v
    return handlen

#
# Problem #4: Playing a hand
#
def play_hand(hand, word_list):
    
    handSize = calculate_handlen(hand)
    handSizeOriginal = calculate_handlen(hand)
    total=0
    
    
    while(handSize > 0):
        print "Current Hand: ", 
        display_hand(hand)
        
        word = raw_input("Enter word, or ""."" to indicate that you are finished: ")
        if word != ".":
            if is_valid_word(word, hand, word_list)==False:
                print "Invalid word please try again"
            else:
                total = total + get_word_score(word,  handSizeOriginal)
                print word, "earned", get_word_score(word,  handSizeOriginal), "points. Total:", total, "points"
                hand = update_hand(hand, word)
                handSize = calculate_handlen(hand)
                   
        else:
            break 
     
    print "your total score: ", total   
    
    

#
# Problem #5: Playing a game
# Make sure you understand how this code works!
# 
def play_game(word_list):
    hand = deal_hand(HAND_SIZE)
    while True:
        acc = raw_input("welcome to the word game, you can write n for new game, r for play the last hand again or e to exit the game: ")
        if acc == "n":
            handN = deal_hand(HAND_SIZE)
            play_hand(handN, word_list)
           
        elif acc=="r":
            play_hand(hand, word_list)
            
        elif acc=="e":
            print "Thank you for playing"
            break
        else:
            print"remember just n,r or e"
        
#
#Problem 6A:Computer Choose Word
#
def comp_choose_word(hand,word_list):
    word=""
    wordList=get_perms(hand,HAND_SIZE)
    for i in wordList:
        if is_valid_word(i, hand, word_list)==True:
            word=i
            break
       
            
    return word    




# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    word_list = load_words()
    hand = {'a':2, 'b':1, 'l':1, 'o':1, 'n':1, 'e':1}
    print comp_choose_word(hand,word_list)
    play_game(word_list)
