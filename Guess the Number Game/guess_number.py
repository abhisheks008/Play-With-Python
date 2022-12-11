import random
from tkinter import *  

root = Tk()
root.title("Guess the Number Game")
root.geometry('750x750')
root.config(bg="#3F31F3")

class NumberGuessing:
    #Variables for input values
    num1 = IntVar()
    num2 = IntVar()
    guessedNumber=IntVar()

    #variable for random number
    value=None

    #Function For Checking and generating random no
    def check(self):
        #For empty input
        if self.num1.get()==0 or self.num2.get() == 0 or self.guessedNumber.get() ==0 :
            self.ResultLabel.configure(text="INPUT ALL INPUTS")
        else:
            #Gfnerates a random no
            self.value = random.randint(self.num1.get(), self.num2.get())

            #Condition that checks random no matches guessed no or not
            if self.guessedNumber.get() == self.value:
                self.ResultLabel.configure(text= "You Win 😊")
            else:
                self.ResultLabel.configure(text="You Lose 😞. Number is " + str(self.value))

    #this runs first when a class is called
    def __init__(self):


        #Fonts for label and entry boxes
        self.lfont = ('Comic Sans MS',22)

        #creating some space for centering the content
        self.EmptyLabel= Label(root, text="                 ", font=self.lfont, background="#3F31F3")
        self.EmptyLabel.grid(row=0, column=0, columnspan=2, pady=10, padx=5)
        
        #displaying "range start"
        self.Label1= Label(root, text="RANGE START 🔼", font=self.lfont, foreground="#CDE927", background="#3F31F3")
        self.Label1.grid(row=0, column=2, sticky=N,columnspan=2, padx=5, pady=5)


        #Field for input
        self.entry1= Entry(root, textvariable=self.num1, font=self.lfont, foreground="blue")
        self.entry1.grid(row=1, column=2, padx=5, pady=5)

        #displaying "range end"
        self.Label2= Label(root, text="RANGE END 🔽", font=self.lfont, foreground="#CDE927", background="#3F31F3")
        self.Label2.grid(row=3, column=2, sticky=N, columnspan=2, padx=5, pady=5)

        #Field for input
        self.entry2= Entry(root, textvariable=self.num2, font=self.lfont, foreground="blue")
        self.entry2.grid(row=4, column=2, padx=5, pady=5)

        #displaying "enter your number"
        self.Label3= Label(root, text="ENTER YOUR NUMBER ✏️", font=self.lfont, foreground="#CDE927", background="#3F31F3")
        self.Label3.grid(row=6,column=2, columnspan=2, pady=10)

        #Field for input
        self.entry3= Entry(root, textvariable=self.guessedNumber, font=self.lfont, foreground="darkorchid")
        self.entry3.grid(row=7,column=2, columnspan=2, pady=10, padx=5)

        #Button that checks value
        self.btn = Button(root, text="Check", font=self.lfont, foreground="white",background="#DC1632", command=self.check)
        self.btn.grid(row=10,column=2, columnspan=2,sticky=N, pady=10,)

        #displaing result
        self.ResultLabel= Label(root, text="", font=self.lfont, foreground="#42F046", background="#3F31F3")
        self.ResultLabel.grid(row=8,column=2, columnspan=2, pady=10, padx=5)


        root.mainloop()

#calling the class
NumberGuessing()