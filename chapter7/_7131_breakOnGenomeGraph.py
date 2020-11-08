import ast

def twoBreakOnGenomeGraph(genomeGraph, x1, y1, x2, y2):

    print(x1, y1, x2, y2, genomeGraph)
    
    foundFirst = False
    foundSecond = False

    breaks = []

    i = 0
    while not foundFirst:
        edge = genomeGraph[i]

        if (x1,y1) == edge:
            genomeGraph[i] = (x1,x2)
            print("FOUND1", i, x1,x2)
            foundFirst = True
        elif (y1,x1) == edge:
            genomeGraph[i] = (x2,x1)
            foundFirst = True
            print("FOUND2", i)
        i += 1

    i = 0
    while not foundSecond:
        edge = genomeGraph[i]

        if (x2,y2) == edge:
            genomeGraph[i] = (y1,y2)
            foundSecond = True
            print("FOUND3", i)
    
        elif (y2,x2) == edge:
            genomeGraph[i]=(y2,y1)
            foundSecond = True
            print("FOUND4", i, y2,y1)
        i += 1




    for i in range(len(genomeGraph)):
        idx = i % len(genomeGraph)
        idxPrev = (i-1) % len(genomeGraph)
        x,_ = genomeGraph[idx]
        _,y = genomeGraph[idxPrev]
        if abs(x-y) != 1:
            breaks.append(i)

    breaks.sort()
    # print('geeeeenn')
    # print(genomeGraph)
    # print('geeeeenn')
    return genomeGraph, breaks

if __name__ == "__main__":
    
    file = open('data/2BreakOnGenomeGraph.txt', 'r')

    genomeGraph = list(ast.literal_eval(file.readline()))
    
    indices = [int(i) for i in file.readline().split(', ')]

    broken, breaks= twoBreakOnGenomeGraph(genomeGraph,*indices)
    print(breaks)
    print(broken)

