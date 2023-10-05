import pygame


class Scene():

    def __init__(self, newScreen : pygame.display, newElements : list) -> None:

        self.screen : pygame.display = newScreen
        self.elements : list = newElements


    def renderScene(self) -> None:
        
        self.screen.fill((255, 255, 255))

        for element in self.elements:
            img : pygame.image = element.getTextureComponent().getTexture()
            if img == None :       
                pygame.draw.rect(self.screen, (0, 0, 0), (element.getPositionX(), element.getPositionY(), element.getBodyWidth(), element.getBodyHeight()))
            else : 
                self.screen.blit(img, (element.getPositionX(), element.getPositionY(), element.getBodyWidth(), element.getBodyHeight()))

        pygame.display.update()