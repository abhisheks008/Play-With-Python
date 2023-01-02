import random
import tkinter as tk
from tkinter import messagebox

def passwordGenerator():
    if(entry1.get() == "" or entry2.get() == "" or entry3.get() == "" or entry4.get() == "" or entry5.get() == ""):
        messagebox.showerror("Error", "Please fill all the fields.")
        return
    elif((entry2.get() != 'y' and entry2.get() != 'Y' and entry2.get() != 'n' and entry2.get() != 'N') or (entry3.get() != 'y' and entry3.get() != 'Y' and entry3.get() != 'n' and entry3.get() != 'N') or (entry4.get() != 'y' and entry4.get() != 'Y' and entry4.get() != 'n' and entry4.get() != 'N') or (entry5.get() != 'y' and entry5.get() != 'Y' and entry5.get() != 'n' and entry5.get() != 'N')):
        messagebox.showerror("Error", "Please enter 'y' or 'n' for yes or no questions respectively.")
        return

    length = int(entry1.get())
    ch = entry2.get()
    lowerAlphabets = entry3.get()
    upperAlphabets = entry4.get()
    numbers = entry5.get()
    password = ""

    if ch == 'y' or ch == 'Y':
        password += "!@#$%^&*()_+"
    if lowerAlphabets == 'y' or lowerAlphabets == 'Y':
        password += "abcdefghijklmnopqrstuvwxyz"
    if upperAlphabets == 'y' or upperAlphabets == 'Y':
        password += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if numbers == 'y' or numbers == 'Y':
        password += "0123456789"

    passwordGenerated = ""
    for i in range(length):
        passwordGenerated += random.choice(password)
    messagebox.showinfo("Password Generator", "Your password is: " + passwordGenerated)

window = tk.Tk()
window.title("Password Generator")
window.geometry("600x400")
window.resizable(False, False)

label1 = tk.Label(window, text="Password Generator", font=("Arial", 20))
label1.pack()

label2 = tk.Label(window, text="------------------", font=("Arial", 20))
label2.pack()

label3 = tk.Label(window, text="For yes or no questions, enter 'y' or 'n' respectively. (Case insensitive)", font=("Arial", 10))
label3.pack()

label4 = tk.Label(window, text="Enter the length of password: ", font=("Arial", 10))
label4.pack()

entry1 = tk.Entry(window, width=10)
entry1.pack()

label5 = tk.Label(window, text="Do you want to include special characters? (y/n): ", font=("Arial", 10))
label5.pack()

entry2 = tk.Entry(window, width=10)
entry2.pack()

label6 = tk.Label(window, text="Do you want to include lower case alphabets? (y/n): ", font=("Arial", 10))
label6.pack()

entry3 = tk.Entry(window, width=10)
entry3.pack()

label7 = tk.Label(window, text="Do you want to include upper case alphabets? (y/n): ", font=("Arial", 10))
label7.pack()

entry4 = tk.Entry(window, width=10)
entry4.pack()

label8 = tk.Label(window, text="Do you want to include numbers? (y/n): ", font=("Arial", 10))
label8.pack()

entry5 = tk.Entry(window, width=10)
entry5.pack()

button1 = tk.Button(window, text="Generate Password", command=passwordGenerator)
button1.pack()

window.mainloop()
