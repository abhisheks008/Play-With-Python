**HANGMAN GAME**  

**GOAL**  
This is a classic word game named Hangman.  In this game, the second player will always be the computer, who will pick a word at random and the first player is the user who will guess the word.


**DESCRIPTION**  
The classic word game Hangman. For those of you who are unfamiliar with the rules, you may read all about them [here](http://en.wikipedia.org/wiki/Hangman%20%28game%29).

Some additional rules of the game:

1. A user is allowed 8 guesses. Make sure to remind the user of how many guesses s/he has left after each round. Assume that players will only ever submit one character at a time (A-Z).

2. A user loses a guess only when s/he guesses incorrectly.

3. If the user guesses the same letter twice, do not take away a guess - instead, print a message letting them know they've already guessed that letter and ask them to try again.

4. The game should end when the user constructs the full word or runs out of guesses. If the player runs out of guesses (s/he "loses"), reveal the word to the user when the game ends.

For this problem, you will need the code files hangman.py and words.txt. Be sure to save them in the same directory. Open and run the file hangman.py without making any modifications to it to ensure that everything is set up correctly. By "open and run" I mean do the following:
* Go to your IDE. From the File menu, choose "Open".
* Find the file hangman.py and choose it.
* The template hangman.py file should now be open. Run the file and enjoy the game :-D


**WHAT I HAD DONE**  
In this game, I implemented a function, called hangman, that will start up and carry out an interactive Hangman game between a player and the computer. The game uses a words.txt file that contains all the words and a word will be picked at random by the computer using a random module in the game for the user to guess.

**DEMONSTRATION**  
![Screenshot 2022-12-05 at 7.05.22 PM](https://github.com/aayushsinha0706/Play-With-Python/blob/main/Hangman/images/Screenshot%202022-12-05%20at%207.05.22%20PM.png)
![Screenshot 2022-12-05 at 7.11.06 PM](https://github.com/aayushsinha0706/Play-With-Python/blob/main/Hangman/images/Screenshot%202022-12-05%20at%207.11.06%20PM.png)
![Screenshot 2022-12-05 at 7.11.24 PM](https://github.com/aayushsinha0706/Play-With-Python/blob/main/Hangman/images/Screenshot%202022-12-05%20at%207.11.24%20PM.png)
![Screenshot 2022-12-05 at 7.11.43 PM](https://github.com/aayushsinha0706/Play-With-Python/blob/main/Hangman/images/Screenshot%202022-12-05%20at%207.11.43%20PM.png)
![Screenshot 2022-12-05 at 7.12.43 PM](https://github.com/aayushsinha0706/Play-With-Python/blob/main/Hangman/images/Screenshot%202022-12-05%20at%207.12.43%20PM.png)

Although I lost the game I hope you don't :-D

**AAYUSH SINHA**  
