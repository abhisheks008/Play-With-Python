import tkinter as tk
import requests
from threading import Thread

api = "http://api.quotable.io/random"
quotes = []
quote_number = 0
MAX_QUOTES = 5

#Configuring Screen
screen = tk.Tk()
screen.geometry("900x268")
screen.title("Random Quote Generator")
screen.grid_columnconfigure(0, weight=1)
screen.resizable (False, False)
screen.configure(bg = '#5271E8')


#Functions
def load_quotes():
    global quotes
    print('Loading Quotes. Please Wait a Moment')
    for x in range(MAX_QUOTES):
        random_quote = requests.get(api).json()
        content = random_quote['content']
        author = random_quote['author']
        quote = '"' + content + '"' + "\n\n" + "By " + author
        # print(quote)
        quotes.append(quote)

load_quotes()

def get_random_quote():
    global quote_label
    global quotes
    global quote_number

    quote_label.configure(text=quotes[quote_number])
    quote_number = quote_number + 1
    # print(quote_number)
    if quotes[quote_number] == quotes[-3]:
        thread = Thread(target=load_quotes)
        thread.start()


# UI
quote_label = tk.Label(screen, text="Click to generate new Quote", bg='#C9F4F9',height=6, pady=10, wraplength=800, font=("Times New Roman", 15, 'italic'))
quote_label.grid(row=0,column=0, stick="WE", padx=20, pady=10)

button = tk.Button(text="Generate", command=get_random_quote, bg='#ffffff', font=("Times New Roman", 14))
button.grid(row=1,column=0, stick="WE", padx=20, pady=10)

#Main Loop
screen.mainloop()
