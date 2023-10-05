import pygame

class Scene():

    def __init__(self, newScreen : pygame.display, newElements : list) -> None :

        self.screen : pygame.display = newScreen
        self.elements : list = newElements


    def renderScene(self) -> None :
        #print("test")
        #map(self.__draw, self.elements)
        #pygame.display.update()
        for element in self.elements :
            img : pygame.image = element.getTextureComponent().getTexture()
            if img == None :       
                pygame.draw.rect(self.screen, (0, 0, 0), (element.getPositionX(), element.getPositionY(), element.getBodyWidth(), element.getBodyHeight()))


    def __draw(self, element):
        pass
        #img : pygame.image = element.getTextureComponent.getTexture()
        #if img == None :       
         #   pygame.draw.rect(self.screen, (0, 0, 0), (element.getPositionX(), element.getPositionY(), element.getBodyWidth(), element.getBodyHeight()))
    
    
class Renderer():

    def __init__(self, newScreen : pygame.display, newElements : list) -> None :

        self.__screen : pygame.display = newScreen
        self.__elements : list = newElements

    def renderScene(self) -> None :
        
        pass
