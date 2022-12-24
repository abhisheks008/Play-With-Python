# Hacking mini game
import sys
import random

GARBAGE_CHARS = '~!@#$%^&*()_+-={}[]|;:,.<>?/'
# WORDS is a list of words that the player must guess (7 letter words)
WORDS=['ADDRESS','TESTING','RESOLVE','DESPITE','ABILITY','ABSENCE','CRYSTAL','CORRECT','DEFAULT','DEPOSIT','DYNAMIC','EFFECTS']

def printComputerMemory():
    """Print the computer memory with the words in the WORDS list."""
    for i in range(6):
        for j in range(2):
            string = ""
            string+="0x12" if (j%2) else "0x11"
            string += str((i+4)*10)+"  "+WORDS[i*2+j]
            print(string, end='    ')
        print()

def getHint(word, guess):
    hint = ""
    for i in range(len(word)):
        if word[i] == guess[i]:
            hint += word[i]
        else:
            hint += "_"
    return hint

def main():
    while(True):
        print("""
Welcome to the Hacking mini game!
The objective of the game is to find the password in the computer's memory.
You must guess a 7 letter word.
You have 4 guesses.
You can type the guessed word in upper or lower case.
If the letter guessed is in the correct position, you will see the letter in the hint.
If the letter guessed is not in the word, you will see a '_' in the hint.
Try to guess the word with the least amount of guesses.
Press Ctrl+C to quit.
Good luck!
    """)
        printComputerMemory()
        word = random.choice(WORDS)
        correct = False
        for i in range(4):
            print("\nGuesses left:", 4 - i)
            guess = input("Guess a word: ").upper()
            if guess == word:
                correct = True
                break
            else:
                print("Incorrect, try again.")
                print("Here is a hint:")
                print(getHint(word, guess))
                print()
        if correct:
            print("You guessed the correct word!")
            cont = input("Do you want to continue? (y/n): ")
            if cont.lower() == 'n':
                break
            elif cont.lower() == 'y':
                continue
            else:
                print("Invalid input.")
                break
        else:
            print("You ran out of guesses.")
            print("The correct word was", word)
            cont = input("Do you want to continue? (y/n): ")
            if cont.lower() == 'n':
                break
            elif cont.lower() == 'y':
                continue
            else:
                print("Invalid input.")
                break
        print()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()