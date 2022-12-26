from tkinter import *
import indian_names

root = Tk()
root.title("Random Name Generator")
root.geometry('500x500')

#Creating labels
l0 = Label(root, text = "Random Name Generator", font=("Arial",20))
l0.pack()
l1 = Label(root, text = "Enter the gender", font=("Arial", 16))
l1.pack()
input = StringVar()
l2 = Entry(root, textvariable = input, font=("Arial", 16))
l2.pack()

def getName():
    l3['text'] = " "
    gender = input.get().lower()
    if gender == "male" : 
        l3['text'] = indian_names.get_full_name(gender='male')
    elif gender == 'female':
        l3['text'] = indian_names.get_full_name(gender='female')
    else :
        l3['text'] = indian_names.get_full_name(gender='female')

button = Button(root, text = "Get Name", command = getName, bg = "#50e3a4", fg = 'black', font=("Arial", 10))
button.pack()
l3 = Label(root, text = "", font=("Arial",16))
l3.pack()

root.mainloop()
