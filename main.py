import msvcrt

from Views.enterAmountScreen import EnterAmountScreen
from Views.mainScreen import MainScreen
from modules.bank import Bank
from screen import Screen

#Pankki
bank = Bank()

#Näytöt
mainScreen = MainScreen()
enterAmountScreen = EnterAmountScreen()

amount = 1
mainScreen.displayMoney(bank.tiliote())
mainScreen.render()

while True:
    if msvcrt.kbhit():
        key = ord(msvcrt.getch())
        if key == 77: #Down arrow
            if mainScreen.options() and Screen.active == 0:
                mainScreen.options(int(False))
                mainScreen.displayMoney(bank.tiliote())
                mainScreen.render()
            elif enterAmountScreen.options() and Screen.active == 1:
                enterAmountScreen.options(int(False))
                enterAmountScreen.addAmountInOrder(str(amount))
                enterAmountScreen.render()
        elif key == 75 : #Up arrow
            if not mainScreen.options() and Screen.active == 0:
                mainScreen.options(int(True))
                mainScreen.displayMoney(bank.tiliote())
                mainScreen.render()
            elif not enterAmountScreen.options() and Screen.active == 1:
                enterAmountScreen.options(int(True))
                enterAmountScreen.addAmountInOrder(str(amount))
                enterAmountScreen.render()
        elif key == 13 :
            if not mainScreen.options() and Screen.active == 0: #Näytä seuraava näyttö
                print('\nPoistuit!')
                break

            if mainScreen.options() and Screen.active == 0: #Näytä seuraava näyttö
                enterAmountScreen.render()
            elif Screen.active == 1: # Syötä arvo
                if enterAmountScreen.options():
                    bank.talleta(int(amount) * 100)
                    mainScreen.displayMoney(bank.tiliote())
                mainScreen.render()
    
        if Screen.active == 1:
            if key >= 49 and key <= 57:
                #print(chr(key))
                amount = chr(key)
                enterAmountScreen.addAmountInOrder(chr(key))
           

