from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.config import Config
Config.set('graphics', 'width', '1000')
Config.set('graphics', 'height', '600')
mies = False
nainen = False

class MainScreen(Screen):
    pass

class AlkometriEka(Screen):
    mies = False
    nainen = False

    def __init__(self, **kwargs):
        super(Screen, self).__init__(**kwargs)

    def maleButton(self):
        mies = True
        print("MIESTÄ ON PAINETTU")
    pass

class ScreenManagement(ScreenManager):
    pass

presentation = Builder.load_file("Myrkytetty.kv")



class MainApp(App):
    def build(self):
        return presentation

MainApp().run()