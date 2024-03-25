import kivy
from kivy.config import Config
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
import time
from kivy.clock import Clock
from datetime import datetime
from kivy.uix.popup import Popup
from pulsectl import Pulse, PulseVolumeInfo
import subprocess
import alsaaudio


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
        "AppBar": "#202020",
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

        

        


        return Builder.load_file("gui.kv")
    
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
        
    def btn1(self):
    	catkin_workspace_path = "/home/crobot/crobot_ws/devel/setup.bash"
    	command1 = f"source {catkin_workspace_path} && roslaunch hello12 firsta.launch"
    	full_command = f"gnome-terminal --tab --title='Tab 1' --command='bash -c \"{command1}; exec bash\"'"
    	subprocess.Popen(full_command, shell=True)
    def on_slider_value_change(self, value):
    	slider_value_1=int(value)
    	print(slider_value_1)
    	m = alsaaudio.Mixer()
    	m.setvolume(slider_value_1)
    def on_slide_1(self,value):
    	abc=int(value)
    	self.ids["volume_slider_1"].value2=abc
    	
 
		



if __name__=="__main__":
    Window.borderless=True
    Config.set('kivy','exit_on_escape','0')
    FirstKVfileApp().run()
