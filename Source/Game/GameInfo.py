

class GameInfo:

    def __init__(self):

        self.playerAlgorithm : list = ["A Star", "A Star"]
        self.algorithms : list = ["A Star", "TSP Solver"]
        self.player : list = [0, 0]
        
        self.difficulty : list = ["Einfach", "Einfach"]
        self.difficulties : list = ["Einfach", "Mittel", "Schwer"]
        self.botDifficulty : list = [0, 0]

        self.winCount : list = [0, 0, 0]
        
        self.coins : list = [0, 0]
        self.points : list = [0, 0]
        self.gameCoins : list = []
        
        
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

        if instance.bot[0].getPosition() == instance.end[1] and instance.bot[1].getPosition() == instance.end[0]:
            self.winCount[2] += 1

        elif instance.bot[0].getPosition() == instance.end[1] and not instance.bot[1].getPosition() == instance.end[0]:
            self.winCount[0] += 1

        elif instance.bot[1].getPosition() == instance.end[0] and not instance.bot[0].getPosition() == instance.end[1]:
            self.winCount[1] += 1

        self.gameCoins.append(self.coins)
        self.coins = [0, 0]
        self.points = [0, 0]