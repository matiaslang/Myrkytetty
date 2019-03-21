from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.config import Config
from kivy.uix.popup import Popup
from kivy.uix.button import Button

Config.set('graphics', 'width', '1000')
Config.set('graphics', 'height', '600')
mies = False
nainen = False

class CalcClass():
    gender = ""
    age = 0

    def __init__(self):
        self.gender = " "
        self.age = 0

    def MaleButton(self):
        self.gender = "male"

    def FemaleButton(self):
        self.gender = "female"

    def TulostaTulos(self):
        print("SUKUPUOLENA ON ", self.gender)

class MainScreen(Screen):
    pass

class AlkometriEka(Screen):
    mies = False
    nainen = False

    def __init__(self, **kwargs):
        super(Screen, self).__init__(**kwargs)

    def FemaleButton(self):
        CalcClass.FemaleButton(self)
        print("Naista on painettu")

    def maleButton(self):
        CalcClass.MaleButton(self)
        print("MIESTÄ ON PAINETTU")

    def tulostus(self):
        CalcClass.TulostaTulos(self)

    pass

class ScreenManagement(ScreenManager):
    pass

#class AuditMittari(ScreenManager)


presentation = Builder.load_file("Myrkytetty.kv")



class MainApp(App):
    def build(self):
        return presentation

MainApp().run()