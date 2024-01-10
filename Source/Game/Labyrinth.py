import random

class Labyrinth:

    def __init__(self, width : int, height : int) -> None:

        self.field : list = []
        self.create(width, height)
        

    def createRandom(self, width, height) -> None:

        self.field = [[0 for _ in range(width+2)] for __ in range(height+2)]

        self.field[1][1] = 2
        self.field[height][width] = 3

        for i in range(height+2):
            self.field[i][0] = 1
            self.field[i][-1] = 1
        for i in range(width+2):
            self.field[0][i] = 1
            self.field[-1][i] = 1

        for y in range(1,height+2):
            for x in range(1,width+2):
                choice = random.randint(0,100)
                if choice >= 80 and self.field[y][x] == 0:
                    self.field[y][x] = 1

        for row in self.field:
            print(*row)

    
    def create(self, width, height):

        def getWalls(field : list, point : list):
            pass

        self.field = [[(i%2+j%2)%2 for i in range(width+2)] for j in range(height+2)]

        randomsetX : list = []
        print("Creating...")

        count = 0
        randomCoord : list = []

        for i in range(len(self.field)):
            for j in range(len(self.field[0])):
                if self.field[i][j] == 0:
                    randomCoord.append([j,i])
                    
        #Pick a random cell
        choice : list = randomCoord[random.randint(0,len(randomCoord)-1)]

        labParts : list = []
        labParts.append(choice)



        print("Finished creating")
        
        self.field[1][1] = 2
        self.field[height][width] = 3


    def getLabyrinth(self) -> list:

        return self.field

lab = Labyrinth(10, 10)
