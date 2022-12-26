import tkinter
import pytesseract  
from tkinter import filedialog
from PIL import Image 

def openFile():
    '''This function opens the directory'''
    # opening files
    filename = filedialog.askopenfilename(title="Open Image",initialdir='C:\Downloads',filetypes=[("PNG","*.png"),("JPG","*.jpg"),("JPEG","*.jpeg"),("ICON","*.ico")])
    file_label.configure(text=filename)
    output_text.delete("1.0", tkinter.END)
    img = Image.open(filename)
    print(img) 
    # path where the tesseract module is installed
    pytesseract.pytesseract.tesseract_cmd ='C:/Program Files/Tesseract-OCR/tesseract.exe'   
    # converts the image to result and saves it into result variable
    result = pytesseract.image_to_string(img)
    output_text.insert(tkinter.END, result)

root = tkinter.Tk()
root.title("Image to Text Converter")

file_label = tkinter.Label(root,text="No image selected")
file_label.pack()
#ouput text widget
output_text = tkinter.Text(root)
output_text.pack()
#button to select the file
open_file_btn = tkinter.Button(root, text="Select Image", command= openFile)
open_file_btn.pack()

root.mainloop()
