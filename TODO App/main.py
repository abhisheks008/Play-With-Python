from tkinter.font import Font as f
from tkinter import *


root = Tk()
root.geometry('500x500')
root.title('TODO App')

my_font = f(
    family = "Arial",
    size = 16,
    weight = "bold"
)

my_frame = Frame(root)
my_frame.pack(pady=10)

my_list = Listbox(
    my_frame,
    font = my_font,
    width = 25,
    height = 5,
    bg = "#deecec",
    bd = 0,
    fg = "#464646",
    selectbackground ="#c8a2d6",
    highlightthickness = 0 ,
    activestyle = "none"
)
my_list.pack(side = LEFT, fill = BOTH)
dummy_list = ["Fast API", "TKinter", "Python", "Open Source"]
for item in dummy_list : 
    my_list.insert(END, item)



my_scrollbar = Scrollbar(my_frame)
my_scrollbar.pack(side = RIGHT, fill = BOTH)

my_list.config(yscrollcommand=my_scrollbar.set)
my_scrollbar.config(command=my_list.yview)

# creating entry box
my_entry = Entry(root,font=("Arial", 20))
my_entry.pack(pady = 20)
# buttons frame
button_frame = Frame(root)
button_frame.pack(pady = 20)

# button functions
def add_item():
    new_item = my_entry.get()
    if len(new_item) >=1 :
        my_list.insert(END, my_entry.get())  
    my_entry.delete(0, END)
def delete_item():
    my_list.delete(ANCHOR)


# adding buttons
dlt_button = Button(button_frame, text = "Delete", command = delete_item, bg = "#fb6b6c", fg = 'white')
add_button = Button(button_frame,width=5, text = "Add", command = add_item, bg="#50e3a4", fg = 'white')
bfont = f(family='Arial', weight = 'bold', size = 14)
dlt_button['font'] = bfont
add_button['font'] = bfont
dlt_button.grid(row = 0, column = 1, padx = 20)
add_button.grid(row = 0, column =0)


root.mainloop()
