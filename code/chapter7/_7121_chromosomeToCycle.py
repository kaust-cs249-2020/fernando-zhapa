def chromosomeToCycle(chromosome):
    # Input: A chromosome Chromosome containing n synteny blocks.
    # Output: The sequence Nodes of integers between 1 and 2n resulting from applying ChromosomeToCycle to Chromosome.

    cycle = []
    for block in chromosome:
        if block < 0:
            block *= -1
            cycle += [2*block, 2*block-1]
        elif block > 0:
            cycle += [2*block-1, 2*block]
        else:
            print("error in chromosomeCycle")
            return -1 
    return cycle

if __name__ == "__main__":
    
    file = open('data/chromosomeToCycle.txt', 'r')

    line = file.readline()[1:-1].split(' ')

    # chromosome = []
    # for item in line:
    #     if item[0] == '+':
    #         chromosome.append(int(item[1:]))
    #     else:
    #          chromosome.append(int(item))


    chromosome = [int(i) for i in line]

    print(chromosomeToCycle(chromosome))