from _7121_chromosomeToCycle import chromosomeToCycle

def coloredEdges(genome):
    # Input: A genome P.
    # Output: The collection of colored edges in the genome graph of P in the form (x, y).
    edges = []
    for chromosome in genome:
        cycle = chromosomeToCycle(chromosome)

        # print("genome", genome, "chromToCycles", cycle)

        for i in range(1,len(chromosome)+1):
            idx = (2*i-1) % len(cycle)
            idx2 = (2*i) % len(cycle)
            edges.append((cycle[idx], cycle[idx2]))
    return edges


def readGenome(string):
    string = string[1:-1]

    chromosomes = string.split(')(')

    chromosomes = [[int(i) for i in chromosome.split(' ')] for chromosome in chromosomes]

    return chromosomes

if __name__ == "__main__":
    
    file = open('data/coloredEdges.txt', 'r')

    chromosomes = readGenome(file.readline().rstrip('\n'))

    edges =  coloredEdges(chromosomes)
   
    print(edges)
   
