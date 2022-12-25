from tkinter import *
from tkinter import filedialog
import PyPDF2

pdf2merge=[]
pdfWriter = PyPDF2.PdfFileWriter()

root = Tk()
root.title("PDF Merger")
root.geometry('500x500')

def selectPDF():
    pdf2merge = filedialog.askopenfilenames()
    print(pdf2merge)
    # Ask user for the name to save the file as
    userfilename = filedialog.asksaveasfilename()
    # loop through all PDFs
    for filename in pdf2merge:
        # rb for read binary
        pdfFileObj = open(filename, 'rb')
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
        # Opening each page of the PDF
        for pageNum in range(pdfReader.numPages):
            pageObj = pdfReader.getPage(pageNum)
            pdfWriter.addPage(pageObj)
    # save PDF to file, wb for write binary
    pdfOutput = open(userfilename + '.pdf', 'wb')
    # Outputting the PDF
    pdfWriter.write(pdfOutput)
    # Closing the PDF writer
    pdfOutput.close()
    status["text"] = "Finished"

title_label = Label(root, text = "Merge PDF files",font=("Arial", 18) )
title_label.pack()

button1 = Button(root, text="Select PDF files", command= selectPDF)
button1.pack()

status = Label(root, text = "", font=("Arial", 18))
status.pack()

root.mainloop()
