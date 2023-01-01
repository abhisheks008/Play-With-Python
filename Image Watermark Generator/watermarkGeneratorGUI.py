import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageDraw, ImageFont
import os   

class watermarkGeneratorGUI(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.label1 = tk.Label(self, text="Image Watermark Generator")
        self.label1.pack(side="top")
        self.label1.config(font=("Arial", 30))

        self.label2 = tk.Label(self, text="Select an image to watermark")
        self.label2.pack(side="top")
        self.label2.config(font=("Arial", 15))
        self.label2.config(fg="blue")

        self.button1 = tk.Button(self, text="Browse", command=self.browse_button)
        self.button1.pack(side="top")
        self.button1.config(font=("Arial", 15))
        self.button1.config(fg="brown")

        self.label3 = tk.Label(self, text="Enter the text to watermark")
        self.label3.pack(side="top")
        self.label3.config(font=("Arial", 15))

        self.entry1 = tk.Entry(self)
        self.entry1.pack(side="top")
        self.entry1.config(font=("Arial", 15))

        self.button2 = tk.Button(self, text="Generate", command=self.generate_button)
        self.button2.pack(side="top")
        self.button2.config(font=("Arial", 15))

    def browse_button(self):
        self.filename = filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
        self.label2.configure(text="Selected file: " + self.filename)

    def generate_button(self):
        watermark_text = self.entry1.get()
        if watermark_text == "":
            messagebox.showerror("Error", "Please enter the text to watermark")
        else:
            self.label3.configure(text="Watermark text: " + watermark_text)
            self.label3.pack(side="top")
            self.generate_watermark(watermark_text)

    def generate_watermark(self, watermark_text):
        image = Image.open(self.filename)
        draw = ImageDraw.Draw(image)
        image_width, image_height = image.size
        font = ImageFont.truetype("arial.ttf", 36)
        text_width, text_height = draw.textsize(watermark_text, font)
        margin = 10
        x = image_width - text_width - margin
        y = image_height - text_height - margin
        draw.text((x, y), watermark_text, font=font)
        image.save(os.path.splitext(self.filename)[0] + "_watermarked.jpg")
        self.label2.configure(text="Watermarked image saved as " + os.path.splitext(self.filename)[0] + "_watermarked.jpg")

root = tk.Tk()
root.title("Image Watermark Generator")
root.geometry("800x600")
app = watermarkGeneratorGUI(master=root)
app.mainloop()
