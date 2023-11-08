import pygame


class Scene():

    def __init__(self, newScreen : pygame.display, newElements : list, newUIElements : list) -> None:

        self.screen : pygame.display = newScreen
        self.elements : list = self.depthSort(newElements)
        self.uiElements : list = newUIElements


    def render(self) -> None:
        
        self.__renderElements()
        self.__renderUI()
        pygame.display.update()


    def __renderElements(self) -> None:
        
        self.screen.fill((255, 255, 255))

        for element in self.elements:

            img : pygame.image = element.getTextureComponent().getTexture()
            if img == None :       
                pygame.draw.rect(self.screen, (0, 0, 0), (element.getPositionX(), element.getPositionY(), element.getBodyWidth(), element.getBodyHeight()))
            else : 
                self.screen.blit(img, (element.getPositionX(), element.getPositionY(), element.getBodyWidth(), element.getBodyHeight()))


    def __renderUI(self) -> None:

        for element in self.uiElements:
            pygame.draw.rect(self.screen, (0, 0, 0), (element.getPositionX(), element.getPositionY(), element.getBodyWidth(), element.getBodyHeight()))
            self.screen.blit(element.getTextFont(), element.getRect())


    def depthSort(self, elements : list) -> list :

        elements.sort(key = lambda x : x.getPositionZ())
        
        return elements 