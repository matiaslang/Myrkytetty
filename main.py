from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.config import Config
from kivy.uix.popup import Popup
from kivy.uix.button import Button

Config.set('graphics', 'width', '1000')
Config.set('graphics', 'height', '600')

Builder.load_file('./AuditScreen.kv')
Builder.load_file('./AlcometerScreen1.kv')

class CalcClass():
    gender = " "
    age = 0
    hoursSince = 0
    weightOf = 0

    def __init__(self):
        self.gender = "N/A"
        #self.age = 0
        self.hoursSince = 999
        self.weightOf = 0

    def MaleButton(self):
        self.gender = "male"

    def FemaleButton(self):
        self.gender = "female"

    def hoursStarted(self, hours):
        self.hoursSince = hours

    def weightInit(self, newWeight):
        self.weightOf = newWeight

    def TulostaTulos(self):
        print("SUKUPUOLENA ON {}\nALOITETTU ON {} tuntia sitten\nPainosi on {} kiloa".format(self.gender, self.hoursSince, self.weightOf))


    def firsScreenReady(self):
        if(self.gender != "N/A"  and self.hoursSince != 999 and self.weightOf != 0):
            return True
        else:
            return False

class MainScreen(Screen):
    pass


class AlkometriEka(Screen):


    def __init__(self, **kwargs):
        super(Screen, self).__init__(**kwargs)
        CalcClass.__init__(self)

    def FemaleButton(self):
        CalcClass.FemaleButton(self)
        if (CalcClass.firsScreenReady(self)):
            self.ids.NextButton.disabled = False

    def maleButton(self):
        CalcClass.MaleButton(self)
        if (CalcClass.firsScreenReady(self)):
            self.ids.NextButton.disabled = False

    def hours(self, number):
        CalcClass.hoursStarted(self, number)
        if(CalcClass.firsScreenReady(self)):
            self.ids.NextButton.disabled = False

    def weight(self, weightNumber):
        if (CalcClass.firsScreenReady(self)):
            self.ids.NextButton.disabled = False
        CalcClass.weightInit(self, weightNumber)

    def tulostus(self):
        CalcClass.TulostaTulos(self)


    pass

class ScreenManagement(ScreenManager):
    pass

class AuditMittari(Screen):
    pass


presentation = Builder.load_file("Myrkytetty.kv")



class MainApp(App):
    def build(self):
        return presentation

MainApp().run()