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
                

        #for row in self.field:
            #print(*row)

    
    def create(self, width, height):

        def getItem(field : list, point : list, mode : int = 1):
            
            #mode := 0 for cells, 1 for walls
            walls : list = []

            #Upper
            try:
                if field[point[1]-1][point[0]] == mode:
                    walls.append([point[0], point[1]-1])
            except IndexError:
                pass

            #Lower
            try:
                if field[point[1]+1][point[0]] == mode:
                    walls.append([point[0],point[1]+1])
            except IndexError:
                pass

            #Right
            try:
                if field[point[1]][point[0]+1] == mode:
                    walls.append([point[0]+1,point[1]])
            except IndexError:
                pass

            #Left
            try:
                if field[point[1]][point[0]-1] == mode:
                    walls.append([point[0]-1,point[1]])
            except IndexError:
                pass
            
            return walls
        

        self.field = [[1 for _ in range(width+2)] for __ in range(height+2)]

        randomCoord : list = []

        for y in range(1,height+1,2):
            for x in range(1,width+1,2):
                self.field[y][x] = 0
                randomCoord.append([x,y])
                    
        #Pick a random cell
        choice : list = randomCoord[random.randint(0,len(randomCoord)-1)]

        labParts : list = []
        passage : list = []

        labParts.append(choice)

        walls = getItem(self.field, choice, 1)

        while len(walls) > 0:

            #Get a random Wall
            choice = walls[random.randint(0,len(walls)-1)]
            walls.remove(choice)

            #Get the devided cells
            devide = getItem(self.field, choice, 0)

            #Check number of visited Cells
            devideCount = 0
            unVisited = None
            for elem in devide:
                if elem in labParts:
                    devideCount += 1
                else:
                    unVisited = elem
            
            #If only one of the cells devided is visited, make the wall a passage
            if devideCount <= 1 and unVisited != None:
                passage.append(choice)
                labParts.append(unVisited)
            
                #Append the neighbouring walls
                neighbourWalls = getItem(self.field, unVisited, 1)
                for wall in neighbourWalls:
                    if wall not in passage and wall not in labParts:
                        walls.append(wall)

        for cell in labParts + passage:
            self.field[cell[1]][cell[0]] = 0

        self.field[1][1] = 2
        self.field[height][width] = 3


    def getLabyrinth(self) -> list:

        return self.field