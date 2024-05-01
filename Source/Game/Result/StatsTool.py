

def procFile(file : str) -> None:
    
    file = open(file, "r")
    content : list = []
    for line in file:
        temp = line.split(",")
        for i in range(len(temp)):
            element = temp[i].replace(" ", "")
            temp[i] = element.replace("\n", "")
            temp[i] = temp[i].replace("Solver", "")
            try:
                temp[i] = int(temp[i])
            except ValueError:
                pass
        content.append(temp)

    return content


def getResult(file : str, keys : dict) -> None:

    fileContent = procFile(file)
    for line in fileContent:
        dictString : str = str(line[0]) + "-" + str(line[1])
        res1 = line[2]
        res2 = line[3]
        if res1 > res2:
            keys[dictString][0] += 1
        elif res1 < res2:
            keys[dictString][1] += 1
        else:
            keys[dictString][2] += 1
    print(keys)

    return keys


def writeResult(targetFile : str, stemp : str, data : dict) -> None:

    file = open(targetFile, "a")

    dashLength = 60 - len(stemp)
    string = "-" * (dashLength//2)
    string += stemp
    string += "-" * (60 - len(stemp) - dashLength//2)
    file.write(string + "\n")
    
    for key, value in data.items():
        file.write(str(key) + " "*(11-len(str(key))) + " : " + str(value) + "\n")
    file.write("-" * 60 + "\n" + "\n")
    file.close()

keys : dict = {
    "AStar-AStar" : [0,0,0],
    "TSP-AStar" : [0,0,0],
    "AStar-TSP" : [0,0,0],
    "TSP-TSP" : [0,0,0]
}

result = getResult("F:\Studium\Semester 5\SoftwareProjekt\CrazyMaze\Source\Game\Result\games.txt", keys)
writeResult("F:\Studium\Semester 5\SoftwareProjekt\CrazyMaze\Source\Game\Result\Statistics.txt", "Spieldoku Merge Final | [win1, win2, draw]", result)




import numpy as np
import matplotlib.pyplot as plt 
 

tspWins : int = result["AStar-TSP"][1] + result["TSP-AStar"][0]
aStarWins : int = result["AStar-TSP"][0] + result["TSP-AStar"][1]
draws : int = result["AStar-TSP"][2] + result["TSP-AStar"][2]
  
# creating the dataset
data = {'TSP':tspWins, 'AStar':aStarWins, 'Draw':draws}
courses = list(data.keys())
values = list(data.values())
  
fig = plt.figure(figsize = (10, 5))
 
# creating the bar plot
plt.bar(courses, values, color ='steelblue', 
        width = 0.4)
 
plt.xlabel("Algorithms")
plt.ylabel("Wins in game")
plt.title("Algorithm comparison")
plt.show()