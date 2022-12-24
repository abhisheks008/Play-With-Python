from tkinter import *
from tkinter import messagebox

# This function clears all the details entered and set them to 0 or NULL.
def clear():

    dayinput.delete(0,END)
    monthinput.delete(0,END)
    yearinput.delete(0,END)
    seconddayinput.delete(0,END)
    secondmonthinput.delete(0,END)
    secondyearinput.delete(0,END)
    finalDayoutput.delete(0,END)
    finalMonthoutput.delete(0,END)
    finalYearoutput.delete(0,END)

# It checks all the input entries and returns Input Error if any entry is absent.
def checkEntries():
    if (dayinput.get() == "" or monthinput.get() == ""
        or yearinput.get() == "" or seconddayinput.get() == ""
        or secondmonthinput.get() == "" or secondyearinput.get() == ""):

            messagebox.showerror("Input Error")

            clear()
            return -1

# This function performs all the calculation and returns the calculated age.
def calculateAge():

    value = checkEntries()
    if value == -1:
        return
    else:

        birth_day = int(dayinput.get())
        birth_month = int(monthinput.get())
        birth_year = int(yearinput.get())

        entered_day = int(seconddayinput.get())
        entered_month = int(secondmonthinput.get())
        entered_year = int(secondyearinput.get())

        month =[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        if(birth_day > entered_day):
            entered_month = entered_month -1
            entered_day = entered_day + month[birth_month - 1]

        if(birth_month > entered_month):
            entered_year = entered_year -1
            entered_month = entered_month + 12

        calculated_day = entered_day - birth_day
        calculated_month = entered_month - birth_month
        calculated_year = entered_year - birth_year

        finalDayoutput.insert(10, str(calculated_day))
        finalMonthoutput.insert(10, str(calculated_month))
        finalYearoutput.insert(10, str(calculated_year))

if __name__ == "__main__":

    root = Tk()

    root.resizable(width=False,height=False)

    root.title("AGE CALCULATOR")

    root.geometry("535x280")

    root.config(bg="#F7DC6F")

    dob = Label(root, text = "Date Of Birth", bg = "#F7DC6F",font=('Times New Roman',12))

    enteredDate = Label(root, text = "Age at the date of",bg = "#F7DC6F", font=('Times New Roman',12))


    greeting = Label(root, text = " Enter the dates in 'DD-MM-YYYY' format",bg="#F7DC6F", font = ('STENCIL', 15))
    
    resultantagebutton = Button(root, text = "Calculate Age",fg="black", bg = '#5ced73',font = ('Calibri', 10),command = calculateAge)

    ResultantAge = Label(root, text = "You are ", bg = "#F7DC6F",font=('Times New Roman',13))
    
    daylabel = Label(root, text = "days old", bg = "#F7DC6F", font=('Times New Roman',13))

    monthlabel = Label(root, text = "months", bg = "#F7DC6F", font=('Times New Roman',13))

    yearlabel = Label(root, text = "years",  bg = "#F7DC6F",font=('Times New Roman',13))

    Clear = Button(root, text = "Clear All", fg = "Black", bg = '#f94449', font = ('Calibri', 10),command = clear)

    dayinput = Entry(root,width = 5, font = ('Arial',12))
    monthinput = Entry(root,width = 5, font = ('Arial',12))
    yearinput = Entry(root,width = 5, font = ('Arial',12))

    seconddayinput = Entry(root, width =5, font = ('Arial',12))
    secondmonthinput = Entry(root,width = 5, font = ('Arial',12))
    secondyearinput = Entry(root,width = 5,  font = ('Arial',12))

    finalDayoutput = Entry(root, width = 2, font = ('Arial',11))
    finalMonthoutput = Entry(root, width = 2, font = ('Arial',11))
    finalYearoutput = Entry(root, width = 2, font = ('Arial',11))

    greeting.place(x = 85, y = 15)

    dob.place(x=132, y=55)
    dayinput.place(x=230, y=55)
    monthinput.place (x=275, y=55)
    yearinput.place(x=320, y=55)

    enteredDate.place(x=104,y =90)
    seconddayinput.place(x=230, y=90)
    secondmonthinput.place (x=275, y=90)
    secondyearinput.place(x=320, y=90)

    resultantagebutton.place(x = 240, y = 135)

    ResultantAge.place(x = 120, y = 180)
    finalYearoutput.place(x = 184, y = 180)
    yearlabel.place(x = 206, y = 180)
    finalMonthoutput.place(x = 248, y = 180)
    monthlabel.place(x = 270, y = 180)
    finalDayoutput.place(x = 326, y = 180)
    daylabel.place(x = 349, y = 180)
   
    Clear.place(x = 250, y = 220)
    
root.mainloop()