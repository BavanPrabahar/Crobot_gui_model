import kivy
from kivy.config import Config
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
import time
from kivy.clock import Clock
from datetime import datetime
from kivy.uix.popup import Popup

from pulsectl import Pulse, PulseVolumeInfo,pulsectl



Config.set('input', 'mouse', 'mouse,multitouch_on_demand')


Window.size = (1280,800)


Colors = {
    "Orange": {
        "200": "#E25011",
        "500": "#E25011",
        "700": "#E25011",
    },
    "White": {
        "200": "#EEEEEE",
        "500": "#EEEEEE",
        "700": "#EEEEEE",
    },
    "Light": {
        "StatusBar": "E0E0E0",
        "AppBar": "#EEEEEE",
        "Background": "#2E3032",
        "CardsDialogs": "#FFFFFF",
        "FlatButtonDown": "#CCCCCC",
    }
}





class FirstKVfileApp(MDApp): 

    def build(self):

        self.theme_cls.colors = Colors
        self.theme_cls.primary_palette = "Orange"
        

        # self.theme_cls.primary_palette = "DeepOrange"               #for the fab button 
        # self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_hue= "200"
       
        Clock.schedule_interval(self.update_time_date, 1)

        

        


        return Builder.load_file("practice3.kv")
    
    def update_time_date(self, dt):
        # Get current time and date
        now = datetime.now()
        current_time = now.strftime("%H:%M")
        current_date = now.strftime("%d-%m-%Y")

        # Update labels
        self.root.ids.time_label.text = f"Time: {current_time}"
        self.root.ids.date_label.text = f"Date: {current_date}"

    def show_volume_slider_1(self):
        volume_slider_1 = self.root.ids.volume_slider_1
        volume_slider_1.opacity = 1

        
    def show_volume_slider_2(self):
        volume_slider_2=self.root.ids.volume_slider_2
        volume_slider_2.opacity = 1

    def show_volume_slider_3(self):
        volume_slider_3=self.root.ids.volume_slider_3
        volume_slider_3.opacity = 1

    def show_volume_slider_4(self):
        volume_slider_4=self.root.ids.volume_slider_4
        volume_slider_4.opacity = 1

    def show_volume_slider_5(self):
        volume_slider_5=self.root.ids.volume_slider_5
        volume_slider_5.opacity = 1

    def slider_volume_change(self, value):
        x=int(value)
        print(x)


if __name__=="__main__":
    # Window.borderless=True

    FirstKVfileApp().run()