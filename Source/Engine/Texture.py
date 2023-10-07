import pygame


class TextureComponent:

    def __init__(self) -> None:
        
        self.__textures : list = []
        self.__textureCurrent : int = 0

        self.__color : tuple = (0,0,0)
        self.__fileConfig : None = None

        self.__frameInterval : list = [0]
        self.__frameIntervalCurrent : int = 0
        self.__frameCurrent : int = 0

    # Compute Methods


    def update(self):
            
        self.__frameCurrent += 1.0

        if self.__frameCurrent >= self.__frameInterval[self.__frameIntervalCurrent]:
            self.__frameCurrent = 0
            self.__textureCurrent = (self.__textureCurrent + 1) % len(self.__textures)
            self.__frameIntervalCurrent = int((self.__frameIntervalCurrent + 1) % len(self.__frameInterval))


    # Set Methods


    def setTexture(self, tex2D : str) -> None:

        try: 
            self.__textures = [pygame.image.load(tex2D)]
        except ValueError:
            print("Error while loading Texture " + tex2D + " in component " + self)


    def setTextureSet(self, textureSet : list) -> None:

        try: 
            self.__textures.clear()
            for tex in textureSet:
                self.__textures.append(pygame.image.load(tex))
        except ValueError:
            print("Error while loading Texture " + textureSet + " in component " + self)


    def setFrameInterval(self, interval : float) -> None:
        
        self.__frameInterval = [interval * 144]


    def setFrameIntervalCustom(self, interval : list[int]) -> None:

        self.__frameInterval = list(map(lambda x : x * 144, interval))


    # Get Methods


    def getTexture(self) -> pygame.image:

        return self.__textures[self.__textureCurrent]
