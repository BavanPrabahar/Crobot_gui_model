#i can add

import pyautogui
import multiprocessing
import kivy
import multiprocessing
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
from kivy.properties import BooleanProperty
from playsound import playsound
import alsaaudio
from kivy.input.providers.mouse import MouseMotionEvent
from kivy.graphics import *
from kivymd.uix.spinner import MDSpinner
a=0
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
    },
    "Red": {
                "50": "FFEBEE",
                "100": "FFCDD2",
                "200": "EF9A9A",
                "300": "E57373",
                "400": "EF5350",
                "500": "F44336",
                "600": "E53935",
                "700": "D32F2F",
                "800": "C62828",
                "900": "B71C1C",
                "A100": "FF8A80",
                "A200": "FF5252",
                "A400": "FF1744",
                "A700": "D50000"
            }
}





class FirstKVfileApp(MDApp): 
    SSID=None
    x = NumericProperty(0)
    y = NumericProperty(0)
    b=[]
    w=None
    l=None
    icon_name = StringProperty("wifi")
    
    vol=100
    t=0
    #m.setvolume(vol)
    angle=NumericProperty(360)
   
    active=BooleanProperty(True)
    
    def build(self):
        
        self.theme_cls.colors = Colors
        self.theme_cls.primary_palette = "Orange"
       

        # self.theme_cls.primary_palette = "DeepOrange"               #for the fab button 
        # self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_hue= "200"

        
       
        Clock.schedule_interval(self.update_time_date, 1)
        Clock.schedule_interval(self.u, 1 / 100)
        Clock.schedule_interval(self.check,8)
        Clock.schedule_interval(self.check1,2)
        Clock.schedule_interval(self.vol_set,1/2)
        #Clock.schedule_interval(self.bms, 1 / 100)

     

        Window.borderless=True

 

 


        return Builder.load_file("new.kv")
    def vol_set(self,*args):
        m=alsaaudio.Mixer()
        self.vol = m.getvolume()
        #self.root.ids.volume_slider_1.value =self.vol
           
    def u(self, dt):
        # Increment the angle to rotate continuously
        self.angle -= 1
        if self.angle <=0:
            self.angle =360

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

    def slider_volume_change(self, value,*args):
        x=int(value)
        print(x)
        m = alsaaudio.Mixer()
        m.setvolume(x)
        self.vol = m.getvolume()

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
    def kill(self):


        catkin_workspace_path = "/home/racer/catkin_ws/devel/setup.bash"
        command1 = f"source {catkin_workspace_path} && rosnode kill --all"
        full_command = f"gnome-terminal --tab --title='Tab 1' -- bash -c \"{command1}; echo; echo 'Output captured, closing in 5 seconds...'; sleep 5; exit\""
        subprocess.Popen(full_command, shell=True)

    def show(self):
        self.root.current="nav1"


        catkin_workspace_path = "/home/racer/catkin_ws/devel/setup.bash"
        command1 = f"source {catkin_workspace_path} && rosrun teleop_twist_keyboard teleop_twist_keyboard.py"
        full_command = f"gnome-terminal --tab --title='Tab 1' -- bash -c \"{command1}; echo; echo 'Output captured, closing in 5 seconds...'; sleep 5; exit\""
        subprocess.Popen(full_command, shell=True)


    def show_popup(self):
        self.dialog = MDDialog(
            title="Hello, User",
            text="Do you want to proceed with the recorded data?",
            buttons=[
                MDFlatButton(
                    text="[b]START OVER[b]", on_release=self.close_popup
                ),
                MDFlatButton(
                    text="[b]PROCEED[b]", on_release= self.proceed
                ),

            ],
        )
        self.dialog.open()
    
    def hel(self):
        catkin_workspace_path = "/home/racer/catkin_ws/devel/setup.bash"
        command1 = f"source {catkin_workspace_path} && rosrun teleop_twist_keyboard teleop_twist_keyboard.py"
        full_command = f"gnome-terminal --title='Tab 1' -- bash -c \"{command1}; echo; echo 'Output captured, closing in seconds...'; exit\""
        subprocess.Popen(full_command, shell=True)




    def close_popup(self):
        self.wifi_popup.dismiss()

    def proceed(self, obj):
        self.root.current="fifth_screen"

        if self.root.current=="fifth_screen":
            self.dialog.dismiss()

    def get_wifi_networks(self):
        co="nmcli radio wifi "
        ful = f"gnome-terminal --tab --title='z' -- bash -c '{co}; echo; echo \"Output captured, closing in 5 seconds...\"; sleep 5; exit'"
        subprocess.Popen(ful, shell=True)
        p2=subprocess.Popen(f"bash -c '{co}'", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        
        self.z = p2.stdout.readline()
      
        subprocess.run("bash -c 'kill'",shell=True)
            

        if self.z.strip()=="disabled":
            self.b==0   

        else:
            #catkin_workspace_path = "/home/racer/catkin_ws/devel/setup.bash"
            command2= " nmcli -f SSID device wifi list"
            #command2 = f"source {catkin_workspace_path} && {nmcli_command}"
            #command3="nmcli radio wifi "
            #command2=f"{command21}&&{command3}"
            full_command = f"gnome-terminal --tab --title='WiFi Scan' -- bash -c '{command2}; echo; echo \"Output captured, closing in 5 seconds...\"; sleep 5; exit'"
            
            subprocess.Popen(full_command, shell=True)
            p= subprocess.Popen(f"bash -c '{command2}'", shell=True,  stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            
            while p.poll() is None:
                self.l = p.stdout.readline()
                if self.l:
                    
                    self.b.append(self.l)
                    
                    if len(self.b) >= 20:
                        break
            pyautogui.hotkey('ctrl', 'c')
        command3 = f"nmcli -t -f NAME connection show --active"
        full_command3 = f"gnome-terminal --tab --title='conn Scan' -- bash -c '{command3}; echo; echo \"Output captured, closing in 5 seconds...\"; sleep 5; exit'"
      
        subprocess.Popen(full_command3, shell=True)
        p1 = subprocess.Popen(f"bash -c '{command3}'", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
      
        self.w = p1.stdout.readline()
       
      
        return self.b,self.w,self.z
 

    def callback(self,instance):
        self.SSID=instance.text
        a=self.SSID.strip()
        a=a.replace(' ','\ ')
        a=a.replace("'","\'")
        a=a.replace("^",'\^')
        ssid_quoted =f"'{a}'"
        print(ssid_quoted)
        
        command2 = f"nmcli dev wifi connect '{ssid_quoted}'"
        
        #catkin_workspace_path = "/home/racer/catkin_ws/devel/setup.bash"
        #command2 = f"source {catkin_workspace_path} && {nmcli_command}"
        full_command = f"gnome-terminal --tab --title='WiFi Scan' -- bash -c '{command2}; echo; echo \"Output captured, closing in 5 seconds...\"; sleep 5; exit'"
        
        subprocess.run(full_command, shell=True)
    def check(self,*args):
        if self.t==1:
            self.button.trigger_action(duration=0.1)
            self.t=0
        else:
            pass
    def check1(self,*args):
        if self.t==2:
            self.button.trigger_action(duration=0.1)
            self.t=0
        else:
            pass

        
    def aaa(self):
        print("hello")
#         MDSpinner(
#     size_hint=(None, None),
#     size=(46, 46),
#     pos_hint={'center_x': .5, 'center_y': .5},
#     active=True,
#     palette=[
#         [0.28627450980392155, 0.8431372549019608, 0.596078431372549, 1],
#         [0.3568627450980392, 0.3215686274509804, 0.8666666666666667, 1],
#         [0.8862745098039215, 0.36470588235294116, 0.592156862745098, 1],
#         [0.8784313725490196, 0.9058823529411765, 0.40784313725490196, 1],
#     ]
# )




       
       
    # def show_wifi_popup(self,*args):
    #     p1=multiprocessing.process(target=self.aaa,args=())
    #     p2=multiprocessing.process(target=self.show_s,args=())

    #     p1.start()
    #     p2.start()
    #     p1.join()
    #     p2.join()

  
        
    def show_wifi_popup(self,*args):

        self.root.ids.spinner.active = True
        
        wifi_networks, status, h= self.get_wifi_networks()

        content = BoxLayout(orientation='vertical', spacing=10, padding=30, size_hint=(None, None), size=(550, 450))
        
        # Switch layout
        switch_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height='50dp', padding='10dp')
        
        self.wifi_switch = MDSwitch()
        

        if self.z.strip()=="disabled":
            self.wifi_switch.active=False
        else:
            self.wifi_switch.active=True
    
        switch_layout.add_widget(Label( size_hint_x=1, width='100dp', halign='right'))
        switch_layout.add_widget(self.wifi_switch)
        content.add_widget(switch_layout)
        self.wifi_switch.bind(active=self.on_wifi_switch_active)
        # Label for available networks
        content.add_widget(Label(text="Available Wi-Fi Networks:", size_hint_y=None, height='30dp'))
    
        # Scroll view and grid layout for Wi-Fi networks
        scroll_view = ScrollView(size_hint=(1, 1))
        grid_layout = GridLayout(cols=1, spacing=20, size_hint_y=None)
        grid_layout.bind(minimum_height=grid_layout.setter('height'))

        wifi_networks = set(wifi_networks[1:-1])

        if self.z.strip()=="disabled":
            pass
        
        else:
            
            for network in wifi_networks:
                if network.strip() != "SSID":
                    if network.strip() == status.strip() :
                            
                        btn = Button(text=network, size_hint_y=None,background_color=(240/255, 240/255, 240/255,1),height=50)
                    else:
                        btn = Button(text=network, size_hint_y=None,background_color=(240/255, 240/255, 240/255,0.2),height=50)
                    btn.bind(on_press=self.callback)
                    grid_layout.add_widget(btn)

        
        scroll_view.add_widget(grid_layout)
        content.add_widget(scroll_view)

        self.wifi_popup = Popup(
            title='Wi-Fi Connections',
            content=content,
            size_hint=(None, None),
            size=(550, 450),
            background_color=(240/255, 240/255, 240/255,0.4),
            separator_color=(226/255, 80/255, 16/255, 0.5)
        )
        self.wifi_popup.open()
        self.icon_name="wifi"
    def show_popup1(self):
        self.root.current="nav"
        self.wifi_pass()
        
    def wifi_pass(self):
       
        pas= self.root.ids.user.text
        if pas=="1234":
            Window.minimize()
    def on_wifi_switch_active(self, switch ,value):
        
        print(value)
        if value==True:

            self.t=0
            command2 = f"nmcli radio wifi on"
        
        
            full_command = f"gnome-terminal --tab  --title='wifi on' -- bash -c '{command2}; echo; echo \"Output captured, closing in 5 seconds...\"; sleep 5; exit'"
            
            subprocess.Popen(full_command, shell=True)  
            self.close_popup()
           
            self.button = self.root.ids.my_button
            self.z=None
            self.b=[None in range(0,20)]
            self.w=0
            self.t=1
            

                     

        elif value==False:
            self.t=0
            command3 = f"nmcli radio wifi off"
            
            full_command1 = f"gnome-terminal --tab  --title='wifi on' -- bash -c '{command3}; echo; echo \"Output captured, closing in 5 seconds...\"; sleep 5; exit'"
            
            subprocess.Popen(full_command1, shell=True)
            self.close_popup()
            self.button = self.root.ids.my_button
            self.z=None
            self.b=[None in range(0,20)]
            self.w=0
            
            self.t=2
          
    def bms(self):
        commandb = f"ls"
        full_commandb = f"gnome-terminal --tab --title='conn Scan' -- bash -c '{commandb}; echo; echo \"Output captured, closing in 5 seconds...\"; sleep 5; exit'"
      
        subprocess.Popen(full_commandb, shell=True)
        p1 = subprocess.Popen(f"bash -c '{commandb}'", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
      
        x = p1.stdout.readline()
        dac=(3.3*x)/4096
        bat_v=(dac-1.9127)/0.0294
        if 28<bat_v<=29.4:
            self.icon_name="battery"
        elif 26.6<bat_v<=28:
            self.icon_name="battery-80"
        elif 25.2<bat_v<=26.6:
            self.icon_name="battery-60"
        elif 23.8<bat_v<=25.2:
            self.icon_name="battery-40"
        elif bat_v<23.8:
            self.icon_name="battery-20"
            self.root.ids.bat.text_color=(1,0,0,1)
        
        



           
          
            



      




if __name__=="__main__":
    # Window.borderless=True

    #Window.fullscreen = 'auto'
    FirstKVfileApp().run()
