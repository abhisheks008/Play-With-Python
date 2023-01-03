
import tkinter as tk
import webbrowser

def search():
  query = entry.get()
  webbrowser.open(f"https://www.google.com/search?q={query}")

root = tk.Tk()
root.title("Google Search")
root.geometry('500x500')

heading_label = tk.Label(root, text="Google Search Automation", font="poppins 20 bold")
heading_label.pack()
entry = tk.Entry(root, font="poppins 16")
entry.pack()

button = tk.Button(root, text="Search", command=search)
button.pack()

root.mainloop()
