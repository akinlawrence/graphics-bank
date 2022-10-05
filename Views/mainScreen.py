from screen import Screen, bgcolors 

class MainScreen:
    def __init__(self):
        self.mainScreen = Screen()
        self.mainContainer = self.mainScreen.drawContainer(13,60)
        self.mainScreen.textToContainer(self.mainContainer,'    PANKKI V2  - HAMK AUTOMAATTI')
        self.moneyContainer = self.mainScreen.drawContainer(2,22, bgcolors.CONTAINERBG, False, self.mainContainer, [20,3] )
        self.mainScreen.textToContainer(self.moneyContainer,  'Nykyisen saldon määrä:')
        #self.mainScreen.textToContainer(self.moneyContainer, '200e', 1)
        self.mainScreen.saveDisplay()
        self.options(True)
        self.optionOne = True

    def displayMoney(self, money):
        self.mainScreen.textToContainer(self.moneyContainer, str(money)+"e", 1)
    def options(self,toggle = None):
        if toggle == None:
            return self.optionOne

        self.mainScreen.applySave()
        self.optionOne = toggle
        if toggle:
            self.planeOneContainer = self.mainScreen.drawContainer(3,12, bgcolors.CYANBG , False, self.mainContainer, [10,7])
            self.mainScreen.textToContainer(self.planeOneContainer,'+')
            self.mainScreen.textToContainer(self.planeOneContainer,'Laita Rahaa',1)
            self.planeTwoContainer = self.mainScreen.drawContainer(3,12, bgcolors.DARK_GRAY , False, self.mainContainer, [35,8], False)
            self.mainScreen.textToContainer(self.planeTwoContainer,'+')
            self.mainScreen.textToContainer(self.planeTwoContainer,'Poistu',1)
            
        else:
            self.planeOneContainer = self.mainScreen.drawContainer(3,12, bgcolors.DARK_GRAY , False, self.mainContainer, [10,8], False)
            self.mainScreen.textToContainer(self.planeOneContainer,'+')
            self.mainScreen.textToContainer(self.planeOneContainer,'Laita Rahaa',1)
            self.planeTwoContainer = self.mainScreen.drawContainer(3,12, bgcolors.CYANBG , False, self.mainContainer, [35,7])
            self.mainScreen.textToContainer(self.planeTwoContainer,'+')
            self.mainScreen.textToContainer(self.planeTwoContainer,'Poistu',1)
    
    def render(self):
        Screen.active = 0
        self.mainScreen.render()
    