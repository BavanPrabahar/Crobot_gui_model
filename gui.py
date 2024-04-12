import kivy
from kivy.config import Config
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
import time
from kivy.clock import Clock
from datetime import datetime
from kivy.uix.popup import Popup
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivy.properties import NumericProperty
import subprocess
import alsaaudio
import keyboard 
import rospy
from std_msgs.msg import Int32




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

    x = NumericProperty(0)
    y = NumericProperty(0)

    def build(self):

        self.theme_cls.colors = Colors
        self.theme_cls.primary_palette = "Orange"
        

        # self.theme_cls.primary_palette = "DeepOrange"               #for the fab button 
        # self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_hue= "200"

       
       
        Clock.schedule_interval(self.update_time_date, 1)

        Window.borderless=True

        

        


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

    def btn1(self):
        catkin_workspace_path = "/home/crobot/crobot_ws/devel/setup.bash"
        command1 = f"source {catkin_workspace_path} && roslaunch ros_teleop ubot_run.launch"
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
            
        
    def btn5(self):
        catkin_workspace_path = "/home/crobot/crobot_ws/devel/setup.bash"
        command1 = f"source {catkin_workspace_path} && roslaunch hello a.launch"
        full_command = f"gnome-terminal --tab --title='Tab 1' --command='bash -c \"{command1}; exec bash\"'"
        subprocess.Popen(full_command, shell=True)  
    def btn3(self):
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