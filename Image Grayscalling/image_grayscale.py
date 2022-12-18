#Importing all the necessary modules
import tkinter as tk
from tkinter import filedialog
from tkinter.filedialog import askopenfile

import PIL
from PIL import Image, ImageTk

import cv2

#Setting up our gui
gui = tk.Tk()
# Size of the window 
gui.geometry("410x400")
gui.title('Image Grayscalling 📷')
gui.config(background="#FFB8A7")
my_font1=('Times New Roman', 18, 'italic')

#Function to save the image, handler pointing to grayscale image is passed
def savefile(imag):
    filename = filedialog.asksaveasfile(mode='wb', defaultextension=".png")
    if not filename:
        return
    imag.save(filename)

#Function to take input of image via file upload and convert it into grayscale
def uploadFile():
    # type of files to select 
    f_types = [('PNG Files','*.png'),
    ('Jpg Files', '*.jpg')]
    f = tk.filedialog.askopenfilename(multiple=False,filetypes=f_types)
    col=1 # start from column 1
    row=3 # start from row 3 

    #Reading the image from location
    img = cv2.imread(f)

    #with help of cv2.cvtColor() converting the image to grayscale
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #Since return type of above is a numpy array, so using Pillow to convert to image
    imagePIL = PIL.Image.fromarray(gray_img)
    #Making the copy of image, it will be used in saving to save the grayscale image with original dimension
    duplicate = imagePIL.copy()

    #Resizing image to display in gui
    imagePIL.thumbnail((400,250))
    img = ImageTk.PhotoImage(image = imagePIL)

    #creating a label to display the image
    Img =tk.Label(gui)
    Img.grid(row=row,column=col)
    # keep a reference! by attaching it to a widget attribute
    Img.image = img 
    # Show Image
    Img['image']=img

    # start new line after third column   
    if(col==3):
        # start wtih next row 
        row=row+1
        # start with first column
        col=1 
    # within the same row 
    else:
        # increase to next column
        col=col+1 
    
    #Calling the save function to save the file
    button = tk.Button(gui, text="Download🔽", command=lambda:savefile(duplicate), background="#CAF4F4")
    button.grid(row=10, column=1, columnspan=4)

#Creating some empty space initially
Empty = tk.Label(gui,text='',width=30,font=my_font1, background="#FFB8A7")  
Empty.grid(row=1,column=1,columnspan=4)

#Button to take image via file upload
b1 = tk.Button(gui, text='Upload Image⬆️', 
   width=20,command = lambda:uploadFile(), background="#CAF4F4")
b1.grid(row=2,column=1,columnspan=4)
#calling the function while clicking the button


gui.mainloop()  # Keep the window open