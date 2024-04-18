

class File():

    
    def writeContent(filePath : str, gameInfo):
        
        file = open(filePath, "a")

        file.write(str(gameInfo.playerAlgorithm[0]) + ", " + str(gameInfo.playerAlgorithm[1]) + ", " + str(gameInfo.coins[0]) + ", " + str(gameInfo.coins[1]) + "\n")
        #file.write(str(gameInfo.coins[0]) + ", " + str(gameInfo.coins[1]) + "\n")
        #file.write("\n")

        file.close()

    def getContentSplit(filePath : str, split : str = ";") -> list: # Gets content from file, need of putting the split on EVERY endline

        file = open(filePath, "r")

        content = []
        for row in file:
            substring = ""
            for i in range(len(row)):
                if row[i] == split:
                    content.append(substring)
                    substring = ""
                substring += row[i]

        return content


    def getContentRaw(filePath : str) -> list:
    
        return list(map(lambda x : x.replace("\n", ""), [row for row in open(filePath)]))