import pyttsx3  # text to speech
import PyPDF2 as pdf  # reading pdf
import tkinter as tk  # GUI
from tkinter import filedialog  # file selection
import threading  # Running both text to speech and GUI simultaneously

# creating tkinter instance and setting up text to speech
root = tk.Tk()
engine = pyttsx3.init()

# speech speed rate - change the value to increase or decrease speech rate
engine.setProperty("rate", 200)

# tkinter variables
stop = tk.BooleanVar()
file = tk.StringVar()


# file selection
def browsefiles():
    filename = filedialog.askopenfilename(
        initialdir="/",
        title="Select a File",
        filetypes=(("PDF files", "*.pdf*"), ("all files", "*.*")),
    )
    chosenfile.configure(text="File Opened: " + filename)
    file.set(filename)


# starting the reading
def start():
    start_page = start_page_b.get()
    if start_page == "":
        start_page = 1
    start_page = int(start_page)
    filename = file.get()
    book = open(filename, "rb")
    reader = pdf.PdfReader(book)
    pages = len(reader.pages)
    for i in range(start_page - 1, pages):
        page = reader.pages[i]
        text = page.extract_text()
        lines = text.splitlines()
        for i in lines:
            engine.say(i)
            if stop.get():
                engine.stop()
                stop.set(False)
                break
            engine.runAndWait()
        break


# to stop the reading
def stopf():
    stop.set(True)


# GUI setup
root.geometry("480x270")
root.title("Audio Book Reader")
root.config(bg="#011627")
title = tk.Label(root, text="Audio Book", font=("Arial", 20), fg="white", bg="#011627")
title.pack(pady=20)
button_explore = tk.Button(root, text="Browse Files", command=browsefiles)
button_explore.pack()
chosenfile = tk.Label(root, text="No file choosen", fg="white", bg="#011627")
chosenfile.pack(pady=(0, 20))
start_page_l = tk.Label(
    root, text="Enter the page number to start from:", fg="white", bg="#011627"
)
start_page_l.pack()
start_page_b = tk.Entry(root)
start_page_b.pack(pady=(0, 20))
start = tk.Button(root, text="START", command=threading.Thread(target=start).start)
start.pack()
stopb = tk.Button(root, text="STOP", command=stopf)
stopb.pack()
root.mainloop()
