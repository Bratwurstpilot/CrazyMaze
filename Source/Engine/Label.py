import pygame

from Source.Engine.Entity import Entity

pygame.font.init()

class Label(Entity):

    def __init__(self, positionX : int = 0, positionY : int = 0, positionZ : int = 0, bodyWidth : int = 100, bodyHeight : int = 100, text : str = "Crazy Maze", textColor : tuple = (255, 255, 255), size : int = 20):

        super().__init__(positionX, positionY, positionZ, bodyWidth, bodyHeight)

        self.__text : str = text
        self.__textSize : int = size
        self.__textColor : tuple = textColor
        self.__bgColor : tuple = (0, 0, 0)
        self.__font : pygame.font = pygame.font.SysFont('Arial', self.__textSize, True)
        self.__rect : pygame.Rect = pygame.Rect(positionX, positionY, bodyWidth, bodyHeight)
        self.__textRect : pygame.Rect = pygame.Rect(100, 100, 100, 100)
        self.__textFont = self.__font.render(self.__text, True, self.__textColor)


    def update(self):
        pass


    #set Methods
    
    
    def setTextSize(self, size : int) -> None:

        self.__textsize = size


    def setTextFont(self) -> None:

        self.__textFont = self.__font.render(self.__text, True, self.__textColor)


    def setRect(self) -> None:

        self.__rect = pygame.Rect(self.positionX, self.positionY, self.bodyWidth, self.bodyHeight)
    
    
    def setTextRect(self) -> None:

        self.__textRect = self.__textFont.get_rect(center = (self.positionX + (self.bodyWidth / 2), self.positionY + self.bodyHeight / 2))


    def setText(self, text : str) -> None:

        self.__text = text


    def setFont(self, font : pygame.font, fontSize : int) -> None:

        self.__font = pygame.font.SysFont(font, fontSize)

    
    def setBgColor(self, color : tuple) -> None:

        self.__bgColor = color
        

    #get Methods


    def getTextFont(self) :

        return self.__textFont


    def getText(self) -> str:

        return self.__text
    

    def getRect(self) -> pygame.Rect:

        return self.__rect
    

    def getTextRect(self) -> pygame.Rect:

        return self.__textRect


    def getBgColor(self) -> tuple:

        return self.__bgColor