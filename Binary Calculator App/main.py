from tkinter import *
from tkinter import messagebox

DARK_THEME = '#211522'
ENTRY_COLOR = '#d3b1c2'
TEXT_COLOR = 'white'
SELECT_COLOR = '#2f435a'


class App:
    def __init__(self, master):
        master.title("Binary Calculator", )
        master.columnconfigure(0, weight=1)
        master.rowconfigure(0, weight=1)
        master.resizable(False, False)
        master.geometry('300x250')
        self.menubar = Menu(master, )
        master.config(menu=self.menubar)

        self.entry = Entry(master,background=ENTRY_COLOR)

        self.lstbx1 = Listbox(master,selectbackground=SELECT_COLOR, selectmode=BROWSE, exportselection=0, height=2, background=ENTRY_COLOR)
        self.lstbx2 = Listbox(master,selectbackground=SELECT_COLOR, selectmode=BROWSE, exportselection=0, height=2, background=ENTRY_COLOR)

        for i in ["Binary", "Decimal"]:
            self.lstbx1.insert(END, i)
            self.lstbx2.insert(END, i)

        # set default for convert types
        self.lstbx1.select_set(1)
        self.lstbx2.select_set(0)

        self.result = Text(master, font='Times 17', fg=TEXT_COLOR, background=SELECT_COLOR, width=10, height=2,state=DISABLED)

        # right arrow icon on top
        self.type_to = Label(master, text='➥', font='Times 18', fg='red', background=DARK_THEME)

        # right arrow icon on bottom
        self.result_to = Label(master, text='➭', font='Times 18', fg='red', background=DARK_THEME)

        self.convert_button = Button(master, text="Convert", command=self.convert, background='#228280', fg=TEXT_COLOR,
                                     padx=20, activebackground=ENTRY_COLOR)

        self.layout()

    def layout(self):
        self.lstbx1.grid(row=0, column=0)
        self.type_to.grid(row=0, column=1)
        self.lstbx2.grid(row=0, column=2, padx=5)
        self.entry.grid(row=1, column=0)
        self.result_to.grid(row=1, column=1)
        self.result.grid(row=1, column=2)
        self.convert_button.grid(row=2, column=0, pady=20, padx=5, sticky=W)

    def convert(self):
        try:
            tmp = self.entry.get()
            calc_src = self.lstbx1.curselection()
            calc_dst = self.lstbx2.curselection()
            src = {0: 2, 1: 0, }
            tmp = int(tmp, src[calc_src[0]])

            dst = {0: bin, 1: int}
            tmp = dst[calc_dst[0]](tmp)

            self.result.config(state=NORMAL)
            # check if result box not empty
            if self.result.get(1.0, END):
                # clean the result box
                self.result.delete(1.0, END)
            self.result.insert(END, tmp)
            self.result.config(state=DISABLED)
        except ValueError:
            messagebox.showerror(title="Error", message="cannot convert the specified input")
        except IndexError:
            messagebox.showerror(title="Error", message="Specify the conversion type")


root = Tk()
root.config(background=DARK_THEME)
app = App(root)
root.mainloop()
