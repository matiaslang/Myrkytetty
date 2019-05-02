from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.config import Config
from kivy.properties import StringProperty
from kivy.uix.popup import Popup
from kivy.uix.button import Button

Config.set('graphics', 'width', '1000')
Config.set('graphics', 'height', '600')

Builder.load_file('./AuditScreen.kv')
Builder.load_file('./AlcometerScreen1.kv')
Builder.load_file('./chooseDrinks.kv')
Builder.load_file('./Report.kv')

Drinkscount = None
PersonInfo = None

def calculateHowDrunk():
    annokset = Drinkscount.calculatePortions()
    weight = PersonInfo.weightOf
    gender = PersonInfo.gender
    hours = PersonInfo.hoursSince
    personVolume = 0
    if(gender == "male"):
        personVolume = 0.75
    if (gender == "female"):
        personVolume = 0.66

    if(annokset > 0):
        palaminen = (0.1*weight)*hours
        promillet = ((((0.79) * (((4.7 * (330 / 100))) )) * annokset)-palaminen) / ((personVolume * (weight))*1000)
        promillet = round((promillet * 1000),1)
    else:
        promillet = 0
    return promillet




class DrinkCounter(object):
    portions = 0
    o1 = 0
    o2 = 0
    s1 = 0
    s2 = 0
    v1 = 0
    v2 = 0
    v3 = 0
    v4 = 0
    j1 = 0
    j2 = 0
    j3 = 0
    k1 = 0
    k2 = 0
    k3 = 0
    def __init__(self):
        self.portions = 0
        self.o1 = 0
        self.o2 = 0
        self.s1 = 0
        self.s2 = 0
        self.v1 = 0
        self.v2 = 0
        self.v3 = 0
        self.v4 = 0
        self.j1 = 0
        self.j2 = 0
        self.j3 = 0
        self.k1 = 0
        self.k2 = 0
        self.k3 = 0

    def calculatePortions(self):
        self.portions = self.o1 + (self.o2 * 1.5) + (self.s1 * 1.25) + (self.s2 * 2) + (self.v1) + (self.v2 * 1.25) + (self.v3 * 4) + (self.v4 * 7) + (self.j1) + (self.j2 * 4.5) + (self.j3 * 9) + self.k1 + (self.k2 * 13) + (self.k3 * 17)
        return self.portions

    def addPortions(self, portion, type):
        if(type == "o1"):
            self.o1 = portion
        elif (type == "o2"):
            self.o2 = portion
        elif (type == "s1"):
            self.s1 = portion
        elif (type == "s2"):
            self.s2 = portion
        elif (type == "v1"):
            self.v1 = portion
        elif (type == "v2"):
            self.v2 = portion
        elif (type == "v3"):
            self.v3 = portion
        elif (type == "v4"):
            self.v4 = portion
        elif (type == "j1"):
            self.j1 = portion
        elif (type == "j2"):
            self.j2 = portion
        elif (type == "j3"):
            self.j3 = portion
        elif (type == "k1"):
            self.k1 = portion
        elif (type == "k2"):
            self.k2 = portion
        elif (type == "k3"):
            self.k3 = portion
        #print(Drinkscount.calculatePortions())





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
        self.portions =0

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
        PersonInfo.FemaleButton()
        if (PersonInfo.firsScreenReady()):
            self.ids.NextButton.disabled = False

    def maleButton(self):
        PersonInfo.MaleButton()
        if (PersonInfo.firsScreenReady()):
            self.ids.NextButton.disabled = False

    def hours(self, number):
        PersonInfo.hoursStarted(number)
        if(PersonInfo.firsScreenReady()):
            self.ids.NextButton.disabled = False

    def weight(self, weightNumber):
        if (PersonInfo.firsScreenReady()):
            self.ids.NextButton.disabled = False
        PersonInfo.weightInit(weightNumber)

    def tulostus(self):
        print(PersonInfo.TulostaTulos(self))


    pass

class chooseDrinks(Screen):

    def __init__(self, **kwargs):
        super(Screen, self).__init__(**kwargs)
        DrinkCounter.__init__(self)

    def addDrinks(self, portion, type):
        Drinkscount.addPortions(int(portion),type)

    def updatePerce(self):
        ReportScreen.getDrinks(self)
    pass




class ScreenManagement(ScreenManager):
    pass

class AuditMittari(Screen):
    pass

class ReportScreen(Screen):
    portions = "  "
    def __init__(self, **kwargs):
        super(ReportScreen, self).__init__(**kwargs)
        #self.portions = str(calculateHowDrunk())

    def getDrinks(self):
        self.portions = str(calculateHowDrunk())

    def printIt(self):
        self.portions = str(calculateHowDrunk())
        print(calculateHowDrunk())
        print(self.portions)

    def test(self):
        self.portions = str(calculateHowDrunk())
        self.textForLabel.text = self.portions

    pass


presentation = Builder.load_file("Myrkytetty.kv")



class MainApp(App):
    global Drinkscount
    global PersonInfo
    Drinkscount = DrinkCounter()
    PersonInfo = CalcClass()
    def build(self):
        return presentation

#MainApp().run()

if __name__ == "__main__":
    MainApp().run()