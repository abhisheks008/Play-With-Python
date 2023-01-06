import datetime
import time
from tkinter import * 
from playsound import playsound

root = Tk() 
root.title("Alarm Clock")
root.geometry("265x270")
root.resizable(width=False,height=False)

# functions
def setalarm():
    alarmtime=f"{hrs.get()}:{mins.get()}:{secs.get()}"
    # print(alarmtime)
    if(alarmtime!="::"):
        alarmclock(alarmtime) 

def alarmclock(alarmtime): 
    while True:
        time.sleep(1)
        time_now=datetime.datetime.now().strftime("%H:%M:%S")
        print(time_now)
        if time_now==alarmtime:
            Wakeup=Label(root, font = ('arial', 13, 'bold'),
            text="Time to Wake up!",fg="red").grid(row=10,columnspan=4)
            # print("wake up!")
            playsound('alarm.mp3')
            break

# GUI
hrs=StringVar()
mins=StringVar()
secs=StringVar()

Label(root, font = ('arial', 16, 'bold'),
text="Set Your Alarm Clock!").grid(row=1,columnspan=4)

Label(root, font = ('arial', 12, 'bold'),
text="ENTER IN 24Hrs FORMAT").grid(row=2,columnspan=4)


Label(root, font = ('arial', 11, 'bold'),
text="Hour").grid(row=3,column=1)

hrbtn=Entry(root,textvariable=hrs,width=5,
font =('arial', 18, 'bold')).grid(row=4,column=1)

Label(root, font = ('arial', 11, 'bold'),
text="Minute").grid(row=3,column=2)

minbtn=Entry(root,textvariable=mins,width=5,
font = ('arial', 18, 'bold')).grid(row=4,column=2)

Label(root, font = ('arial', 11, 'bold'),
text="Second").grid(row=3,column=3)

secbtn=Entry(root,textvariable=secs,
width=5,font = ('arial', 18, 'bold')).grid(row=4,column=3)

setbtn=Button(root,text="Set Alarm",command=setalarm,bg="#D4AC0D",
fg="Black",font = ('arial', 19, 'bold')).grid(row=8,columnspan=4)

timeleft = Label(root,font=('arial', 20, 'bold')) 
timeleft.grid()

exit = Button(root,text="Exit",width=10, command=root.destroy, bg="#D4AC0D",
fg="Black",font = ('arial', 19, 'bold'))
exit.grid(row=9, columnspan=4)
  
mainloop() 