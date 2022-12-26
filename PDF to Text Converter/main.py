import tkinter, PyPDF2
from tkinter import filedialog

def openFile():
    '''This function opens the directory'''
    filename = filedialog.askopenfilename(title="Open PDF",initialdir='C:\Downloads',filetypes=[('PDF files','*.pdf')])
    file_label.configure(text=filename)
    output_text.delete("1.0", tkinter.END)
    reader = PyPDF2.PdfReader(filename)
    for i in range(reader.numPages):
        text = reader.getPage(i).extractText()
        output_text.insert(tkinter.END, text)

root = tkinter.Tk()
root.title("PDF to Text Converter")

file_label = tkinter.Label(root,text="No file selected")
file_label.pack()
#ouput text widget
output_text = tkinter.Text(root)
output_text.pack()
#button to select the file
open_file_btn = tkinter.Button(root, text="Open PDF", command= openFile)
open_file_btn.pack()

root.mainloop()
