from tkinter import *
import requests


root = Tk()
root.geometry('600x2060')
root.title('Weather App')


heading_label = Label(root, text="Welcome To The Weather App", font="poppins 20 bold")
heading_label.pack()
search_cityLabel = Label(root, text="Search Weather in your city ", fg='dark blue', font="poppins 16 ")
search_cityLabel.pack()

search_entry = Entry(root,font="poppins 14 ")
search_entry.pack()

def getWeather():
    weatherApiKey = 'b69aad09b93027c2964380fa99fa3f0c'
    city = search_entry.get()
    url = "http://api.openweathermap.org/data/2.5/weather?appid=" + weatherApiKey + "&q=" + city
    data = requests.get(url).json()
    if data["cod"] != "404":
        y = data["main"]
    else:
        city_name_label['text'] = "Please enter a valid city name"
        return
    #getting temperature
    current_temperature = y["temp"]
    current_temperature -= 274.04
    #extracting humidity
    current_humidity = y["humidity"]
    z = data["weather"]
    weather_description = z[0]["description"]
    degree_sign = u"\N{DEGREE SIGN}"
    temperature = "{:.0f}".format(current_temperature) + degree_sign + "C"
    humidity = str(current_humidity) + "%"
    details = weather_description
    #changing the image according to the weather condition
    if "clouds" in details:
        photo = PhotoImage(file='./images/partly cloudy.png')
        photoLabel.config(image=photo)
        photoLabel.image = photo
    elif "clear sky" in details :
        photo = PhotoImage(file='./images/clear sky.png')
        photoLabel.config(image=photo)
        photoLabel.image = photo
    elif "windy" in details : 
        photo = PhotoImage(file='./images/windy.png')
        photoLabel.config(image=photo)
        photoLabel.image = photo
    elif "rain" in details : 
        photo = PhotoImage(file='./images/heavy rain.png')
        photoLabel.config(image=photo)
        photoLabel.image = photo
    elif "haze" in details : 
        photo = PhotoImage(file='./images/haze.png')
        photoLabel.config(image=photo)
        photoLabel.image = photo
    
    city_name = search_entry.get()
    city_name_label['text'] = "Location : "+city_name.title()

    temperature_label['text'] = temperature+","+details
    humidity_label['text'] = "Humidity : " + humidity
    return

button1 = Button(text='Search', command=getWeather, bg='black', fg='white', font="poppins 12")
button1.pack()

city_name_label = Label(root,text = "", font="poppins 16")
city_name_label.pack()
photo = PhotoImage(file='./images/windy.png')
photoLabel = Label(root,image=photo)
photoLabel.pack()
temperature_label = Label(root,text = " ", font="poppins 16")
temperature_label.pack()
humidity_label = Label(root,text = " ", font="poppins 16")
humidity_label.pack()

root.mainloop()
