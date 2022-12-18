# Import Module
from tkinter import *
from tkinter.filedialog import askopenfilenames
import img2pdf
from PIL import Image
  
# Create Object
root = Tk() 
# set Geometry
root.geometry('400x200')
  
def select_file():
    global file_names
    file_names = askopenfilenames(initialdir = "/",
                                  title = "Select File")
  
# IMAGE TO PDF
def image_to_pdf():
    for index, file_name in enumerate(file_names):
        with open(f"file {index}.pdf", "wb") as f:
            image = Image.open(file_name)
            pdf_bytes = img2pdf.convert(image.filename)
            f.write(img2pdf.convert(image.filename))
            image.close()
            f.close()
            print('Converted')
  
  
# Add Labels and Buttons
Label(root, text = "IMG TO PDF",
      font = "italic 15 bold").pack(pady = 10)
  
Button(root, text = "Select Image",
       command = select_file, font = 14).pack(pady = 10)
  
frame = Frame()
frame.pack(pady = 20)
  
Button(frame, text = "Image to PDF",
       command = image_to_pdf,
       relief = "solid",
       bg = "white", font = 15).pack(side = LEFT, padx = 10)
  
  
# Execute Tkinter
root.mainloop()