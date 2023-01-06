
import tkinter as Tkinter
from datetime import datetime

root = Tkinter.Tk()
root.title("Stopwatch")

# Fixing the window size.
root.minsize(width=250, height=250) 

counter = 66600
running = False
def counter_label(label):
	def count():
		if running:
			global counter
			tt = datetime.fromtimestamp(counter)
			string = tt.strftime("%H:%M:%S")
			display=string

			label['text']=display
			label.after(1000, count)
			counter += 1

	# Triggering the start of the counter.
	count()	

# start function of the stopwatch
def start(label):
	global running
	running=True
	counter_label(label)
	start_btn['state']='disabled'
	stop_btn['state']='normal'
	reset_btn['state']='normal'

# Stop function of the stopwatch
def stop():
	global running
	start_btn['state']='normal'
	stop_btn['state']='disabled'
	reset_btn['state']='normal'
	running = False

# Reset function of the stopwatch
def reset(label):
	global counter
	counter=66600

	# If reset is pressed after pressing stop.
	if running==False:	
		reset_btn['state']='disabled'
		label['text']='00:00:00'

	# If reset is pressed while the stopwatch is running.
	else:			
		label['text']='00:00:00'


time_label = Tkinter.Label(root, text="00:00:00", fg="black", font="Arial 30 bold")
time_label.pack()
#creating a frame to align the buttons next to each other
f = Tkinter.Frame(root)
start_btn = Tkinter.Button(f, text='Start', font="Arial 16 bold",bg="#50e3a4", command=lambda:start(time_label))
stop_btn = Tkinter.Button(f, text='Stop',font="Arial 16 bold",bg = "#fb6b6c",state='disabled', command=stop)
reset_btn = Tkinter.Button(f, text='Reset',font="Arial 16 bold", state='disabled', command=lambda:reset(time_label))
f.pack(anchor = 'center',pady=5)
start_btn.pack(side="left")
stop_btn.pack(side ="left")
reset_btn.pack(side="left")
root.mainloop()
