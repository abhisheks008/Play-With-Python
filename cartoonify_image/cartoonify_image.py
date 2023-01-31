from tkinter import filedialog
import tkinter as tk
import cv2
from PIL import ImageTk,Image,UnidentifiedImageError
import numpy as np

#importing all the required libraries

window=tk.Tk()
#initializing the tkinter window

window.title("Cartoonify Image")
window.geometry("1000x1000")

#A function used to open the image
def open_image():
    try:
        #img is made global so that it can be accessed outside the open_image function
        global img

        #it is used to get the path of the image
        filepath=filedialog.askopenfilename()
        image_name=filepath.split("/")[-1]

        #message indicating that the image has been uploaded
        image_label=tk.Label(window,text=image_name+" has been uploaded.")
        image_label.pack(pady=10)

        #opening the image using PIL(Python Image Library)
        img=Image.open(filepath)
        #converting the image to a displayable format
        image=ImageTk.PhotoImage(img)

        #displaying the image on the window
        image_display_label=tk.Label(window,image=image)
        image_display_label.image=image
        image_display_label.pack(pady=10)
    #handling the error if the user uploads a file other than an image
    except UnidentifiedImageError:
        error_label=tk.Label(window,text="Please Upload an Image ")
        error_label.pack()

#function to convert the image to a cartoon
def cartoonify(img):
    
    #cartoon_image is made global so that it can be accessed in the other parts of the program
    global cartoon_image

    #Converting the image to grayscale
    gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #medianBlur blur the image based on the provided value
    gray_blur_image= cv2.medianBlur(gray_image, 5)

    #adaptiveThreshold is used to get the edges of the image
    # cv2.ADAPTIVE_THRESH_MEAN_C is the algorithm used to perform the Treshold operation
    #whereas cv2.THESH_BINARY is the type of the Threshold
    edges = cv2.adaptiveThreshold(gray_blur_image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 5,5)
    
    #making the color_image tha same shape and type as that of the original image
    color_image = np.zeros(img.shape, img.dtype)
    
    #to convert the image from 4 channel to 3 channels
    #As the bilateralFilter does not accept a 4 channel image
    b, g, r, a = cv2.split(img)
    img = cv2.merge((b, g, r))
    
    #to apply bilateralFilter to image based on the given parameters
    color_image=cv2.bilateralFilter(img,4,300,300)
    #bitwise_and merges the two given images to produce the final effect using the edges as the mask
    cartoon_image = cv2.bitwise_and(color_image, color_image, mask=edges)
    
    #fromarray is used to converta numpy array into an image
    cartoon_image=Image.fromarray(cartoon_image)
    cartoon_image=ImageTk.PhotoImage(cartoon_image)
    #displaying the image
    label=tk.Label(window,text="The cartoonified Image")
    label.pack(pady=5)
    image_display_label=tk.Label(window,image=cartoon_image)
    image_display_label.image=cartoon_image
    image_display_label.pack(pady=10)


#creating a button to open the image
open_image_buttuon=tk.Button(window,text="Open Image",command=open_image)
open_image_buttuon.pack(pady=5)

#creating a bnutton to cartoonify the image
cartoonify_image_buttuon=tk.Button(window,text="Cartoonify Image",command=lambda:cartoonify(np.asarray(img)))
cartoonify_image_buttuon.pack(pady=5)


window.mainloop()