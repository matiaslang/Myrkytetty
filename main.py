from kivy.app import App

from kivy.uix.scatter import Scatter
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout

class MenuScreen(Screen):
    pass

class SeuraavaSivu(Screen):
    pass

sm = ScreenManager()
sm.add_widget(MenuScreen(name = 'menu'))
sm.add_widget(SeuraavaSivu(name = 'next'))


class ScatterTextWidget(BoxLayout):
    pass

class Myrkytetty(App):
    #TODO MUISTA TEHDÄ ASIOITA
    def build(self):
        return sm


if __name__ == "__main__":
    Myrkytetty().run()
