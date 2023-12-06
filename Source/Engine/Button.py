from __future__ import annotations
import pygame

from Source.Engine.Entity import Entity

pygame.init()

class Button(Entity):

    def defaultFunc(param):
        print(param)

    def __init__(self, positionX : int = 0, positionY : int = 0, positionZ : int = 0, bodyWidth : int = 100, bodyHeight : int = 100, text : str = "Crazy Maze", textColor : tuple = (255, 255, 255), size : int = 20, buttonFunction = [defaultFunc], param = ["Test"]):

        super().__init__(positionX, positionY, positionZ, bodyWidth, bodyHeight)
        
        self.text : str = text
        self.textSize : int = size
        self.textColor : tuple = textColor
        self.colorBg : tuple = (0, 0, 0)
        self.colorUnhover : tuple = (255, 255, 255)
        self.colorHover : tuple = (128, 128, 128)
        self.colorClicked : tuple = (47,79,79)
        self.font : pygame.font = pygame.font.SysFont('Arial', self.textSize, True)
        self.rect : pygame.Rect = pygame.Rect(positionX, positionY, bodyWidth, bodyHeight)
        self.textRect : pygame.Rect = pygame.Rect(100, 100, 100, 100)
        self.textFont = self.font.render(self.text, True, self.textColor)

        self.alreadyPressed : bool = False
        self.func = buttonFunction
        self.param = param


    def update(self):
        
        self.onClick(pygame.mouse.get_pos())
    

    def onClick(self, mousePos : tuple) -> None:
        
        self.colorBg = self.colorUnhover
        if self.rect.collidepoint(mousePos):
            self.colorBg = self.colorHover
            self.setRect()
            if pygame.mouse.get_pressed(num_buttons = 3)[0]:
                self.colorBg = self.colorClicked
                if not self.alreadyPressed:
                    try:
                        for i in range(len(self.func)):
                            self.func[i](self.param[i])
                    except:
                        print("Error while calling function at button", self.text)
                    self.alreadyPressed = True
                    return True
            else:
                self.alreadyPressed = False


    #set Methods
    
    
    def setFunc(self, func) -> None:

        self.func = func


    def setParam(self, param : list) -> None:

        self.param = param


    def setTextSize(self, size : int) -> None:

        self.textsize = size


    def setTextFont(self) -> None:

        self.textFont = self.font.render(self.text, True, self.textColor)


    def setRect(self) -> None:

        self.rect = pygame.Rect(self.positionX, self.positionY, self.bodyWidth, self.bodyHeight)
    
    
    def setTextRect(self) -> None:

        self.textRect = self.textFont.get_rect(center = (self.positionX + (self.bodyWidth / 2), self.positionY + self.bodyHeight / 2))


    def setText(self, text : str) -> None:

        self.text = text
        self.setTextFont()
        self.setTextRect()


    def setFont(self, font : pygame.font, fontSize : int) -> None:

        self.font = pygame.font.SysFont(font, fontSize)

    
    def setBgColor(self, color : tuple) -> None:

        self.colorBg = color
        self.colorUnhover = color


    #get Methods


    def getTextFont(self) :

        return self.textFont


    def getText(self) -> str:

        return self.text
    

    def getRect(self) -> pygame.Rect:

        return self.rect
    

    def getTextRect(self) -> pygame.Rect:

        return self.textRect


    def getBgColor(self) -> tuple:

        return self.colorBg

    #def getCommand(self) -> str:
        
     #   return self.__command
