from __future__ import annotations
import pygame

from Source.Engine.Entity import Entity

pygame.init()

class Button(Entity):

    def defaultFunc():
        print("default")

    def __init__(self, positionX : int = 0, positionY : int = 0, positionZ : int = 0, bodyWidth : int = 100, bodyHeight : int = 100, buttonFunction = defaultFunc, param = None):

        super().__init__(positionX, positionY, positionZ, bodyWidth, bodyHeight)
        
        self.__text : str = ""
        self.__textSize : int = 20
        self.__textColor : tuple = (255, 255, 255)
        self.__bgColor : tuple = (0, 0, 0)
        self.__font : pygame.font = pygame.font.SysFont('Arial', 40)
        self.__rect : pygame.Rect = pygame.Rect(100, 100, 100, 100)
        self.__textFont = self.__font.render(self.__text, True, self.__textColor)

        self.__useable : bool = False
        self.__onePress : bool = True
        self.__command : str = ""
        self.__alreadyPressed : bool = False
        self.func = buttonFunction
        self.param = param

    def __execCommand(self) -> None:

        exec(self.__command)


    def update(self):
        
        self.onClick(pygame.mouse.get_pos())
    

    def onClick(self, mousePos : tuple) -> None:
        
        if self.__rect.collidepoint(mousePos):
            if pygame.mouse.get_pressed(num_buttons = 3)[0]:
                if not self.__alreadyPressed:
                    try:
                        self.func(self.param)
                    except:
                        print("Error while calling function at button", self)
                    self.__alreadyPressed = True
            else:
                self.__alreadyPressed = False


    #set Methods
    
    
    def setFunc(self, func) -> None:

        self.func = func


    def setTextSize(self, size : int) -> None:

        self.__textsize = size


    def setTextFont(self) -> None:

        self.__textFont = self.__font.render(self.__text, True, self.__textColor)


    def setRect(self) -> None:

        self.__rect = self.__textFont.get_rect(center = (self.positionX + (self.bodyWidth / 2), self.positionY + self.bodyHeight / 2))


    def setText(self, text : str) -> None:

        self.__text = text


    def setFont(self, font : pygame.font, fontSize : int) -> None:

        self.__font = pygame.font.SysFont(font, fontSize)

    
    def setBgColor(self, color : tuple) -> None:

        self.__bgColor = color
        

    def setCommand(self, command : str) -> None:

        self.__command = command
    #get Methods


    def getTextFont(self) :

        return self.__textFont


    def getText(self) -> str:

        return self.__text
    

    def getRect(self) -> pygame.Rect:

        return self.__rect


    def getBgColor(self) -> tuple:

        return self.__bgColor

    def getCommand(self) -> str:
        
        return self.__command