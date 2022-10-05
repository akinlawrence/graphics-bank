import copy
import os
import sys
  
class bgcolors:
    DARK_GRAY = '\x1b[37m'
    CYANBG = '\x1b[1;36;46m'
    BLACKBG = '\x1b[44m'
    MANGENTABG ='\u001b[45m'
    RESET = '\x1b[0m'
    CONTAINERBG = '\x1b[47m'
    BOXSHADOW = '\x1b[40m'

class Screen:
    __display = []
    __displaySave = []
    active = 0

    def __init__(self, defaultColor = bgcolors.BLACKBG):
        self.__display.clear()
        #try:
        #    print(self.__display)
        #except:
        #    print('not existing')
        self.__size = os.get_terminal_size()

        if self.__size.lines < 15:
            print('Terminaalin ikkuna on liian pieni. Suurenna ja paina run uudestaan!')
            exit()

        
        for i in range(self.__size.lines):
            self.__display.append([]) 
            for j in range(self.__size.columns):
                self.__display[i].append(defaultColor+' ')

    def saveDisplay(self):
        self.__displaySave = copy.deepcopy( self.__display)

    def applySave(self):
        self.__display = copy.deepcopy( self.__displaySave)

    def initScreen(self):
        for i in range(self.__size.lines):
            for text in self.__display[i] :
                print(bgcolors.BLACKBG, end='')
                #print(bgcolors.BLACKBG + text, end='')
            print('')
        print(bgcolors.RESET)

    def textToContainer(self,container, text, row = 0):
        for index, letter in enumerate(text):
            self.__display[container[1] + row][container[0]+ index] =  bgcolors.CONTAINERBG+ '\033[30m' + letter


    def moveXY(self,y,x):
        sys.stdout.write("\033[%d;%dH" % (y, x)) #https://stackoverflow.com/questions/54630766/how-can-move-terminal-cursor-in-python

    def render(self):
        self.moveXY(0,0)
        #self.__size.lines - 1 <-- viimeinen rivi aiheuttaa välkkymistä, joten poisteaaan
        for i in range(self.__size.lines - 1):
            for text in self.__display[i] :
                print(text , end='')
                #print(bgcolors.BLACKBG + text, end='')
            print('')
        print(bgcolors.RESET, end='')
        self.moveXY(self.__size.lines - 1,self.__size.columns)

    def drawContainer(self, height, width, color = bgcolors.CONTAINERBG, center =True, location= [0,0], offset= [0,0], shadow = True ):
        if center:
            startY = round((self.__size.lines / 2) + (height/2)) -1
            startX = round((self.__size.columns / 2) - (width/2))

                        #Varjon piirto
            if shadow:
                for i in range(height):
                    for j in range(width):
                        self.__display[startY -i+ 1][startX + 2 + j] = bgcolors.BOXSHADOW  + " "

            # Laatinkon päälle piirto
            for i in range(height):
                for j in range(width):
                    boxCordination = [startX , startY -i]
                    self.__display[startY -i][startX  + j] = color  + " "
            return boxCordination
        else:
            startY = location[1]
            startX = location[0]

                       #Varjon piirto
            if shadow:
                for i in range(height):
                    for j in range(width):
                        self.__display[startY +offset[1] +i+ 1][startX +offset[0] + 2 + j] = bgcolors.BOXSHADOW  + " "

            # Laatinkon päälle piirto
            for i in range(height):
                for j in range(width):
                    boxCordination = [startX +offset[0]  , startY + offset[1] ]
                    self.__display[startY +offset[1] +i][startX +offset[0] + j] = color  + " "
            return boxCordination

    def drawWindow(self):
        for i in range(self.__size.lines):
            for text in self.__display[i] :
                print(bgcolors.BLACKBG, end='')
                #print(bgcolors.BLACKBG + text, end='')
            print('')
        print(bgcolors.RESET)
