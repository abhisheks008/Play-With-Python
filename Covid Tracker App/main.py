from kivy.core.window import Window
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.relativelayout import MDRelativeLayout
from kivy.core.text import LabelBase

#Defining Window Size
Window.size = (600, 600)

class WindowManager(ScreenManager):
    pass

class Covid_Tracker(MDApp):
    def build(self):
        self.screen = Builder.load_file("./components/main.kv")
        return self.screen

    def getData(self):
        print(self.screen.get_screen('screen2').ids.cityName.text)

Covid_Tracker().run()