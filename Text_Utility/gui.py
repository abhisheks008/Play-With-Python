import tkinter as tk
from tkinter import ttk, filedialog, Button
from tkinter.messagebox import showerror

# root window
root = tk.Tk()
root.title('Text Utility')
root.geometry('500x250')
root.resizable(False, False)


def removePunc():
    tf = filedialog.askopenfilename(
        initialdir="../", 
        title="Open Text file", 
        filetypes=(("Text Files", "*.txt"),)
        )
    tf = open(tf)
    path = tf.name
    
    with open(path) as file:
        contents = file.read()
    with open(path,'w') as file2:
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in contents:
            if char not in punctuations:
                analyzed = analyzed + char
        file2.write(analyzed)
    tf.close()    
    

def convertUpper():
    tf = filedialog.askopenfilename(
        initialdir="../", 
        title="Open Text file", 
        filetypes=(("Text Files", "*.txt"),)
        )
    tf = open(tf)
    path = tf.name
    
    with open(path) as file:
        contents = file.read()
    with open(path,'w') as file2:
        analyzed = ""
        for char in contents:
            analyzed = analyzed + char.upper()
        file2.write(analyzed)
    tf.close()    
    

def convertlower():
    tf = filedialog.askopenfilename(
        initialdir="../", 
        title="Open Text file", 
        filetypes=(("Text Files", "*.txt"),)
        )
    tf = open(tf)
    path = tf.name
    
    with open(path) as file:
        contents = file.read()
    with open(path,'w') as file2:
        analyzed = ""
        for char in contents:
            analyzed = analyzed + char.lower()
        file2.write(analyzed)
    tf.close()       
    

def removeextraspace():
    tf = filedialog.askopenfilename(
        initialdir="../", 
        title="Open Text file", 
        filetypes=(("Text Files", "*.txt"),)
        )
    tf = open(tf)
    path = tf.name
    
    with open(path) as file:
        contents = file.read()
    with open(path,'w') as file2:
        analyzed = ""
        for index, char in enumerate(contents):
            # It is for if a extraspace is in the last of the string
            if char == contents[-1]:
                    if not(contents[index] == " "):
                        analyzed = analyzed + char

            elif not(contents[index] == " " and contents[index+1]==" "):                        
                analyzed = analyzed + char
        file2.write(analyzed)
    tf.close()    
    

def removenewline():
    tf = filedialog.askopenfilename(
        initialdir="../", 
        title="Open Text file", 
        filetypes=(("Text Files", "*.txt"),)
        )
    tf = open(tf)
    path = tf.name
    
    with open(path) as file:
        contents = file.read()
    with open(path,'w') as file2:
        analyzed = ""
        for char in contents:
            if char != "\n" and char!="\r":
                analyzed = analyzed + char
            analyzed += ' '
        file2.write(analyzed)
    tf.close()    
    


# frame
frame = ttk.Frame(root)


# field options
options = {'padx': 5, 'pady': 5}


convert_button = ttk.Button(frame, text='Remove Punctuation')
convert_button.grid(column=3, row=0, sticky='W', **options)
convert_button.configure(command=removePunc)



convert_button = ttk.Button(frame, text='Convert Uppercase')
convert_button.grid(column=6, row=0, sticky='W', **options)
convert_button.configure(command=convertUpper)



convert_button = ttk.Button(frame, text='Convert Lowercase')
convert_button.grid(column=9, row=0, sticky='W', **options)
convert_button.configure(command=convertlower)



convert_button = ttk.Button(frame, text='Remove Newline')
convert_button.grid(column=3, row=4, sticky='W', **options)
convert_button.configure(command=removenewline)




convert_button = ttk.Button(frame, text='Remove ExtraSpace')
convert_button.grid(column=6, row=4, sticky='W', **options)
convert_button.configure(command=removeextraspace)




convert_button = ttk.Button(frame, text='Exit')
convert_button.grid(column=9, row=4, sticky='W', **options)
convert_button.configure(command=lambda:root.destroy())



# add padding to the frame and show it
frame.grid(padx=10, pady=10)


# start the app
root.mainloop()