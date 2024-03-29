import kivy
from kivy.config import Config
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
import time
from kivy.clock import Clock
from datetime import datetime
from kivy.uix.popup import Popup
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
        "AppBar": "#EEEEEE",
        "Background": "#2E3032",
        "CardsDialogs": "#FFFFFF",
        "FlatButtonDown": "#CCCCCC",
    }
}





class FirstKVfileApp(MDApp): 
    x=0
     

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
        #elf.root.ids.time_label.text = f"Time: {current_time}"
        #self.root.ids.date_label.text = f"Date: {current_date}"

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

   
    def on_slider_value_change(self, value):
    	slider_value_1=int(value)
       
    	m = alsaaudio.Mixer()
    	m.setvolume(slider_value_1)  
    	x=m.getvolume()
    	
    def on_slider2(self,value):
    	slider_value_2=int(value)
       
    	m = alsaaudio.Mixer()
    	m.setvolume(slider_value_2)  
    	x=m.getvolume()
    	self.root.ids["volume_slider_1"].value=x[0]
    	
    	
    	
    	
    def btn1(self):
    
    	catkin_workspace_path = "/home/racer/catkin_ws/devel/setup.bash"
    	command1 = f"source {catkin_workspace_path} && roslaunch hello a.launch"
    	
    	full_command = f"gnome-terminal --tab --title='Tab 1' --command='bash -c \"{command1}; exec bash\"'"
    	subprocess.Popen(full_command, shell=True)  
    def btn5(self):
    
    	catkin_workspace_path = "/home/racer/catkin_ws/devel/setup.bash"
    	command1 = f"source {catkin_workspace_path} && roslaunch hello b.launch"
    	
    	full_command = f"gnome-terminal --tab --title='Tab 1' --command='bash -c \"{command1}; exec bash\"'"
    	subprocess.Popen(full_command, shell=True)  
    def btn3(self):
    
    	catkin_workspace_path = "/home/racer/catkin_ws/devel/setup.bash"
    	command1 = f"source {catkin_workspace_path} && sudo shutdown now"
    	
    	full_command = f"gnome-terminal --tab --title='Tab 1' --command='bash -c \"{command1}; exec bash\"'"
    	subprocess.Popen(full_command, shell=True)  
    	
    	
    def btn2(self):
    
    	catkin_workspace_path = "/home/racer/catkin_ws/devel/setup.bash"
    	command2 = f"source {catkin_workspace_path} && rosnode kill webcam_pub webcam_sub"
    	full_command = f"gnome-terminal --tab --title='Tab 1' --command='bash -c \"{command2}; exec bash\"'"
    	subprocess.Popen(full_command, shell=True)  
    
    def btn4(self):
    	catkin_workspace_path = "/home/racer/catkin_ws/devel/setup.bash"
    	command2 = f"source {catkin_workspace_path} && rosnode kill -a"
    	full_command = f"gnome-terminal --tab --title='Tab 1' --command='bash -c \"{command2}; exec bash\"'"
    	subprocess.Popen(full_command, shell=True)  
    	


if __name__=="__main__":
    # Window.borderless=True

    FirstKVfileApp().run()
