# Weather App

This app built using `tkinter` and `openweathermap` API

## Approach

**Working with API**

- open [openweathermap](https://openweathermap.org/) API website and navigate to sing-up page
- create account and you will get API Key on successfull account creation through mail or navigate to API page to see the API key
- copy the API key
- to make sure the key is working or not use `api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}` by replacing `{city name}` and `{API key}` with your city name and API key

Now create the GUI and make a function `getWeather()` to get the details of weather

**To get Weather details**

- import `request` module
- store the openweathermap API key in `weatherApiKey` variable and take city name user input into `city` variable
- use `request.get().json` by passing the query `"http://api.openweathermap.org/data/2.5/weather?appid=" + weatherApiKey + "&q=" + city` to fetch the weather details in json format

While running this app, we will get some HTTPerrors like :

`404` - this means, Can't find weather data for this city

`401` - Unauthorized

Make sure to handle such HTTPerrors
## Demonstration

https://user-images.githubusercontent.com/89008784/210406636-40f1e017-c644-4e99-9774-86080dd37797.mp4

