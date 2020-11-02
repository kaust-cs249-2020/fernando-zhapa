from _7123_coloredEdges import coloredEdges, readGenome
from _7131_breakOnGenomeGraph import twoBreakOnGenomeGraph
from math import floor, ceil



def cycleToChromosome(cycle):
    # Input: A sequence Nodes of integers between 1 and 2n.
    # Output: The chromosome Chromosome containing n synteny blocks resulting from applying CycleToChromosome to Nodes.
    chromosome = []
    minElement = ceil(min(cycle)/2)

    for i in range(floor(len(cycle)/2)):
        if cycle[2*i+1] > cycle[2*i]:
            chromosome.append(ceil(cycle[2*i+1]/2))
        else:
            chromosome.append(-ceil(cycle[2*i]/2))
    return chromosome

def graphToGenome(graphs):
    # Input: The colored edges ColoredEdges of a genome graph.
    # Output: The genome P corresponding to this genome graph.
    chromosomes = []

    cycle = []

    for graph in graphs:
        cycle = []
       
        for x,y in graph:
            cycle += [x,y]
        cycle = [cycle[-1]] + cycle[:-1]
        print(cycle)
        chromosome = cycleToChromosome(cycle)
        chromosomes.append(chromosome)
   
   
    return chromosomes



def twoBreakOnGenome(genome, x1, y1, x2, y2):

    genomeGraph = coloredEdges(genome)

    genomeGraph, breaks = twoBreakOnGenomeGraph(genomeGraph, x1, y1, x2, y2)

    # print("BREAKS", breaks)
   

    genomeGraph = [ genomeGraph[breaks[1]:] + genomeGraph[:breaks[0]], genomeGraph[breaks[0]:breaks[1]] ]
    # print("GRAPH",genomeGraph)
    # print("BREAKS",breaks)
    prevGenLen = len(genome)
    genome = graphToGenome(genomeGraph)

    if len(genome)>prevGenLen:
        genome[-1][0] *= -1
    # print("GENOME", genome)
    return genome

if __name__ == "__main__":
    
    file = open('data/2BreakOnGenome.txt', 'r')

    genome = readGenome(file.readline().rstrip('\n'))
    
    indices = [int(i) for i in file.readline().split(', ')]


    genome = twoBreakOnGenome(genome,*indices)


    toPrint = ''
    for chromosome in genome:
        toPrint += '('
        for elem in chromosome:
            if elem>0:
                toPrint += '+' + str(elem)
            else:
                toPrint += str(elem)
            toPrint += ' '
        toPrint = toPrint[:-1]
        toPrint += ')'

    print(toPrint)