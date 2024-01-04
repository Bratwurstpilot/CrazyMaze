import pygame


class Scene():

    def __init__(self, screen : pygame.display, elements : list, uiElements : list, image : pygame.image = None) -> None:

        self.screen : pygame.display = screen
        self.elements : list = self.depthSort(elements)
        self.uiElements : list = uiElements
        self.background : pygame.image = image


    def render(self) -> None:
        
        self.elements = self.depthSort(self.elements)
        self.__renderElements()
        self.__renderUI()
        pygame.display.update()


    def __renderElements(self) -> None:
        
        if self.background != None:
            self.screen.blit(self.background, (0, 0))

        for element in self.elements:

            img : pygame.image = element.getTextureComponent().getTexture()
            if img == None :       
                pygame.draw.rect(self.screen, element.getTextureComponent().color, (element.getPositionX(), element.getPositionY(), element.getBodyWidth(), element.getBodyHeight()))
            else : 
                self.screen.blit(img, (element.getPositionX(), element.getPositionY(), element.getBodyWidth(), element.getBodyHeight()))


    def __renderUI(self) -> None:

        for element in self.uiElements:
            pygame.draw.rect(self.screen, element.getBgColor(), (element.getPositionX(), element.getPositionY(), element.getBodyWidth(), element.getBodyHeight()))
            self.screen.blit(element.getTextFont(), element.getTextRect())


    def depthSort(self, elements : list) -> list :

        elements.sort(key = lambda x : x.getPositionZ())
        
        return elements 