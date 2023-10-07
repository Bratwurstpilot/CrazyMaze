

class File():

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