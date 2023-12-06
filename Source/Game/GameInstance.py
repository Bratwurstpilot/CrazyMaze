

class Instance:

    def __init__(self):
        self.playerOneAlgorithm : str = "Player1"
        self.playerTwoAlgorithm : str = "Player2"

        self.difficulty : int= 0

        self.maze : list = []

    def setPlayerOne(self, newAlgorithm : str):
        
        self.playerOneAlgorithm = newAlgorithm
        print(self.playerOneAlgorithm)
