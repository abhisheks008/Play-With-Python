# importing the random module
import random
from os import system, name
from time import sleep

#Game with player and the computer

#variables
no_of_die = 5
die_death_values = [2,5]
computer_score = 0
user_score = 0

continue_playing = "yes"

#functions

def clear():
 
    # for windows
    if name == 'nt':
        _ = system('cls')
 
    # for mac and linux
    else:
        _ = system('clear')

def player_play():
    no_of_die_in_turn = no_of_die
    player_score = 0
    
    while no_of_die_in_turn > 0:
        die_death_counter = 0
        turn_score = 0
        die_with_death = False

        print("Die rolled: ", end =" ")
        for i in range(no_of_die_in_turn):
            if no_of_die_in_turn <= 0:
                return player_score
            turn_value = random.randint(1,6)
            if turn_value in die_death_values:
                no_of_die_in_turn -= 1
                die_with_death = True
                die_death_counter += 1
            else:
                turn_score += turn_value

            print(turn_value, end =" ")
            
        if die_with_death == True:
            turn_score = 0
        print("Total Die deaths in this round ",die_death_counter)
        player_score += turn_score

    return player_score
   

while continue_playing == "yes":
    #decide who goes first

    print("Who goes first?")
    #computer
    for i in range(5):
        computer_score += random.randint(1,6)

    for i in range(5):
        user_score += random.randint(1,6)

    if user_score >= computer_score:
        print("You go first!")
        user_score = player_play()
        print("Your Score :",user_score)
        print("\nMy turn")
        computer_score = player_play()
        print("My Score :",computer_score)
    else:
        print("I go first!")
        computer_score = player_play()
        print("My Score :",computer_score)
        print("\nYour turn")
        user_score = player_play()
        print("Your Score :",user_score)

    if computer_score > user_score:
        print("I win!")
    elif user_score == computer_score:
        print("Tie! Up for another round?")
    else:
        print("You win!")
    
    print("Continue playing? (yes/no)")
    continue_playing = input()

    print("\n\n")
    clear()

print("Bye Bye!")
sleep(1)