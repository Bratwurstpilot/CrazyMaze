import pygame

from Source.Engine.Texture import TextureComponent

class UIElement:

    def __init__(self):

        self.__textureComp = TextureComponent()

        self.__useable : bool = False
        self.__onePress : bool = True
        self.__command : str = ""
        self.__alreadyPressed : bool = False
        self.__text : str = ""
        self.__textSize : int = 20
        self.__textColor : tuple = (255, 255, 255)
        self.__bgColor : tuple = (0, 0, 0)
    
        self.__PositionX : int = 100
        self.__PositionY : int = 100
        self.__PositionZ : int = 1
        self.__width : int = 100
        self.__height : int = 100

        self.__font : pygame.font = pygame.font.SysFont('Arial', 40)
        self.__rect : pygame.Rect = pygame.Rect(100, 100, 100, 100)
        self.__textFont = self.__font.render(self.__text, True, self.__textColor)


    def __execCommand(self) -> None:

        exec(self.__command)


    def onClick(self, mousePos : tuple) -> None:
        
        if self.__rect.collidepoint(mousePos):
            if pygame.mouse.get_pressed(num_buttons = 3)[0]:
                if self.__useable and self.__onePress:
                    self.__execCommand()
                
                elif not self.__alreadyPressed:
                    self.__execCommand()
                    self.__alreadyPressed = True
            
            else:
                self.__alreadyPressed = False


    #set Methods
    
    
    def setTextSize(self, size : int) -> None:

        self.__textsize = size


    def setTextFont(self) -> None:

        self.__textFont = self.__font.render(self.__text, True, (255,255,255))


    def setRect(self) -> None:

        self.__rect = self.__textFont.get_rect(center = (self.__PositionX + self.__width / 2, self.__PositionY + self.__height / 2))


    def setText(self, text : str) -> None:

        self.__text = text


    def setFont(self, font : pygame.font, fontSize : int) -> None:

        self.__font = pygame.font.SysFont(font, fontSize)


    def shitPositionX(self, shift : int) -> None:

        self.__PositionX += shift
        

    def shitPositionY(self, shift : int) -> None:

        self.__PositionY += shift
        

    def shitPositionZ(self, shift : int) -> None:

        self.__PositionZ += shift


    def setPositionX(self, newPos : int) -> None:

        self.__PositionX = newPos
        

    def setPositionY(self, newPos : int) -> None:

        self.__PositionY = newPos
        

    def setPositionZ(self, newPos : int) -> None:

        self.__PositionY = newPos
        

    def setWidth(self, newWidth : int) -> None:

        self.__width = newWidth
        

    def setHeight(self, newHeight : int) -> None:

        self.__height = newHeight
    

    def setCommand(self, newCommand : str) -> None:

        self.__command = newCommand


    def setUsable(self) -> None:

        self.__useable = True

    #get Methods
    

    def getTextFont(self) :

        return self.__textFont


    def getText(self) -> str:

        return self.__text
    

    def getRect(self) -> pygame.Rect:

        return self.__rect


    def getTextureComponent(self) -> TextureComponent:

        return self.__textureComp


    def getPositionX(self) -> int:
        
        return self.__PositionX
    

    def getPositionY(self) -> int:
        
        return self.__PositionY
    

    def getPositionZ(self) -> int:
        
        return self.__PositionZ
    

    def getBodyWidth(self) -> int:

        return self.__width
    

    def getBodyHeight(self) -> int:

        return self.__height
    
