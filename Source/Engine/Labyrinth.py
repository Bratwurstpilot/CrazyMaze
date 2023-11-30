import random

class Labyrinth:

    def __init__(self, width: int, height: int) -> None:

        self.width = width
        self.height = height
        self.grid = [[None for _ in range(width)] for _ in range(height)]


        for i in range(self.height):
            self.grid[i][0] = [False]
            self.grid[0][i] = [False]
            self.grid[self.height-1][i]=[False]
            self.grid[i][self.width-1]=[False]
        self.grid[self.height-2][self.width-1]=[True]
        self.grid[1][0]=[True]
        self.grid[1][1]=[True]

        self.setRules()


    def setRules(self) -> None:

        self.rules = [ [False,False,False,
                        True ,True ,False,
                        False,True ,False],

                       [False,False,False,
                        True ,False,False,
                        True ,False ,True],

                       [False,False,False,
                        False,True ,True ,
                        False,False,True],

                       [False,False,False,
                        False,True ,False,
                        True ,True ,False],


                       [False,True ,True,
                        False,False,False,
                        False,True ,True],

                       [True,True ,True,
                        True,False,False,
                        True,False ,True],
                        
                       [False,True,True,
                        False ,False ,True,
                        True,True ,True],
                        
                       [False,True,True,
                        False ,True ,False,
                        True,True ,False],
                        

                       [False,False,True,
                        False,True ,True,
                        False,True ,False],
                        
                       [False,True,True,
                        False,True ,False,
                        False,True ,False],
                        
                       [False,False,False,
                        True ,True ,False,
                        False,True ,False],
                        
                       [True,False,False,
                        True ,True ,False,
                        True ,False,False],
                        

                       [False,True ,True ,
                        False,False,True ,
                        False,False,False],

                       [True ,True ,True ,
                        False,False,True ,
                        False,False,False],

                       [True ,True ,True ,
                        False ,True ,False,
                        False ,False,False],
                        
                       [True ,False,False,
                        True ,True ,True ,
                        False,False,False]]


    def generateLabyrinth(self) -> list:

        self.generateOnePath()

        for i in range(self.height-1):
            for j in range(self.width-1):
                if self.grid[i][j] is None:
                    self.setStatus(i,j)

        return self.grid


    def checkMatch(self, labyrinth: list) -> list:

        match_count=[0 for _ in range(len(self.rules)-1)]
        
        for j in range(len(self.rules)-1):
            for i in range(9):
                if labyrinth[i] is not None:
                    if labyrinth[i][0] is self.rules[j][i]:
                        match_count[j] +=1

        return match_count


    def setStatus(self, x: int, y: int) -> None:

        labyrinth = self.allneighbors(x,y)
        var = self.checkMatch(labyrinth)
        pos = var.index(max(var))
        if isinstance(pos, list):
            self.grid[x][y]=[self.rules[pos[random.randint(len(pos))]][4]] 
        else:
            self.grid[x][y]=[self.rules[pos][4]]


    def generateOnePath(self) -> None:

        self.recGenerateOnePath(1,1)


    def recGenerateOnePath(self, x: int, y: int) -> None:

        if self.grid[self.height-2][self.width-2] != [True]:
            select=[[0,1],[1,0]]
            x1,y1 = x,y
            if random.randint(0,100)>51:
                x1 += select[random.randint(0,1)][0]
            else:
                y1 += select[random.randint(0,1)][1]

            if 1 <= x1 < self.height-1: 
                if 1 <= y1 < self.width-1:
                    if self.grid[x1][y1] is None:
                        self.grid[x1][y1] = [True]
                        self.rec_generate_one_path(x1,y1)
                    else:
                        self.rec_generate_one_path(x,y)
                else:
                    if y > 1:
                        self.rec_generate_one_path(x1,y1-1)
                    else:
                        self.rec_generate_one_path(x1,y1+1)
            else:
                if x > 1:
                    self.rec_generate_one_path(x1-1,y1)
                else:
                    self.rec_generate_one_path(x1+1,y1)

    
    def allneighbors(self, x: int, y: int) -> list:

        #  (x-1,y-1)(x-1,y) (x-1,y+1)
        #  (x,y-1)  (x,y)   (x,y+1)   =ret[(x-1,y-1),(x-1,y),(x-1,y+1),(x,y-1),(x,y),(x,y+1),(x+1,y-1),(x+1,y),(x+1,y+1)]
        #  (x+1,y-1)(x+1,y) (x+1,y+1)
        ret = []
        for i in range(-1,2,1):
            for j in range(-1,2,1):
                ret.append(self.grid[x+i][y+j])
        
        return ret
