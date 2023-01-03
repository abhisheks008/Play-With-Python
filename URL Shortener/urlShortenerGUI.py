# Create a gui based application to shorten a url

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import pyshorteners
# If you get an error, try installing pyshorteners using pip

# Create instance
win = tk.Tk()

# Add a title
win.title("URL Shortener")

# Disable resizing the GUI
win.resizable(0, 0)

# Creating a tkinter container
frame = ttk.LabelFrame(win, text=' Enter URL ')

# Set the padding of the container
frame.grid(padx=20, pady=20)

# Creating a tkinter entry box
url = tk.StringVar()

# Creating a tkinter label
label = ttk.Label(frame, text='Enter URL: ')

# Creating a tkinter entry box
entry = ttk.Entry(frame, width=50, textvariable=url)

# Creating a tkinter button
button = ttk.Button(frame, text='Shorten')

# Creating a tkinter label
label2 = ttk.Label(frame, text='Shortened URL: ')

# Creating a tkinter entry box
entry2 = ttk.Entry(frame, width=50)

# Function to shorten the url
def shorten():
    # Get the url from the entry box
    url = entry.get()

    # Shorten the url
    shortener = pyshorteners.Shortener()
    short_url = shortener.tinyurl.short(url)

    # Set the shortened url in the entry box
    entry2.delete(0, 'end')
    entry2.insert(0, short_url)

# Function to copy the shortened url
def copy():
    # Copy the shortened url
    win.clipboard_clear()
    win.clipboard_append(entry2.get())

    # Display a message
    messagebox.showinfo('URL Shortener', 'URL copied to clipboard')

# Function to clear the entry boxes
def clear():
    # Clear the entry boxes
    entry.delete(0, 'end')
    entry2.delete(0, 'end')

# Bind the button to the function
button.config(command=shorten)

# Creating a tkinter button
button2 = ttk.Button(frame, text='Copy')

# Bind the button to the function
button2.config(command=copy)

# Creating a tkinter button
button3 = ttk.Button(frame, text='Clear')

# Bind the button to the function
button3.config(command=clear)

# Place the label
label.grid(row=0, column=0, padx=5, pady=5)

# Place the entry box
entry.grid(row=0, column=1, padx=5, pady=5)

# Place the button
button.grid(row=1, column=0, padx=5, pady=5)

# Place the label
label2.grid(row=2, column=0, padx=5, pady=5)

# Place the entry box
entry2.grid(row=2, column=1, padx=5, pady=5)

# Place the button
button2.grid(row=3, column=0, padx=5, pady=5)

# Place the button
button3.grid(row=3, column=1, padx=5, pady=5)

# Start the GUI
win.mainloop()