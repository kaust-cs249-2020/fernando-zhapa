import numpy as np
from _7123_coloredEdges import coloredEdges, readGenome
from _7132_breakOnGenome import twoBreakOnGenome
from _7124_graphToGenome import graphToGenome

from math import ceil
# ShortestRearrangementScenario(P, Q)
#      output P
#      RedEdges ← ColoredEdges(P)
#      BlueEdges ← ColoredEdges(Q)
#      BreakpointGraph ← the graph formed by RedEdges and BlueEdges
#      while BreakpointGraph has a non-trivial cycle Cycle
#           (i1 , i2 , i3 , i4 ) ← path starting at arbitrary red edge in nontrivial red-blue cycle
#           RedEdges ← RedEdges with edges (i1, i2) and (i3, i4) removed
#           RedEdges ← RedEdges with edges (i1, i4) and (i2, i3) added
#           BreakpointGraph ← the graph formed by RedEdges and BlueEdges
#           P ← 2-BreakOnGenome(P, i1 , i2 , i4 , i3 )
#           output P

def shortestRearrangementScenario(genomeP, genomeQ):
    redEdges = coloredEdges(genomeP)
    blueEdges = coloredEdges(genomeQ)

    steps = [genomeP]
    trivialCycles = [i for i in genomeP if len(i) == 1]
    nonTrivialCycle = getNonTrivialCycle(redEdges, blueEdges, trivialCycles)
    # print('non trivial cycle', nonTrivialCycle)
    while nonTrivialCycle != []:
        i1, i2, i3, i4 = nonTrivialCycle

        # redEdges[redEdges==(i1,i2)] = (i1,i4)
        # redEdges[redEdges==(i3,i4)] = (i2,i3)

        # genomeP = graphToGenome(redEdges)
        genomeP = twoBreakOnGenome(genomeP,i1,i2,i4,i3)


        print("THIS IS GENOMEP", genomeP)

        trivialCycles = [i for i in genomeP if len(i) == 1]

        redEdges = coloredEdges(genomeP)
        # print("this is red edges", redEdges)
        steps.append(genomeP)
        nonTrivialCycle = getNonTrivialCycle(redEdges, blueEdges, trivialCycles)

    return steps


def getNonTrivialCycle(graph1, graph2, trivialCycles):
    cycle = []

    foundCycle = False

    i = 0
    j = 0
    last = -1
    while not foundCycle:
        x1, y1 = graph1[i]

        if not [ceil(x1/2)] in trivialCycles and not [ceil(y1/2)] in trivialCycles:

            for x2,y2 in graph2:
                if y1 == x2:
                    if x1 != y2:
                        cycle = [x1,x2,y2]
                        foundCycle =  True
                        last = y2
                        break
                elif y2 == y1:
                    if x1 != x2:
                        cycle = [x1,y2,x2]
                        foundCycle =  True
                        last = x2
                        break
        i += 1
    
    for x1, y1 in graph1:
        if x1 == last and not y1 in cycle:
            cycle.append(y1)
        elif y1 == last and not x1 in cycle:
            cycle.append(x1)

    # print("GETCYCLE:", graph1, graph2, cycle)
    return tuple(cycle) 



if __name__ == "__main__":
    
    file = open('data/2BreakSorting.txt', 'r')

    genomeA = readGenome(file.readline().rstrip('\n'))
    genomeB = readGenome(file.readline().rstrip('\n'))

    print(shortestRearrangementScenario(genomeA, genomeB))