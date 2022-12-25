# python program to download pdf from url with GUI

import requests
import tkinter as tk

# GUI

def input_data():
    name = textfield.get()
    url = name
    r = requests.get(url, stream=True)
    # download_data
    # You need to add the downloading path here
    with open('/Users/govindkushwaha/Programming/Python/Pdf Downloader/myfile-new.pdf', 'wb') as f:
            f.write(r.content)


root = tk.Tk()
root.geometry("1000x800")
root.title("PDF Downloader")
f = ("poppins", 25, "bold")

# For importing the image
# NOTE:-If image is not visible then add the (logo.png) image path from the image folder
banner = tk.PhotoImage(file="/Users/govindkushwaha/Programming/Python/Pdf Downloader/image/logo.png")
bannerlabel = tk.Label(root, image=banner)
bannerlabel.pack()

# creating text box
textfield = tk.Entry(root, width = 50)
textfield.pack()

# get data button
gbtn = tk.Button(root, text="Download", font=f, relief='solid', command=input_data)
gbtn.pack()

root.mainloop()
