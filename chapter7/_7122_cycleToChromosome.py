from math import floor, ceil

def cycleToChromosome(cycle):
    # Input: A sequence Nodes of integers between 1 and 2n.
    # Output: The chromosome Chromosome containing n synteny blocks resulting from applying CycleToChromosome to Nodes.
    chromosome = []
    minElement = ceil(min(cycle)/2)

    for i in range(floor(len(cycle)/2)):
        if cycle[2*i+1] > cycle[2*i]:
            chromosome.append(i+minElement)
        else:
            chromosome.append(-(i+minElement))
    return chromosome

if __name__ == "__main__":
    
    file = open('data/cycleToChromosome.txt', 'r')

    line = file.readline()[1:-1].split(' ')


    cycle = [int(i) for i in line]

    chromosome = cycleToChromosome(cycle)

    toPrint = ''
    for elem in chromosome:
            if elem>0:
                toPrint += '+' + str(elem)
            else:
                toPrint += str(elem)
            toPrint += ' '
    print(toPrint[:-1])