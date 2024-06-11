import kivy
import sys
from kivy.config import Config
from kivymd.app import MDApp
from kivy.uix.label import Label
import subprocess
from kivy.uix.textinput import TextInput
import shlex
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.textfield import MDTextField
from kivy.lang import Builder
from kivy.core.window import Window
import time
from kivy.clock import Clock
from datetime import datetime
from kivy.uix.popup import Popup
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivy.properties import NumericProperty
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivymd.uix.screen import MDScreen
from kivymd.uix.selectioncontrol import MDSwitch
from kivy.properties import StringProperty
from kivy.clock import Clock
import rospy


Config.set('input', 'mouse', 'mouse,multitouch_on_demand')
a=0

# Window.size = (1280,800)


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

    x = NumericProperty(0)
    y = NumericProperty(0)
    b=[]
    w=None
    l=None
    def build(self):

        self.theme_cls.colors = Colors
        self.theme_cls.primary_palette = "Orange"
        

        # self.theme_cls.primary_palette = "DeepOrange"               #for the fab button 
        # self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_hue= "200"

       
       
        Clock.schedule_interval(self.update_time_date, 1)
        Clock.schedule_interval(self.update_time_date, 1)

        Window.borderless=True

        

        


        return Builder.load_file("practice3.kv")
    
    def update_time_date(self, dt):
        # Get current time and date
        now = datetime.now()
        current_time = now.strftime("%H:%M")
        current_date = now.strftime("%d-%m-%Y")

        # Update labels
        self.root.ids.date_label.text = f"{current_time}"
        self.root.ids.time_label.text = f"{current_date}"

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

    def show_volume_slider_record_screen(self):
        volume_slider_record_screen=self.root.ids.volume_slider_record_screen
        volume_slider_record_screen.opacity = 1
        
    def show_volume_slider_navigation_screen(self):
        volume_slider_record_screen=self.root.ids.volume_slider_navigation_screen
        volume_slider_record_screen.opacity = 1

    def slider_volume_change(self, value):
        x=int(value)
        print(x)


    def move_up(self):
        self.y += 1
        print("Move Up",self.y)

    def move_down(self):
        self.y -= 1
        print("Move Down",self.y)

    def move_left(self):
        self.x -= 1
        print("Move Left", self.x)

    def move_right(self):
        self.x += 1
        print("Move Right", self.x)

    

    def show_popup(self):
        self.dialog = MDDialog(
            title="Hello, world!",
            text="This is a KivyMD popup window.",
            buttons=[
                MDFlatButton(
                    text="START OVER", on_release=self.close_popup
                ),
                MDFlatButton(
                    text="ACCEPT", on_releasse=self.close_popup
                ),
            ],
        )
        self.dialog.open()

    def close_popup(self, obj):
        self.dialog.dismiss()

    def btn1(self):#launch
        catkin_workspace_path = "/home/crobot/crobot_ws/devel/setup.bash"
        command1 = f"source {catkin_workspace_path} && roslaunch ubot ubot_run.launch"
        full_command = f"gnome-terminal --tab --title='Tab 1' --command='bash -c \"{command1}; exec bash\"'"
        try:
            process=subprocess.Popen(full_command,stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
            
            
        
            return_code = process.wait()
            if return_code != 0:
                print("Error occurred ")
            else:
                print("Process executed successfully.")
        except subprocess.CalledProcessError as e:
            print("An error occurred")
        
        except Exception as e:
            print("An error occurred")
            
        
    def btn5(self):#teleoperration
        catkin_workspace_path = "/home/crobot/crobot_ws/devel/setup.bash"
        command1 = f"source {catkin_workspace_path} && roslaunch ubot ubot_run.launch"
        full_command = f"gnome-terminal --tab --title='Tab 1' --command='bash -c \"{command1}; exec bash\"'"
        subprocess.Popen(full_command, shell=True)  
    def btn3(self):#terminate
        catkin_workspace_path = "/home/crobot/crobot_ws/devel/setup.bash"
        command1 = f"source {catkin_workspace_path} && sudo shutdown now"
        full_command = f"gnome-terminal --tab --title='Tab 1' --command='bash -c \"{command1}; exec bash\"'"
        subprocess.Popen(full_command, shell=True)  
    
    def btn4(self):
        catkin_workspace_path = "/home/crobot/crobot_ws/devel/setup.bash"
        command2 = f"source {catkin_workspace_path} && rosnode kill -a"
        full_command = f"gnome-terminal --tab --title='Tab 1' --command='bash -c \"{command2}; exec bash\"'"
        subprocess.Popen(full_command, shell=True) 
    def btn7(self):
        catkin_workspace_path = "/home/crobot/crobot_ws/devel/setup.bash"
        command2 = f"source {catkin_workspace_path} && rosbag record --all -O all_data.bag /topic __name:=my_bag"
        full_command = f"gnome-terminal --tab --title='Tab 1' --command='bash -c \"{command2}; exec bash\"'"
        subprocess.Popen(full_command, shell=True) 
    def btn8(self):
        catkin_workspace_path = "/home/crobot/crobot_ws/devel/setup.bash"
        command2 = f"source {catkin_workspace_path} &&  rosnode kill /my_bag"
        full_command = f"gnome-terminal --tab --title='Tab 1' --command='bash -c \"{command2}; exec bash\"'"
        subprocess.Popen(full_command, shell=True) 
    def btn9(self,h):
        
        pub = rospy.Publisher('/cmd_vel1', Int32, queue_size=10)
        
        pub.publish(h)
                
    def callback(self,instance):
        self.SSID=instance.text
        a=self.SSID.strip()
        a=a.replace(' ','\ ')
        ssid_quoted =f"'{a}'"
        print(ssid_quoted)
        command2 = f"nmcli dev wifi connect '{ssid_quoted}'"
        
        #catkin_workspace_path = "/home/racer/catkin_ws/devel/setup.bash"
        #command2 = f"source {catkin_workspace_path} && {nmcli_command}"
        full_command = f"gnome-terminal --tab --title='WiFi Scan' -- bash -c '{command2} ; exec bash'"
        print(full_command)
        subprocess.run(full_command, shell=True)

        
    def show_wifi_popup(self):
        wifi_networks, status = self.get_wifi_networks()

        content = BoxLayout(orientation='vertical', spacing=10, padding=30, size_hint=(None, None), size=(400, 350))
        
        # Switch layout
        switch_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height='50dp', padding='10dp')
        wifi_switch = MDSwitch(active=False)
        wifi_switch.bind(active=self.on_wifi_switch_active)
        switch_layout.add_widget(Label( size_hint_x=0.7, width='50dp', halign='right'))
        switch_layout.add_widget(wifi_switch)
        content.add_widget(switch_layout)

        # Label for available networks
        content.add_widget(Label(text="Available Wi-Fi Networks:", size_hint_y=None, height='30dp'))

        # Scroll view and grid layout for Wi-Fi networks
        scroll_view = ScrollView(size_hint=(1, 1))
        grid_layout = GridLayout(cols=1, spacing=20, size_hint_y=None)
        grid_layout.bind(minimum_height=grid_layout.setter('height'))

        wifi_networks = set(wifi_networks[1:])
        for network in wifi_networks:
            if network.strip() != "SSID":
                if network.strip() == status.strip():
                    btn = Button(text=network, size_hint_y=None,background_color=(240/255, 240/255, 240/255,1),height=50)
                else:
                    btn = Button(text=network, size_hint_y=None,background_color=(240/255, 240/255, 240/255,0.2),height=50)
                btn.bind(on_press=self.callback)
                grid_layout.add_widget(btn)

        scroll_view.add_widget(grid_layout)
        content.add_widget(scroll_view)

        wifi_popup = Popup(
            title='Wi-Fi Connections',
            content=content,
            size_hint=(None, None),
            size=(400, 350),
            background_color=(240/255, 240/255, 240/255,0.4),
            separator_color=(226/255, 80/255, 16/255, 0.5)
        )
        wifi_popup.open()
    def show_popup1(self):
        self.root.current="nav"
        self.wifi_pass()   
    def wifi_pass(self):
       
        pas= self.root.ids.user.text
        if pas=="1234":
            Window.minimize()
    def on_wifi_switch_active(self, switch ,value):
        if value:
            print("Wi-Fi switch is ON")
           
        else:
            print("Wi-Fi switch is OFF")
            

    def update_icon(self,*args):
        # Simulating the DAC value received
        dac_value = self.get_dac_value()

        # Update the icon based on the DAC value
        if dac_value < 10:
            self.icon_name = "battery-20"
        elif 10 <= dac_value < 20:
            self.icon_name = "battery-40"
        else:
            self.icon_name = "battery-60"

    def get_dac_value(self):
        # This method should return the DAC value.
        # Replace with actual code to get DAC value.
        import random
        return random.randint(0, 30)

        
  

if __name__=="__main__":
    
    Window.borderless=True
    catkin_workspace_path = "/home/crobot/crobot_ws/devel/setup.bash"
    command3= f"source {catkin_workspace_path} &&  roscore"
    full_command = f"gnome-terminal --tab --title='Tab 1' --command='bash -c \"{command3}; exec bash\"'"
    subprocess.Popen(full_command, shell=True) 
    rospy.init_node('hello')

    
    Window.fullscreen='auto'
    Config.set('kivy','exit_on_escape','0')
    catkin_workspace_path = "/home/crobot/crobot_ws/devel/setup.bash"
    command2 = f"source {catkin_workspace_path} &&  rosrun ros_teleop vel.py"
    full_command = f"gnome-terminal --tab --title='Tab 1' --command='bash -c \"{command2}; exec bash\"'"
    subprocess.Popen(full_command, shell=True) 
 


    FirstKVfileApp().run()
    rospy.spin()
