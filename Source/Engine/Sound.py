import pygame


class SoundComponent:
    
    def __init__(self) -> None:
        
        self.__sounds : list = None
        self.__soundState : int = -1 # -1 = inactive
        self.__currentSound : str = ""
        self.__mixer : pygame.mixer = pygame.mixer


    # Sound Playing Functions


    def play(self, sound) -> None: 

        self.__mixer.Sound.play(sound)


    # Get Methods
    
    
    def setConfig(self, file : None) -> None:

        pass

    
    def setSounds(self, sounds : list) -> None:

        self.__sounds = sounds

    
    def addSound(self, sound) -> None:

        self.__sounds.append(sound)