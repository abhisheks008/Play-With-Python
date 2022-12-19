import tkinter as tk
import time


# Create the main window
window = tk.Tk()
# window.attributes("-fullscreen", True)

# Create a label to display the time
time_label = tk.Label(window, font=("Helvetica", 150))
time_label.pack()

# Function to update the time
def update_time():
    # Get the current time
    current_time = time.strftime("%I:%M:%S %p")
   
    # Update the time label
    time_label.configure(text=current_time)

    # Call this function again after one second
    window.after(1000, update_time)

# Start the clock
update_time()

# Start the main loop
window.mainloop()
