from tkinter import *
from tkinter import filedialog
import csv
import json

root = Tk()
root.title("CSV to JSON Converter")
root.geometry('500x500')

def selectCSV():
    data = []
    csv_file_path = filedialog.askopenfilename()
    # Ask user for the name to save the file as
    userfilename = filedialog.asksaveasfilename()
    with open(csv_file_path, encoding='utf-8') as csvfile:
        csvReader = csv.DictReader(csvfile)
        for rows in csvReader:
            data.append(rows)
    with open(userfilename, 'w', encoding='utf-8') as jsonfile:
        
        jsonfile.write(json.dumps(data,indent=4))
    
    status["text"] = "Finished"

title_label = Label(root, text = "CSV to JSON Converter",font=("Arial", 18) )
title_label.pack()

button1 = Button(root, text="Select CSV file", command= selectCSV)
button1.pack()

status = Label(root, text = "", font=("Arial", 18))
status.pack()

root.mainloop()
