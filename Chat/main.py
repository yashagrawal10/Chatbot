from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.label import MDLabel
from kivy.properties import StringProperty, NumericProperty
from kivy.core.text import LabelBase
from kivy.clock import Clock
import requests
Window.size = (350, 550)

class Command(MDLabel):
    text = StringProperty()
    size_hint_x = NumericProperty()
    halign = StringProperty()
    font_name = "Poppins"
    font_size = 17
class ChatBot(MDApp):

    def change_screen(self, name):
        screen_manager.current = name

    def build(self):
        global screen_manager
        screen_manager = ScreenManager()
        screen_manager.add_widget(Builder.load_file("main.kv"))
        screen_manager.add_widget(Builder.load_file("chats.kv"))
        return screen_manager

        name_base = str({bot-name})
        name_base = name_base.replace("\'","")
    def bot_name(self):
        if screen_manager.get_screen('main').bot_name.text != "":
            screen_manager.get_screen('Chats').bot_name.text = screen_manager.get_screen('main').bot_name.text
            screen_manager.current = "Chats"

    def send(self):
        global  size, halign, value

        if screen_manager.get_screen('Chats').text_input != "":
            value = screen_manager.get_screen('Chats').text_input.text

            if len(value) < 6:
                size = .22
                halign = "center"

            elif  len(value) < 11:
                size = .32
                halign = "center"
            elif  len(value) < 16:
                size = .45
                halign = "center"
            elif  len(value) < 21:
                size = .58
                halign = "center"
            elif  len(value) < 26:
                size = .71
                halign = "center"
            else:
                size = .77
                halign = "left"

            screen_manager.get_screen('Chats').chat_list.add_widget(Command(text=value,size_hint_x=size, halign=halign))

            screen_manager.get_screen('Chats').text_input.text = ""



if __name__ == '__main__':
    LabelBase.register(name="Poppins", fn_regular="Poppins-Regular.ttf")
    ChatBot().run()