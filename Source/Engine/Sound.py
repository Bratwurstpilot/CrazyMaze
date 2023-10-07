from typing import Any
import pygame


class SoundComponent:
    
    def __init__(self) -> None:
        
        self.__sound : str = ""
        self.__mixer : pygame.mixer = pygame.mixer


    # Sound Playing Functions


    def play(self, sound) -> None: 

        self.__mixer.Sound.play(sound)

    
    def play(self) -> None:

        pass #TODO add functionality


    # Set Methods
    
    
    def setConfig(self, file : None) -> None:

        pass

    
    def setSounds(self, sounds : list) -> None:

        self.__sounds = sounds

    
    def addSound(self, sound) -> None:

        self.__sounds.append(sound)


class Music():

    def __init__(self) -> None:
        
        self.__loop : int = -1 
        self.__volume : float = 0.5

    
    def play(self, music : str) -> None:

        pygame.mixer.music.load(music)
        pygame.mixer.music.set_volume(self.__volume)
        pygame.mixer.music.play(self.__loop,0.0)


    def play(self) -> None:

        try:
            pygame.mixer.music.load(self.__sound)
            pygame.mixer.music.set_volume(self.__volume)
            pygame.mixer.music.play(self.__loop,0.0)
        except ValueError:
            print("Error while trying to play Music with Object " + self)

    
    # Set Methods


    def setMusic(self, music : str) -> None:

        self.__sound = music


    def setLoop(self, loop : int) -> None:

        self.__loop = loop


    def setVolume(self, volume : float) -> None:

        self.__volume = volume