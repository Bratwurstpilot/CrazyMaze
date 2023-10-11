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


class Music(): # .queue bedenken

    def __init__(self, musicTrack : str = "", volume : float = 0.1) -> None:
        
        self.__sound : str =  musicTrack
        self.__volume : float = volume

        self.__loop : int = -1 
        self.__playing : bool = False

    
    def play(self, music : str) -> None:

        if not self.__playing:
            pygame.mixer.music.load(music)
            pygame.mixer.music.set_volume(self.__volume)
            pygame.mixer.music.play(self.__loop,0.0)

            self.__playing = True


    def play(self) -> None:

        if not self.__playing:
            try:
                pygame.mixer.music.load(self.__sound)
                pygame.mixer.music.set_volume(self.__volume)
                pygame.mixer.music.play(self.__loop,0.0)

                self.__playing = True
            except ValueError:
                print("Error while trying to play Music with Object " + self)


    def stop(self) -> None:

        self.__playing = False
        pygame.mixer.music.stop() 

    
    # Set Methods


    def setMusic(self, music : str) -> None:

        self.__sound = music


    def setLoop(self, loop : int) -> None:

        self.__loop = loop


    def setVolume(self, volume : float) -> None:

        self.__volume = volume