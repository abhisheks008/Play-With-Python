from tkinter import *


root = Tk()
root.title('Weight Converter')

#Creating labels
l1 = Label(root, text = "Enter the weight in Kg", font=("Arial", 18))
input = StringVar()
l2 = Entry(root, textvariable = input, font=("Arial", 18))
l3 = Label(root, text = "Gram", font=("Arial", 18))
l4 = Label(root, text = "Pounds", font=("Arial", 18))
l5 = Label(root, text = "Ounce", font=("Arial", 18))
#Text widgets for output
t1_gram = Text(root, height = 1, width = 20,font=("Arial", 18))
t2_pounds = Text(root, height = 1, width = 20, font=("Arial", 18))
t3_ounce = Text(root, height = 1, width = 20, font=("Arial", 18))

def convert():
    # convert kg to gram
    gram = float(input.get())*1000
     
    # convert kg to pound
    pound = float(input.get())*2.20462
     
    # convert kg to ounce
    ounce = float(input.get())*35.274
     
    # Enters the converted weight to
    # the text widget
    t1_gram.delete("1.0", END)
    t1_gram.insert(END,gram)
     
    t2_pounds.delete("1.0", END)
    t2_pounds.insert(END,pound)
     
    t3_ounce.delete("1.0", END)
    t3_ounce.insert(END,ounce)
#button
button = Button(root, text = "Convert", command = convert, bg = "#50e3a4", fg = 'white', font=("Arial", 18))
#positioning the labels and Text widgets
l1.grid(row = 0, column = 0)
l2.grid(row=0, column=1)
l3.grid(row=2, column=0)
l4.grid(row=2, column=1)
l5.grid(row=2, column=2)
t1_gram.grid(row=3, column=0)
t2_pounds.grid(row=3, column=1)
t3_ounce.grid(row=3, column=2)
button.grid(row=1, column = 1)


root.mainloop()
