'''
Created on 28/08/2012

@author: carlosfelgarcia
'''
#'''
#Created on 25/08/2012
#
#@author: carlosfelgarcia
#'''
## 6.00 Problem Set 2
##
## Successive Approximation
##
#import math as mat
#
#
#
#def evaluate_poly(poly, x):
#    """
#    Computes the polynomial function for a given value x. Returns that value.
#
#    Example:
#    >>> poly = (0.0, 0.0, 5.0, 9.3, 7.0)    # f(x) = 7x^4 + 9.3x^3 + 5x^2
#    >>> x = -13
#    >>> print evaluate_poly(poly, x)  # f(-13) = 7(-13)^4 + 9.3(-13)^3 + 5(-13)^2
#    180339.9
#
#    poly: tuple of numbers, length > 0
#    x: number
#    returns: float
#    """
#    # TO DO ...
#    result = 0
#    for i in range(0,len(poly)):
#        result = result + (poly[i]*x**i)
#        
#    return result
#
#
#def compute_deriv(poly):
#    """
#    Computes and returns the derivative of a polynomial function. If the
#    derivative is 0, returns (0.0,).
#
#    Example:
#    >>> poly = (-13.39, 0.0, 17.5, 3.0, 1.0)    # x^4 + 3x^3 + 17.5x^2 - 13.39
#    >>> print compute_deriv(poly)        # 4x^3 + 9x^2 + 35^x
#    (0.0, 35.0, 9.0, 4.0)
#
#    poly: tuple of numbers, length > 0
#    returns: tuple of numbers
#    """
#    # TO DO ...
#
#    assert len(poly)>0
#    derivate = ()
#    for i in range (1,len(poly)):
#        if poly[i] == 0:
#            derivate = derivate + (0.0,)
#        
#        else:
#            temp = i*poly[i]
#            derivate = derivate + (temp,)
#    return derivate
#
#
#        
#    
#
#def compute_root(poly, x_0, epsilon):
#    """
#    Uses Newton's method to find and return a root of a polynomial function.
#    Returns a tuple containing the root and the number of iterations required
#    to get to the root.
#
#    Example:
#    >>> poly = (-13.39, 0.0, 17.5, 3.0, 1.0)    #x^4 + 3x^3 + 17.5x^2 - 13.39
#    >>> x_0 = 0.1
#    >>> epsilon = .0001
#    >>> print compute_root(poly, x_0, epsilon)
#    (0.80679075379635201, 8.0)
#
#    poly: tuple of numbers, length > 1.
#         Represents a polynomial function containing at least one real root.
#         The derivative of this polynomial function at x_0 is not 0.
#    x_0: float
#    epsilon: float > 0
#    returns: tuple (float, int)
#    """
#    # TO DO ... 
#    assert len(poly)>1
#    result = ()
#    evaluation = 1
#    counter = 0
#    while abs(evaluation) > epsilon:
#        counter += 1
#        evaluation = evaluate_poly(poly, x_0)
#        if abs(evaluation) < epsilon:
#            result = result + (x_0,counter)
#        else:
#            derivPoly =  compute_deriv(poly)
#            temp= evaluate_poly(derivPoly, x_0)
#            x_0 = x_0 - (evaluation / temp)
#    return result
#
#poly = (-13.39, 0.0, 17.5, 3.0, 1.0)    #x^4 + 3x^3 + 17.5x^2 - 13.39
#x_0 = 0.1
#epsilon = .0001
#print compute_root(poly, x_0, epsilon)
        
        

#******************************************* 2 Part *******************************

# 6.00 Problem Set 3
# 
# Hangman
#


# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
import random
import string



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
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

def position(word, letter):
    indexs=()
    for i in range(0,len(word)):
        if word[i] == letter:
            indexs=indexs + (i,)
    return indexs
        
    

# end of helper code
# -----------------------------------

# actually load the dictionary of words and point to it with 
# the wordlist variable so that it can be accessed from anywhere
# in the program
wordlist = load_words()
finish = False
word=choose_word(wordlist)
numGuess=9
alpha=string.lowercase
respound = ""
for res in range(0,len(word)):
    respound = respound + "_"

next='-------------------'
print 'Welcome to the game, Hangman!\n' + 'I am thinking of a word that is ', len(word) , " letters long."
while finish == False:
    wordLower=str(word).lower()
    print next, word
    print "You have ", numGuess, " guesses left"
    print "Available letters: ", alpha
    sizeAlpha = len(alpha)
    
    letter = raw_input("Please guess a letter: ")
    #Take out the letter
    for i in range(0,len(alpha)):
        if(alpha[i]==letter):
            alpha=alpha[0:i] + alpha[i+1: len(alpha)]
            break
    
    index=position(word,letter)
    if(index==()):
        numGuess-=1
        print "Oops! That letter is not in my word: ", respound
        if(numGuess == 0):
            print "You lose!!!, you don't have more guesses left"
            print "The word was: ", word
            finish=True
        
    else:
        
        for y in range(0,len(index)):
            
            for z in range(0,len(word)):
                if z == index[y]:
                    respound = respound[0:z] + letter + respound[z+1:len(word)]
        if respound == word:
            print "Good guess: ", respound  
            print "Congratulations, You Won!!!"
            finish = True            
        else:
            print "Good guess: ", respound    
            
        
    
#    finish = True
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    






