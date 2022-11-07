*** ROCK-PAPER-SCISSORS ***

### GOAL

This game aims the player and computer to compete using rock , paper and scissors (elements for game-play)

### DESCRIPTION

The rules to win are as follows: 
    1. Rock beats Scissors
    2. Paper beats Rock
    3. Scissor beats Paper

If player chooses the element that can beat the element selected by computer , player wins!!!

Computer randomly selects the element to play with.


Rules to play 

    1. This game is human VS computer

    2. Select from the three options : 
                i)   ROCK
                ii)  PAPER
                iii) SCISSORS

    3. After every turn , RESET GAME !


### WHAT I HAD DONE

1. Necessary packages have been imported (mentioned next) 
   "root" variable calls for it and geometry and title for the window to appear is specified 
   A dictionary is used for the values from computer can genarate a response each time program runs

2. Functions/methods for every action are defined clearly
    a. Reset : Resets the game -> All the buttons are activated and result is cleared.

    b. Disable Button : All buttons  except selcted button are disabled to avoid multiple entries.

    c.rockPlayer : If player selects ROCK , this functions deals with that case
                    $ If computer plays Scissors --> Player  WINS
                    $ If computer plays Rock --> TIE
                    $ If computer plays Paper --> Player LOSES

    d.paperPlayer : If player selects PAPER , this functions deals with that case
                    $ If computer plays Rock --> Player  WINS
                    $ If computer plays Paper --> TIE
                    $ If computer plays Scissors --> Player LOSES

    e.scissorsPlayer : If player selects SCISSORS , this functions deals with that case
                    $ If computer plays Paper --> Player  WINS
                    $ If computer plays Scissors --> TIE
                    $ If computer plays Rock --> Player LOSES

    f.formatting : defined rock , paper, scissors and reset button with appropiate colours,padding, fonts etc.



### LIBRARIES NEEDED

1. Tkinter Library : Tkinter is the standard GUI library for Python. Python when combined with Tkinter provides a fast and easy way to create GUI applications. Tkinter provides a powerful object-oriented interface to the Tk GUI toolkit.

2. Random Package : Python Random module is an in-built module of Python which is used to generate random numbers. 


### DEMONSTRATION

https://drive.google.com/drive/folders/1LUfug60zkTIcD2704Zle2GSJNP6kF-A7?usp=sharing


### AISHVI GULERIA
 






