from tkinter import *
import sys
from tkinter.ttk import *
import time

health=100

inventory = []

monster=[]

rooms = {

            'Hall' : {'south' : 'Kitchen',
                  'east'  : 'Dining Room',
                  "north":"Bed Room",
                  'item'  : 'shotgun',
                  'monster'  : '', "desc":"No one has been here for a while",
                },        

            'Kitchen' : { 'north' : 'Hall',
                  "item":"golden_crown",
                  'monster'  : 'zombie',"desc":"Dead bodies scatter the floor",                        
                },
                
            'Dining Room' : { 'west'  : 'Hall',
                  'south' : 'Garden',
                  'item'  : 'key',
                  'monster'  : 'zombie',"desc":"Old painting hangs on the wall",    
                },
                
            'Garden' : { 'north' : 'Dining Room',
            'monster'  : '', "desc": "There is a locked gate here",
                },

        'Bed Room' : {'south' : 'Hall',
            'item'  : 'bandage',
            'monster'  : 'ghoul',"desc":"There is blood all over the bed ",  
              },        
         }

currentRoom = 'Hall'


def welcome():
    label = Label(window, text="Welcome to the Haunted House!")
    label.pack()

def show_instructions():
     instructions=Message(new_window,text='''  
Commands:
  use [item] eg: use key 
  
  shoot[enemy] eg: shoot zombie
   
  go [direction] eg: go north
  
  get [object] eg: get bandage
''')
     instructions.pack()

def showStatus():
  health_bar['value']=health
  window.update_idletasks()
  health_bar.pack()
  location_label=Label(window,text='You are in the ' + currentRoom)
  location_label.pack()
  desc_label=Label(window,text=rooms[currentRoom]['desc'])
  desc_label.pack()
  inventory_label=Label(window,text=f"Inventory : {str(inventory)}")
  inventory_label.pack()
  if "item" in rooms[currentRoom]:
    message_label=Label(window,text=f"You see a {rooms[currentRoom]['item']}")
    message_label.pack()

def game(move):
    global currentRoom
    global inventory
    global health
    
    if move[0]=="shoot":  
      if "monster"in rooms[currentRoom] and move[1] in rooms[currentRoom]['monster'] and "shotgun" in inventory :
          del rooms[currentRoom]['monster']
          message_label=Label(window,text=f"you killed the {move[1]}")
          message_label.pack()
          rooms[currentRoom].update({"monster":"dead"},)
        
      else:
          message_label=Label(window,text="you cannot attack " )
          message_label.pack()

    if move[0]=="exit":
       time.sleep(1)
       sys.exit()   

    if move[0]=="use":
      
      
      if "bandage" in inventory and move[1]== "bandage":
          heal=40
          health=min(100,health+heal)
          inventory.remove("bandage")
          message_label=Label(window,text="you recovered 40 health (max 100)")
          message_label.pack()

      elif "key" in inventory and move[1]== "key" and "golden_crown" in inventory and currentRoom=="Garden":     
         message_label=Label(window,text="you escape with the loot, you retire in style, you win!!  ")
         message_label.pack()
         #here the program doesn't display the message it exits after 1 second
         time.sleep(1)
         sys.exit()   
              
          
      elif "key" in inventory and move[1]== "key" in inventory and currentRoom=="Garden":
         message_label=Label(window,text="you escape the house but die a pauper, you lose ")
         message_label.pack()
         #here the program doesn't display the message it exits after 1 second
         time.sleep(1)
         sys.exit()

      

      else:
          message_label=Label(window,text="can't use that")
          message_label.pack()

      
    
    if move[0] == 'go':
      if move[1] in rooms[currentRoom]:
          currentRoom = rooms[currentRoom][move[1]]
      else:
          message_label=Label(window,text=r"You can\'t go that way!")
          message_label.pack()

    if move[0] == 'get' :
          
      if 'item' in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
          inventory += [move[1]]
          message_label=Label(window,text=f"{move[1]} got!")
          message_label.pack()
          del rooms[currentRoom]['item']
     
      else:
          message_label=Label(window,text=r"Can\'t get that")
          message_label.pack()
        
    if 'zombie' in rooms[currentRoom]['monster']:
      message_label=Label(window,text="A zombie attack you !!!")
      message_label.pack()
      health=health-30

    if 'ghoul' in rooms[currentRoom]['monster']:
      message_label=Label(window,text='A ghoul attack you !!!')
      message_label.pack()
      health=health-20

    if health<0:
      message_label=Label(window,text="you are dead")
      message_label.pack()
  
def get_input():
   showStatus()
   input=Entry(window,width=25)
   input.pack()
   submit_Button=Button(window,text="Submit", command=lambda:submit(input))
   submit_Button.pack()

def submit(input):
   move = input.get().lower().split()
   if input.get():
      game(move)
   else:
      Error_Lab=Label(window,text="Please Enter something")
      Error_Lab.pack()
   get_input()

window=Tk()
window.title("Haunted House Game")
window.geometry('500x500')

new_window=Toplevel(window)
new_window.title("Commands")

#tried to create a scrollbar but it did not work

#frame-Frame(window)
# frame.pack(,fill=BOTH)

# canvas = Canvas(frame,yscrollcommand=scrollbar.set)
# canvas.pack(fill=BOTH, expand=True)

# scrollbar.config(command=canvas.yview)


health_bar= Progressbar(window, orient = HORIZONTAL, length = 100, mode = 'determinate')
                        
welcome()

show_instructions()

health_meter=Label(window,text="Your Health")

health_meter.pack()

get_input()

window.mainloop()
