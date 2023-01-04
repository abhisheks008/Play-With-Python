#Importing modules
from textblob import TextBlob
from tkinter import *

#Creating the window
wn = Tk()
wn.title("Spell Checker App")
wn.geometry('500x250')
wn.configure(background='SlateGray1')

#Creating the variables to get the word and set the correct word
text=StringVar(wn)
correctedText =StringVar(wn)

#The main label
Label(wn, text='Spell Checker',bg='SlateGray1', fg='gray30', font=('Times', 20,'bold')).place(x=100, y=10)

#Getting the input of word from the user
Label(wn, text='Please enter the word',bg='SlateGray1',font=('calibre',13,'normal'), anchor="e", justify=LEFT).place(x=20, y=70)

Entry(wn,textvariable=text, width=35,font=('calibre',13,'normal')).place(x=20,y=110)

#Label to show the correct word
opLabel = Label(wn, textvariable=correctedText, bg='SlateGray1',anchor="e",font=('calibre',13,'normal'), justify=LEFT).place(x=20, y=140)

#Function to check the spelling
def checkSpelling():
    a = text.get() #Getting the word user entered
    b = TextBlob(a) #Getting the object for the word
    if(a==""):
        Label(wn, text='Please enter a word or sentence',bg='SlateGray1', fg='red', font=('calibre',13,'normal')).place(x=20, y=200)
    elif(a==str(b.correct())):
        Label(wn, text='The given input is already correct',bg='SlateGray1', fg='green', font=('calibre',13,'normal')).place(x=20, y=200)
    else:
        correctedText.set("The corrected word or sentence is: "+str(b.correct())) #Showing the corrected word

#Button to do the spell check
Button(wn, text="Click Me", bg='SlateGray4',font=('calibre', 13),
command=checkSpelling).place(x=20, y=170)

#Runs the window till it is closed by the user
wn.mainloop()

