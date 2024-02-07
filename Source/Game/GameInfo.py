

class GameInfo:

    def __init__(self):

        self.playerAlgorithm : list = ["Manuell", "Manuell"]
        self.algorithms : list = ["Manuell", "A Star"]
        self.player : list = [0, 0]
        
        self.difficulty : list = ["Einfach", "Einfach"]
        self.difficulties : list = ["Einfach", "Mittel", "Schwer"]
        self.botDifficulty : list = [0, 0]

        self.winCount : list = [0, 0, 0]
        
        
    def setPlayerAlgorithm(self, state : int, player : int) -> None:

        self.player[player] += state
        if self.player[player] < 0:
            self.player[player] = 0
        elif self.player[player] == len(self.algorithms):
            self.player[player] = len(self.algorithms) - 1
        self.playerAlgorithm[player] = self.algorithms[self.player[player]]


    def setBotDifficulty(self, state : int, player : int) -> None:
        
        self.botDifficulty[player] += state
        if self.botDifficulty[player] < 0:
            self.botDifficulty[player] = 0
        elif self.botDifficulty[player] == len(self.difficulties):
            self.botDifficulty[player] = len(self.difficulties) - 1
        self.difficulty[player] = self.difficulties[self.botDifficulty[player]]

    
    def addWin(self, instance):

        if instance.bot[0].getPosition() == instance.end[1] and instance.bot[0].getPosition() == instance.end[1]:
            self.winCount[2] += 1

    

