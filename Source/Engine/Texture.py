import pygame


class TextureComponent:

    def __init__(self) -> None:
        
        self.__textures : list = []
        self.__textureCurrent : int = 0

        self.color : tuple = (0,0,0)
        self.__fileConfig : None = None

        self.__frameInterval : list = [1 * 144]
        self.__frameIntervalCurrent : int = 0
        self.__frameCurrent : int = 0


    # Compute Methods


    def update(self):
            
        self.__frameCurrent += 1.0

        if self.__frameCurrent >= self.__frameInterval[self.__frameIntervalCurrent] and len(self.__textures) > 0:
            self.__frameCurrent = 0
            self.__textureCurrent = (self.__textureCurrent + 1) % len(self.__textures)
            self.__frameIntervalCurrent = (self.__frameIntervalCurrent + 1) % len(self.__frameInterval)


    # Set Methods


    def setTexture(self, tex2D : str, size : tuple = None, rotate : float = 0) -> None:

        try: 
            if size != None:
                self.__textures = [ (pygame.transform.scale(pygame.image.load(tex2D), size)) ]
        
            else:
                self.__textures = [ (pygame.image.load(tex2D)) ]

            self.__textures = [pygame.transform.rotate(self.__textures[0], rotate)]

        except ValueError:
            print("Error while loading Texture " + tex2D + " in component " + self)


    def setTextureSet(self, textureSet : list, size : tuple = None, reflectX : bool = False) -> None:

        try: 
            self.__textures.clear()
            for tex in textureSet:
                if size != None:
                    self.__textures.append(pygame.transform.flip(pygame.transform.scale(pygame.image.load(tex), size), reflectX, False))
                else:
                    self.__textures.append(pygame.transform.flip(pygame.image.load(tex), reflectX, False))
        except ValueError:
            ("Error while loading Texture " + textureSet + " in component " + self)


    def setFrameInterval(self, interval : float) -> None:
        
        self.__frameInterval = [interval * 144]


    def setFrameIntervalCustom(self, interval : list[int]) -> None:

        self.__frameInterval = list(map(lambda x : x * 144, interval))


    # Get Methods


    def getTexture(self) -> pygame.image:

        if len(self.__textures) > 0:
            return self.__textures[self.__textureCurrent]
        return None