# importing the random module
import random
import tkinter
from os import system, name
from time import sleep

#Game with player and the computer

#variables
no_of_die = 5
die_death_values = [2,5]
player_score = 0
computer_score = 0
button_press = False
no_of_die_in_turn = no_of_die
turn_rolls =[]
no_of_rolls_in_turn = 0
#functions
def common_data(list1, list2):
    global no_of_die_in_turn
    result = False
  
    for x in list1:
        for y in list2:
            if x == y:
                result = True
                no_of_die_in_turn -= 1
    return result

def roll():
    #end game
    global no_of_rolls_in_turn
    global turn_rolls
    global die_death_values
    global player_score
    global computer_score
    global no_of_die_in_turn
    g_canvas.update()
    h = g_canvas.winfo_height()/2
    w = g_canvas.winfo_width()/2
    s = "My Score :" + str(computer_score)
    g_canvas.create_text(w, 10 , text=s, fill="skyblue", font=('Helvetica 15 bold'))
    print(no_of_die_in_turn)
    if no_of_die_in_turn == 0:
        g_canvas.delete("all")
        h = int(g_canvas.winfo_height()/2)
        w = int(g_canvas.winfo_width()/2)
        print(computer_score,player_score,w,h)
        if computer_score > player_score: 
            print("I win")
            g_canvas.create_text(w, 100,text="I win!", fill="skyblue", font=('Helvetica 15 bold'))
        elif player_score == computer_score: 
            print("Tie win")
            g_canvas.create_text(w, 100,text="Tie! Up for another round?", fill="skyblue", font=('Helvetica 15 bold'))
        else: 
            print("You win")
            g_canvas.create_text(w, 100,text="You win!", fill="skyblue", font=('Helvetica 15 bold'))
        s_button.configure(text="Restart?")
        roll_button.pack_forget()
        s_button.pack(side="bottom")
        return
    #if all die in turn rolled
    if no_of_rolls_in_turn == no_of_die_in_turn:
        g_canvas.delete("all")
        no_of_rolls_in_turn = 0#reset for next turn
        turn_score = 0
        if common_data(turn_rolls,die_death_values) == False:
            #to check if this turn had 2 or 5 rolled then don't add values
            for i in turn_rolls:
                turn_score += i
            player_score += turn_score
        s = "Turn Score is: " + str(turn_score)
        g_canvas.create_text(w, (h * 2) - 50 ,text=s, fill="skyblue", font=('Helvetica 15 bold'))
        s = "Your Score:" + str(player_score)
        g_canvas.create_text(w, (h*2) - 20, text=s, fill="skyblue", font=('Helvetica 15 bold'))  
        turn_rolls = []
        return
    temp = random.randint(1,6)
    g_canvas.create_rectangle(w-50,h-50, w+ 50, h+ 50, fill="red")
    g_canvas.create_text(w, h,text=str(temp), fill="white", font=('Helvetica 15 bold'))
    no_of_rolls_in_turn += 1
    turn_rolls.append(temp)


def computer_play():
    no_of_die_in_turn = no_of_die
    computer_score = 0
    
    while no_of_die_in_turn > 0:
        die_death_counter = 0
        turn_score = 0
        die_with_death = False
        print("Die rolled: ", end =" ")
        for i in range(no_of_die_in_turn):
            if no_of_die_in_turn <= 0:
                return computer_score
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
        computer_score += turn_score
        
    no_of_die_in_turn = no_of_die
    turn_rolls =[]
    no_of_rolls_in_turn = 0
    return computer_score
   
def start():
    global no_of_rolls_in_turn
    global turn_rolls
    global player_score
    global computer_score
    global no_of_die_in_turn
    no_of_die_in_turn = no_of_die
    no_of_rolls_in_turn = 0
    turn_rolls = []
    player_score = 0
    computer_score = 0
    g_canvas.delete("all")
    s_button.configure(text="Start?")
    s_button.pack_forget()
    changeButton()
    g_canvas.update()
    can_h = g_canvas.winfo_height()/2
    can_w = g_canvas.winfo_width()/2 
    #computer goes first
    
    g_canvas.create_text(can_w, can_h - 20, text="I go first!", fill="skyblue", font=('Helvetica 15 bold'))
    computer_score = computer_play()
    g_canvas.create_text(can_w, (can_h*2) - 20, text="Your Score: 0", fill="skyblue", font=('Helvetica 15 bold'))

#GUI
g_window = tkinter.Tk()
g_window['bg'] = '#ffff99'
frame = tkinter.Frame(g_window)
button_frame = tkinter.Frame(frame)
g_window.title("Dice With Death")
g_canvas = tkinter.Canvas(frame, width=1700, height=536, bg="#ffff99")
s_button = tkinter.Button(frame, text='Start', width=25,command=start)
roll_button = tkinter.Button(frame, text='Roll', width=25,command=roll)

def changeButton():
    roll_button.pack(side="bottom")


s_button.pack(side="bottom")
g_canvas.pack(side="top")
w = g_canvas.winfo_width() 
g_canvas.create_text(800,20, text="Dice With Death", fill="skyblue", font=('Helvetica 15 bold'))

frame.pack()
g_window.mainloop()