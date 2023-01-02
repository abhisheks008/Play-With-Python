import os
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import pytube
# if you get an error here, run this command in terminal: pip install pytube

def downloadVideo():
    if(entry1.get() == "" or entry2.get() == "" or entry3.get() == "" or entry4.get() == ""):
        messagebox.showerror("Error", "Please fill all the fields.")
        return

    url = entry1.get()
    path = entry2.get()
    name = entry3.get()
    resolution = entry4.get()

    if(resolution != "360p" and resolution != "720p" and resolution != "1080p"):
        messagebox.showerror("Error", "Please enter a valid resolution.")
        return

    if(os.path.exists(path) == False):
        messagebox.showerror("Error", "Please enter a valid path.")
        return

    if(os.path.exists(path + "\\" + name + ".mp4") == True):
        messagebox.showerror("Error", "File already exists.")
        return

    try:
        yt = pytube.YouTube(url)
        video = yt.streams.filter(res=resolution).first()
        video.download(path, name)
        messagebox.showinfo("Success", "Video downloaded successfully.")
    except:
        messagebox.showerror("Error", "Please enter a valid url.")
    
window = tk.Tk()
window.title("Youtube Downloader")
window.geometry("600x400")
window.resizable(False, False)

label1 = tk.Label(window, text="Youtube Downloader", font=("Arial", 20))
label1.pack()

label2 = tk.Label(window, text="Enter the url of the video: ", font=("Arial", 10))
label2.pack()

entry1 = tk.Entry(window, width=50)
entry1.pack()

label3 = tk.Label(window, text="Enter the path where you want to save the video: ", font=("Arial", 10))
label3.pack()

entry2 = tk.Entry(window, width=50)
entry2.pack()

button1 = tk.Button(window, text="Browse", command=lambda: entry2.insert(0, filedialog.askdirectory()))
button1.pack()

label4 = tk.Label(window, text="Enter the name of the video: (with extension)", font=("Arial", 10))
label4.pack()

entry3 = tk.Entry(window, width=50)
entry3.pack()

label5 = tk.Label(window, text="Enter the resolution of the video (360p, 720p, 1080p): ", font=("Arial", 10))
label5.pack()

entry4 = tk.Entry(window, width=50)
entry4.pack()

button2 = tk.Button(window, text="Download", command=downloadVideo)
button2.pack()

window.mainloop()
