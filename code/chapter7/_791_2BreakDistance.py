import sys
sys.setrecursionlimit(3000)

from _7123_coloredEdges import coloredEdges, readGenome


def _2breakDistance(genomeA, genomeB):

    graphA = coloredEdges(genomeA)
    graphB = coloredEdges(genomeB)
                 
    blocks = len(graphA)
    cycles = 0

    start, value = graphA[0]
    graphA = graphA[1:]

    cycle = False
    checkGraphA = False
    while bool(graphB) or bool(graphA):
   
        # print(graphA, graphB)
        if checkGraphA:
 
            for v1, v2 in graphA:
                if v1 == value:
        
                    value = v2
                    checkGraphA = False
                    graphA.remove((v1,v2))
                    break

                if v2 == value:
         
                    value = v1
                    checkGraphA = False
                    graphA.remove((v1,v2))
                    break

        else:
            
            for v1, v2 in graphB:
                if v1 == value:
                    if v2 == start:
                        cycles += 1
                        cycle = True
                        graphB.remove((v1,v2))
                        break
                    else:
                        value = v2
                        checkGraphA = True
                        graphB.remove((v1,v2))
                        break

                if v2 == value:
                    if v1 == start:
                        cycles += 1
                        cycle = True
                        graphB.remove((v1,v2))
                        break
                    else:
                        value = v1
                        checkGraphA = True
                        graphB.remove((v1,v2))
                        break

    
        if cycle and bool(graphA):
            start, value = graphA[0]
            graphA = graphA[1:]
            checkGraphA = False
            cycle = False

    return blocks -cycles


def checkGraphs(graphA, graphB, start, value, cycles):


    for (x, y) in graphB:
        if x == value:
            if y == start:
                newGraphB = graphB[:]
                newGraphB.remove((x,y))
                return graphA, newGraphB, cycles+1
            else:
                newvalue = y
                newGraphB = graphB[:]
                newGraphB.remove((x,y))
                return checkGraphs(newGraphB, graphA, start, newvalue, cycles)
        elif y == value:
            if x == start:
                newGraphB = graphB[:]
                newGraphB.remove((x,y))
                return graphA, newGraphB, cycles+1
            else:
                newvalue = x
                newGraphB = graphB[:]
                newGraphB.remove((x,y))
                return checkGraphs(newGraphB, graphA, start, newvalue, cycles)
        else:
            continue



if __name__ == "__main__":
    
    file = open('data/2BreakDistance.txt', 'r')
    
    genomeA = readGenome(file.readline().rstrip('\n'))
    genomeB = readGenome(file.readline())


    print(_2breakDistance(genomeA, genomeB))