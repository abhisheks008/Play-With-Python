import subprocess
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from tkinter import messagebox, filedialog
from popup import Popup, center_window


class WifiPasswordSaver:

    def __init__(self):
        self.initial_app()
        self.root = None
        self.text_box = None
        self.data = []
        super(WifiPasswordSaver, self).__init__()

    def initial_app(self):
        self.root = tk.Tk()
        self.root.config(width=400, height=400)
        self.root.title("Wifi Password Saver")
        self.root.resizable(False, False)

        self.text_box = ScrolledText(self.root, wrap='word', height=10, width=400, state='disabled', cursor='arrow',
                                     background='white', pady=30, )
        self.text_box.pack(fill=tk.BOTH, expand=True)
        self.text_box.focus_set()
        center_window(self.root)

        self.menu()
        self.wifi_password_saver()
        self.root.mainloop()

    # pop up for passwords
    def show_password(self, password,wifiname):
        Popup(title='Password', message=f'{wifiname} : {password}', master=self.root)
        return

    # main function for wi-fi password
    def wifi_password_saver(self):
        try:
            # using the check_output() for having the network term retrieval
            devices = subprocess.check_output(['netsh', 'wlan', 'show', 'network'])

            # decode it to strings
            devices = devices.decode('ascii')

            s = devices.replace("\r", "")

            # displaying the information
            nearby = [x[x.find(':') + 1:].replace('\r', '').strip() for x in devices.split('\n') if "SSID" in x]

            # getting meta data
            meta_data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles'])

            # decoding meta data
            data = meta_data.decode('utf-8', errors="backslashreplace")

            # splitting data by line by line
            data = data.split('\n')

            # creating a list of profiles
            profiles = []

            # traverse the data
            for i in data:

                # find "All User Profile" in each item
                if "All User Profile" in i:
                    # if found
                    # split the item
                    i = i.split(":")

                    # item at index 1 will be the wifi name
                    i = i[1]

                    # formatting the name
                    # first and last character is use less
                    i = i[1:-1]

                    # appending the wifi name in the list
                    profiles.append(i)

            wifi_column = 2
            password_column = 4
            nearby_column = 6
            # return heading
            self.wifi_label = tk.Label(self.text_box, text='Wi-Fi Name', font='Times 16', background='white')
            self.wifi_label.grid(column=wifi_column, row=1, padx=15)

            self.password_label = tk.Label(self.text_box, text='Password', font='Times 16', background='white')
            self.password_label.grid(column=password_column, row=1, padx=30)

            self.nearby_label = tk.Label(self.text_box, text='Nearby Network', font='Times 16', background='white')
            self.nearby_label.grid(column=nearby_column, row=1, padx=40)

            # traversing the profiles
            self.data = []
            for number, i in enumerate(profiles):

                # try catch block begins
                # try block
                try:
                    # getting meta data with password using wifi name
                    results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear'])

                    # decoding and splitting data line by line
                    results = results.decode('utf-8', errors="backslashreplace")
                    results = results.split('\n')

                    # finding password from the result list
                    results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]

                    # if there is password it will return the pass word
                    try:
                        nearbyFlag = i in nearby
                        wifi_name = tk.Label(self.text_box, font='Aerial 11', text=i, background='white')
                        wifi_name.grid(column=wifi_column, row=number + 5, pady=10)

                        password = tk.Label(self.text_box, font='Aerial 13 bold', text='***', cursor='hand2',
                                            background='white')
                        password.grid(column=password_column, row=number + 5, pady=10)
                        password.bind('<Button-1>', lambda e,wifiname=i, passw=results[0]: self.show_password(passw,wifiname))

                        is_nearby = tk.Label(self.text_box, background='white', font='Aerial 11',
                                             text="Y" if nearbyFlag else "N", fg="blue" if nearbyFlag else "red", )
                        is_nearby.grid(column=nearby_column, row=number + 5, pady=10)

                        self.data.append([i, results[0], "Y" if nearbyFlag else "N"])
                    except IndexError:
                        pass
                # called when this process get failed
                except subprocess.CalledProcessError:
                    tk.Message(text='Encoding Error Occurred', fg='red').grid(column=4, row=20)
        except subprocess.CalledProcessError:
            # this method waits till message box closed then call destroy
            self.root.withdraw()
            messagebox.showinfo('error', 'Please turn on your Wi-fi')
            self.root.destroy()

    def restart_app(self):
        self.root.destroy()
        self.initial_app()

    # navbar buttons
    def menu(self):
        self.menubar = tk.Menu(self.root)
        self.root.config(menu=self.menubar)
        self.menubar.add_command(label="Restart App", command=self.restart_app)
        self.menubar.add_command(label="Save As", command=self.save_file_as)

    # save informations in the files
    def save_file_as(self, whatever=None):
        try:
            self.filename = filedialog.asksaveasfilename(
                defaultextension='.txt',
                filetypes=[('Text', '*.txt')]
            )
            f = open(self.filename, 'w')
            self.structure_data_in_file(f)
            f.close()
            messagebox.showinfo('Wi-Fi Password', 'File Saved')
        except FileNotFoundError:
            pass

    # this function used for structuring text data in text files
    def structure_data_in_file(self, f):
        dash_line = ("-" * 80)
        header = "{:<20}| {:<30} | {:<20} \n {} \n".format(
            (str(self.wifi_label['text'])),
            str(self.password_label['text']),
            str(self.nearby_label['text']),
            str(dash_line)
        )
        f.write(header)
        for item in self.data:
            data = "{:<20}| {:<30} | {:<20} \n".format(item[0], item[1], item[2])
            f.write(str(data))


WifiPasswordSaver()
