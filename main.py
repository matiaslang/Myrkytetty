from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.config import Config
from kivy.uix.popup import Popup
from kivy.uix.button import Button

Config.set('graphics', 'width', '1000')
Config.set('graphics', 'height', '600')

class MainScreen(Screen):
    pass

class AlkometriEka(Screen):
    pass

class ScreenManagement(ScreenManager):
    pass

#class AuditMittari(ScreenManager)


presentation = Builder.load_file("Myrkytetty.kv")

class MainApp(App):
    def build(self):
        return presentation

MainApp().run()