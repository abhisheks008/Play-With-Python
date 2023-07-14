import random
import os
import time
from colorama import init, Fore, Style

# Initialize colorama
init()

# List of words to choose from
words = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon", "mango"]

# ASCII art for hangman stages
hangman_stages = [
    """
       +---+
       |   |
           |
           |
           |
           |
    =======""",
    """
       +---+
       |   |
       O   |
           |
           |
           |
    =======""",
    """
       +---+
       |   |
       O   |
       |   |
           |
           |
    =======""",
    """
       +---+
       |   |
       O   |
      /|   |
           |
           |
    =======""",
    """
       +---+
       |   |
       O   |
      /|\\  |
           |
           |
    =======""",
    """
       +---+
       |   |
       O   |
      /|\\  |
      /    |
           |
    =======""",
    """
       +---+
       |   |
       O   |
      /|\\  |
      / \\  |
           |
    ======="""
]


def select_word():
    """Selects a random word from the list"""
    return random.choice(words)


def clear_screen():
    """Clears the terminal/console screen"""
    os.system('cls' if os.name == 'nt' else 'clear')


def animate(text, delay=0.03):
    """Prints text with animation"""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)


def play_hangman():
    """Main function to play the Hangman game"""
    word = select_word()
    word_letters = set(word)
    guessed_letters = set()
    incorrect_letters = set()
    attempts = len(hangman_stages) - 1  # Number of attempts allowed

    while len(word_letters) > 0 and attempts > 0:
        clear_screen()

        # Display hangman stage
        print(hangman_stages[len(hangman_stages) - attempts - 1])
        print()

        # Display word with hidden letters
        display_word = ''.join([letter if letter in guessed_letters else '-' for letter in word])
        animate(f"{Fore.GREEN}{display_word}{Style.RESET_ALL}")
        print("\n")

        # Display guessed letters
        guessed_str = ' '.join(sorted(guessed_letters))
        animate(f"{Fore.BLUE}Guessed letters: {guessed_str}{Style.RESET_ALL}")
        print("\n")

        # Get user input
        animate(f"{Fore.YELLOW}Enter a letter: {Style.RESET_ALL}", delay=0.01)
        guess = input().lower()

        if len(guess) != 1 or not guess.isalpha():
            animate(f"{Fore.RED}Invalid input. Please enter a single letter.{Style.RESET_ALL}")
            time.sleep(1)
            continue

        if guess in guessed_letters or guess in incorrect_letters:
            animate(f"{Fore.RED}You've already guessed that letter.{Style.RESET_ALL}")
            time.sleep(1)
            continue

        if guess in word_letters:
            word_letters.remove(guess)
            guessed_letters.add(guess)
            animate(f"{Fore.GREEN}Correct!{Style.RESET_ALL}")
            time.sleep(1)
        else:
            incorrect_letters.add(guess)
            attempts -= 1
            animate(f"{Fore.RED}Incorrect!{Style.RESET_ALL}")
            time.sleep(1)

    # Game over
    clear_screen()
    print(hangman_stages[len(hangman_stages) - attempts - 1])
    print()

    if attempts > 0:
        animate(f"{Fore.GREEN}Congratulations! You guessed the word: {word} . YOU SAVED THE HANGMAN🎉{Style.RESET_ALL}.")
    else:
        animate(f"{Fore.RED}Game over! The word was: {word} . HANGMAN IS DEAD😊{Style.RESET_ALL}")


# Start the game
play_hangman()