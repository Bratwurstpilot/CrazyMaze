import pygame


class Animation:

    def __init__(self, components : list = [], targetPositions : list[list[int, int]] = [[0,0]], time : float = 1.0) -> None:
        
        self.__components : list = components
        self.__componentsActive : list = [True for _ in range(len(self.__components))]

        self.__targetPositions : list[list[int, int]] = targetPositions 

        self.__active : bool = False
        self.__time : float = time * 144

        self.__stepValues : list = []
        self.__initialized : bool = False

        self.__queue : list = []
        self.__queueActive : list = []
        self.__timer : float = 0.0
        self.__delay : list = []

        self.__onExitArgs : list = [None, None]


    def __del__(self) : 

        pass


    def update(self) -> None:
        
        if not self.__active:
            return 
        
        if not self.__initialized:
            self.__computeStartInstance()
            self.__initialized = True
        
        self.__timer += 1
        for num, timeLimit in enumerate(self.__delay):
            if self.__timer >= timeLimit and self.__queueActive[num]:
                # Is a currently animated component in a queued Animation? If so, block the queued animation until the object animation finished
                block : bool = False
                for i in range(len(self.__components)):
                    if self.__componentsActive[i] and self.__components[i] in self.__queue[num].getComponents():
                        block = True
 
                if not block:
                    self.__queue[num].setActive()
                    self.__queueActive[num] = False

        x = True
        if x not in self.__queueActive and x not in self.__componentsActive:
            self.__onExit()
            self.reset()

            if self in self.__queue:
                self.__active = True

            return

        for num, element in enumerate(self.__components):
            if not self.__componentsActive[num]:
                break
            element.shiftPositionX(self.__stepValues[num][0])
            element.shiftPositionY(self.__stepValues[num][1])

            if element.getPositionX() >= self.__targetPositions[num][0] and self.__stepValues[num][0] > 0:
                self.__stepValues[num][0] = 0
            elif element.getPositionX() <= self.__targetPositions[num][0] and self.__stepValues[num][0] < 0:
                self.__stepValues[num][0] = 0

            if element.getPositionY() >= self.__targetPositions[num][1] and self.__stepValues[num][1] > 0:
                self.__stepValues[num][1] = 0
            elif element.getPositionY() <= self.__targetPositions[num][1] and self.__stepValues[num][1] < 0:
                self.__stepValues[num][1] = 0

            if self.__stepValues[num][0] == self.__stepValues[num][1] == 0:
                self.__componentsActive[num] = False
            continue

    
    def queue(self, animation):

        self.__queue.append(animation)
        self.__delay.append(self.__time)
        self.__queueActive.append(True)


    def queueAsDelay(self, animation, delay : float):

        self.__queue.append(animation)
        self.__delay.append(delay * 144)
        self.__queueActive.append(True)


    # Set Methods


    def setComponents(self, components : list = []) -> None:

        self.__components = components
        self.__componentsActive = [True for _ in range(len(components))]

    
    def setScript(self, file : str, index : int) -> None:
        
        pass


    def setTargetPositions(self, targetPositions : list[list]) -> None:

        self.__targetPositions = targetPositions


    def setActive(self) -> None:

        self.__active = True


    def setTime(self, time : int) -> None:

        self.__time = time * 144


    def reset(self) -> None:

        self.__active = False
        self.__initialized = False
        self.__componentsActive = [True for _ in range(len(self.__components))]
        self.__queueActive = [True for _ in range(len(self.__queue))]
        self.__timer = 0.0


    def setExitAction(self, func : str, actors : dict) -> None:

        self.__onExitArgs[0] = func
        self.__onExitArgs[1] = actors


    # Get Methods

    def getComponents(self) -> list:

        return self.__components

    
    # Private Methods


    def __computeStartInstance(self) -> None:

        self.__stepValues = [[0,0] for _ in range(len(self.__targetPositions))]
        for i in range(len(self.__targetPositions)):
            self.__stepValues[i][0] = (self.__targetPositions[i][0] - self.__components[i].getPositionX()) / self.__time
            self.__stepValues[i][1] = (self.__targetPositions[i][1] - self.__components[i].getPositionY()) / self.__time



    def __onExit(self) -> None:

        try:
            exec(self.__onExitArgs[0], self.__onExitArgs[1])
        except TypeError:
            pass