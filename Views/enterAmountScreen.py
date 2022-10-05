from screen import Screen, bgcolors 

class EnterAmountScreen:
    def __init__(self):
        self.amountScreen = Screen(bgcolors.MANGENTABG)
        self.mainContainer = self.amountScreen.drawContainer(13,60)
        self.amountScreen.textToContainer(self.mainContainer,'    Laitettava summa (2/2)')
        self.moneyContainer = self.amountScreen.drawContainer(3,25, bgcolors.CONTAINERBG, False, self.mainContainer, [20,2] )
        self.amountScreen.textToContainer(self.moneyContainer,  'Määrä (1 - 900(sadat)):')
        self.amountScreen.textToContainer(self.moneyContainer, '100e', 1)
        self.amountScreen.saveDisplay()
        
        self.options(True)
        self.optionOne = True

    def addAmountInOrder(self,num):
        self.amountScreen.textToContainer(self.moneyContainer, num, 1)
        self.render()


    def options(self,toggle = None):
        if toggle == None:
            return self.optionOne

        self.amountScreen.applySave()
        self.optionOne = toggle
        if toggle:
            self.planeOneContainer = self.amountScreen.drawContainer(3,12, bgcolors.CYANBG , False, self.mainContainer, [10,7])
            self.amountScreen.textToContainer(self.planeOneContainer,'+')
            self.amountScreen.textToContainer(self.planeOneContainer,'Hyväksy!',1)
            self.planeTwoContainer = self.amountScreen.drawContainer(3,12, bgcolors.DARK_GRAY , False, self.mainContainer, [35,8], False)
            self.amountScreen.textToContainer(self.planeTwoContainer,'+')
            self.amountScreen.textToContainer(self.planeTwoContainer,'Palaa',1)
            
        else:
            self.planeOneContainer = self.amountScreen.drawContainer(3,12, bgcolors.DARK_GRAY , False, self.mainContainer, [10,8], False)
            self.amountScreen.textToContainer(self.planeOneContainer,'+')
            self.amountScreen.textToContainer(self.planeOneContainer,'Hyväksy!',1)
            self.planeTwoContainer = self.amountScreen.drawContainer(3,12, bgcolors.CYANBG , False, self.mainContainer, [35,7])
            self.amountScreen.textToContainer(self.planeTwoContainer,'+')
            self.amountScreen.textToContainer(self.planeTwoContainer,'Palaa',1)
    
    def render(self):
        Screen.active = 1
        self.amountScreen.render()
    