from kivy.core.window import Window
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.relativelayout import MDRelativeLayout
from kivy.core.text import LabelBase
from api import getStateInfo

#Defining Window Size
Window.size = (600, 600)

class WindowManager(ScreenManager):
    pass

class Covid_Tracker(MDApp):
    def build(self):
        self.screen = Builder.load_file("./components/main.kv")
        return self.screen

    def showData(self):
        # Receiving state name from Text Input 
        state = self.screen.get_screen('screen2').ids.cityName.text
        apiData = getStateInfo(state or "Delhi")
        if apiData != 0:
            # Fetching and storing API data
            apiProvince = str(apiData[0])
            apiConfirmedCases = str(apiData[1])
            apiDeaths = str(apiData[2])
            apiLastUpdate = str((apiData[3])[:10])

            # Retrieving ids from App Screen
            provinceName = self.screen.get_screen('screen2').ids.province
            confirmedCases = self.screen.get_screen('screen2').ids.confirmed
            deaths = self.screen.get_screen('screen2').ids.deaths
            lastupdated = self.screen.get_screen('screen2').ids.lastupdated

            # Printing Updated Data back to App Screen
            provinceName.text = "[b]"+apiProvince+", India[/b]"
            confirmedCases.text = "[b]"+apiConfirmedCases+"[/b]"
            deaths.text = "[b]"+apiDeaths+"[/b]"
            lastupdated.text = "[b]"+apiLastUpdate+"[/b]"

        else:
            print("Records not found, Insufficient Data")

Covid_Tracker().run()