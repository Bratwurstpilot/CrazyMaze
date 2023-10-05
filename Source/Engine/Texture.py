import pygame


class TextureComponent:

    def __init__(self) -> None:
        
        self.__texture : pygame.image = None
        self.__color : tuple = (0,0,0)
        self.__fileConfig : None = None


    # Set Methods


    def setTexture(self, tex2D : str) -> None:

        try: 
            self.__texture = pygame.image.load(tex2D)
        except ValueError:
            print("Error while loading Texture : " + tex2D + " in component " + self)


    def setTextureSet(self, file) -> None:

        pass #TODO Parse file Content


    def getTexture(self) -> pygame.image:

        return self.__texture
