import pyqrcode
import tkinter as tk
from tkinter import *
from tkinter import messagebox

tk=Tk()
tk.title("QRCODE generator")

def generate_QR():
  if len(user_input.get())!=0:
    global qr,img
    qr = pyqrcode.create("url:" + user_input.get())
    img=BitmapImage(data=qr.xbm(scale=8))
    
  else:
    messagebox.showwarning('warning',"filelds are required!")

  try:
    display_code()
  except:
    pass

def display_code():
  img_lbl.config(image=img)
  output.config(text="QR code : "+user_input.get())

lbl = Label(tk,text="Enter your text",bg="#A555EC",padx=30,pady=30,font=("ariel",30))
lbl.pack()

user_input =StringVar()
entry=Entry(tk,textvariable=user_input,width=50,font=("ariel",15))
entry.pack(padx=50,pady=20)

button = Button(tk,text="generate QR",width=20,command=generate_QR,font=("ariel",15))
button.pack()

img_lbl=Label(tk,bg="#e6e6e6")
img_lbl.pack()

output=Label(tk,text="",bg="#F25252",pady=4)
output.pack()

tk.mainloop()