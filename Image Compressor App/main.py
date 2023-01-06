import os
import tkinter
import pytesseract  
from tkinter import filedialog
from PIL import Image 

def openImage():
    '''This function opens the directory'''
    # opening image
    filename = filedialog.askopenfilename(title="Select Image",initialdir='C:\Downloads',filetypes=[("PNG","*.png"),("JPG","*.jpg"),("JPEG","*.jpeg"),("ICON","*.ico")])
    file_label.configure(text=filename)
    output_text.delete("1.0", tkinter.END)
    userfilename = filedialog.asksaveasfilename()
    userfilename = os.path.basename('/root/'+userfilename)
    # userfilename = os.path.splitext(userfilename)[0]
    print("user file name :",userfilename)
    # open the image
    picture = Image.open(filename)
	
	  # Save the picture with desired quality
    # To change the quality of image,set the quality variable at your desired level
    # The more the value of quality variable and lesser the compression
    picture.save("Compressed_"+userfilename+'.jpeg',
				"JPEG",
				optimize = True,
				quality = 10)
    output_text.insert(tkinter.END, "Image compression finished")

root = tkinter.Tk()
root.title("Image Compressor")

file_label = tkinter.Label(root,text="No image selected")
file_label.pack()
#ouput text widget
output_text = tkinter.Text(root)
output_text.pack()
#button to select the file
open_file_btn = tkinter.Button(root, text="Select Image", command= openImage)
open_file_btn.pack()

root.mainloop()
