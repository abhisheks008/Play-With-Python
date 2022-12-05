

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
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

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    
    for letter in secretWord:
        if letter not in lettersGuessed:
            return False
    return True
    



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    
    word=""
    for letter in secretWord:
        if letter in lettersGuessed:
            word+=letter
        else:
            word+='_'
    return word



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    
    import string
    alphabet = string.ascii_lowercase
    lst_alphabet = list(alphabet)
    for letter in lettersGuessed:
        if letter in lst_alphabet:
            lst_alphabet.remove(letter)
    alpha = ''.join(lst_alphabet)
    return alpha
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
   
    print('Welcome to the game, Hangman!')
    print('I am thinking of a word that is', len(secretWord), 'letters long.')
    print('-------------')
    guess_numbers = 8
    lettersGuessed = ''
    while guess_numbers >= 1:
        if isWordGuessed(secretWord, lettersGuessed) == True:
            print("Congratulations, you won!")
            break
        else:
            print("You have", guess_numbers, "guesses left") 
            print("Available letters:",getAvailableLetters(lettersGuessed)) 
            guess = input("Please guess a letter: ").lower()
            
            if guess in secretWord and guess not in lettersGuessed:
                
                lettersGuessed+=guess
                print("Good guess:",getGuessedWord(secretWord, lettersGuessed))
                print('-------------')
                if isWordGuessed(secretWord, lettersGuessed) == True:
                    print("Congratulations, you won!")
                    break
            
            elif guess in lettersGuessed:
                print("Oops! You've already guessed that letter:",getGuessedWord(secretWord, lettersGuessed))
                print('-------------')
            
            elif guess not in secretWord:
                guess_numbers = guess_numbers - 1
                lettersGuessed+=guess
                print("Oops! That letter is not in my word:",getGuessedWord(secretWord, lettersGuessed))
                print('-------------')
                if guess_numbers == 0:
                    print('Sorry, you ran out of guesses. The word was else', secretWord)








secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
