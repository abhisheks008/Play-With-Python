#importing all the required libraries

import requests
from bs4 import BeautifulSoup
import tkinter as tk
from datetime import date

#creating a new window
window=tk.Tk()
window.title("News App")
window.geometry('1000x1000')

#words used to clean the extracted data
words=['Get in touch','Mobile app','News daily newsletter','BBC World News TV','BBC World Service Radio']

#function used to extract the news
def get_news():
        try:
                news=""
                response=requests.get('https://www.bbc.com/news')
                #using beautiful soup to find ang get the required items 
                soup = BeautifulSoup(response.text,'html.parser')
                s = soup.find('body')
                content=s.find_all('h3')
                for x in content:
                        if x.text.strip() not in words:
                                news+="\n"+x.text.strip()
                news_label=tk.Label(window,text=news)
                news_label.pack()

        
        #Exception Handling
        except requests.exceptions.RequestException as e:
                error_label=tk.Label(window,text="Error: Unable to retrieve news:"+e)
                error_label.pack()


date_label=tk.Label(window,text=date.today())
date_label.pack()
get_news_button=tk.Button(window,text="Get News",command=get_news)
get_news_button.pack()
window.mainloop()
