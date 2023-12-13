

class Instance:

    def __init__(self):
        self.playerAlgorithm : list = ["Manuell", "Manuell"]
        self.algorithms : list = ["Manuell" ,"A Star" ,"Dijkstra"]
        self.playerOne : int = 0
        self.playerTwo : int = 0

        self.difficulty : int= 0

        self.maze : list = []


    def setPlayerOne(self, state : int) -> None:
        self.playerOne += state

        if self.playerOne < 0:
            self.playerOne = 0
        elif self.playerOne > len(self.algorithms):
            self.playerOne = len(self.algorithms)
        print(self.playerOne)
        self.playerAlgorithm[0] = self.algorithms[self.playerOne]
        self.playerAlgorithm[0]
        return self.playerAlgorithm[0]
        

    def setPlayerTwo(self, player : int, state : int):
        
        self.playerTwo += state
        self.playerAlgorithm[1] = self.algorithms[self.playerOne]

