from _7122_cycleToChromosome import cycleToChromosome

import ast

def graphToGenome(genomeGraph):
    # Input: The colored edges ColoredEdges of a genome graph.
    # Output: The genome P corresponding to this genome graph.
    chromosomes = []

    i = 0
    cycle = []
    while bool(genomeGraph) and i<len(genomeGraph):
        x, y = genomeGraph[i]
        if x < y:
            cycle += [x,y]
        else:
            cycle = [y] + cycle[:] + [x]
            chromosome = cycleToChromosome(cycle)
            chromosomes.append(chromosome)
            cycle = []
        i += 1
    return chromosomes

if __name__ == "__main__":
    file = open('data/graphToGenome.txt', 'r')

    graph = ast.literal_eval(file.readline())

    genome =  graphToGenome(graph)


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