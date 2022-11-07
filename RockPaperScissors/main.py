
import tkinter  
import random


root = tkinter.Tk() 
root.geometry("600x300") 
root.title("Rock Paper Scissors") 

possible_val = { "0":"Rock", "1":"Paper", "2":"Scissors" } 

 
def reset_game():
    b1["state"] = "active" 
    b2["state"] = "active" 
    b3["state"] = "active" 
    l1.config(text = "Player			 ") 
    l3.config(text = "Computer") 
    l4.config(text = "") 



def rockPlayer():                                   #player selects rock 
    c_v = possible_val[str(random.randint(0,2))] 
    if c_v == "Rock": 
        result = "Tie!" 
    elif c_v=="Scissors": 
        result = "Player Wins" 
    else: 
        result = "Computer Wins" 
    l4.config(text = result) 
    l1.config(text = "Rock		 ") 
    l3.config(text = c_v) 
    button_disable() 


def paperPlayer():                                   #player selects paper
    c_v = possible_val[str(random.randint(0, 2))] 
    if c_v == "Paper": 
        result = "Tie!" 
    elif c_v=="Scissors": 
        result = "Computer Wins" 
    else: 
        result = "Player Wins" 
    l4.config(text = result) 
    l1.config(text = "Paper		") 
    l3.config(text = c_v) 
    button_disable() 


def scissorsPlayer():                                   #player selects scissors 
    c_v = possible_val[str(random.randint(0,2))]         #syntax: randint(start, end)
    if c_v == "Rock": 
        result = "Computer Wins" 
    elif c_v == "Scissors": 
        result = "Tie!" 
    else: 
        result = "Player Wins" 
    l4.config(text = result) 
    l1.config(text = "Scissors		 ") 
    l3.config(text = c_v) 
    button_disable() 
    
#Disable the button 
def button_disable(): 
    b1["state"] = "disable" 
    b2["state"] = "disable" 
    b3["state"] = "disable" 



#formatting
tkinter.Label(root, 
    text = 'Choose any one: Rock, Paper, Scissors', 
    font = "Consolas", 
    fg = "blue").pack(pady = 20)  


frame = tkinter.Frame(root) 
frame.pack() 

l1 = tkinter.Label(frame, 
    text = "Player		 ", 
    font = 10) 

l2 = tkinter.Label(frame, 
    text = "  VS		 ", 
    font = "Consolas") 

l3 = tkinter.Label(frame, text = "Computer", font = 10) 

l1.pack(side = 'left') 
l2.pack(side = 'left') 
l3.pack() 

l4 = tkinter.Label(root, 
        text = "", 
        font = "Consolas", 
        bg = "white", 
        width = 15 , 
        borderwidth = 2, 
        relief = "solid") 
l4.pack(pady = 20) 

frame1 = tkinter.Frame(root) 
frame1.pack() 

b1 = tkinter.Button(frame1, text = "Rock", 
            font = 8, width = 7, bg = "light green", 
            command = rockPlayer) 

b2 = tkinter.Button(frame1, text = "Paper ", 
            font = 8, width = 7, bg = "light green", 
            command = paperPlayer) 

b3 = tkinter.Button(frame1, text = "Scissors", 
            font = 8, width = 7, bg = "light green", 
            command = scissorsPlayer) 

b1.pack(side = 'left', padx = 10) 
b2.pack(side = 'left', padx = 10) 
b3.pack(padx = 10) 

tkinter.Button(root, text = "Reset Game", 
        font = 10, fg = "red", 
        bg = "yellow", command = reset_game).pack(pady = 20) 

#Execute Tkinter 
root.mainloop() 
