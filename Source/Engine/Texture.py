import pygame



class TextureComponent:

    def __init__(self) -> None:
        
        self.__texture = None


    def setTexture(self, tex2D) -> None:

        try: 
            self.__texture = pygame.image.load(tex2D)
        except ValueError:
            pass


    def getTexture(self) -> pygame.image:

        return self.__texture
