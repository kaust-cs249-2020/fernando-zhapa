def spacedPrint(list_):
    text = ""
    for item in list_:
        text+=str(item)+" "
    print(text[:-1]) #remove last additional space

def verticalPrint(list_):
    text = ""
    for item in list_:
        text+=str(item)+"\n"
    print(text[:-1]) #remove last additional "\n"

def printDict(dict):
    for key, value in dict.items():
        print (str(key)+": "+str(value)+"\n")

def printGraphAdjList(graph):
    for key, value in graph.items():
        strValue = [str(tupl) for tupl in value]
        string = str(key) + "->" + ','.join(strValue)
        print(string)

def toStr(peptide):
    string = ""
    for item in peptide:
        string += str(item)+'-'
    return string[:-1]


def readAdjacencyList(strings):
    graph = {}
    for string in strings:
        spplit = string.split(' -> ')
        key = int(spplit[0])
        value = [int(i) for i in spplit[1].split(',')]
        graph[key] = value
    return graph


def col(matrix, j):
    return [row[j] for row in matrix]