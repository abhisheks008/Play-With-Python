#Import required Image library
from PIL import Image, ImageDraw, ImageFont

print("""
Image Watermark Generator

This program will add a watermark to an image.
To add a watermark to an image, save the image in the same folder as this program and enter the name of the image when prompted.
The image with the generated watermark will be saved in the result folder.
""")

#Get the image name from the user
image_name = input("Enter the name of the image (Also include the extension): ")
#Create an Image Object from an Image
im = Image.open('Image Watermark Generator/'+image_name)
width, height = im.size

draw = ImageDraw.Draw(im)
text = input("Enter the text to be added as watermark: ")

fontsize = int(input("Enter the font size: (Default is 36 and max is 100) "))
font = ImageFont.truetype('arial.ttf', fontsize)
textwidth, textheight = draw.textsize(text, font)

# calculate the x,y coordinates of the text
margin = 10
x = width - textwidth - margin
y = height - textheight - margin

# draw watermark in the bottom right corner
draw.text((x, y), text, font=font)
im.show()

#Save watermarked image
im.save('Image Watermark Generator/result/watermark.jpg')