import numpy as np
def reverse(array, idx):
    # reverses the array position indicated by idx, to the position where the value (idx+1) is.
    value = idx+1
    if value in array:
        actualIdx = array.index(value)
    elif -value in array:
        actualIdx = array.index(-value)

    reverse = [-i for i in array[idx:actualIdx+1][::-1]]
    return array[:idx] + reverse + array[actualIdx+1:]

def greedySorting(permutation):

    # Input: A permutation P.
    # Output: The sequence of permutations corresponding to applying GreedySorting to P, ending with the identity permutation.

    steps = []
    p = len(permutation)

    for i in range(p):
        if abs(permutation[i]) != i+1:
            permutation = reverse(permutation,i)
            steps.append(permutation)
        if permutation[i] == -(i+1):
            permutation = permutation[:] # deep copy of permutation array
            permutation[i] *= (-1)
            steps.append(permutation) 

    return steps

def printSteps(permutations):
    for permutation in permutations:
        toPrint = ''
        for elem in permutation:
            if elem>0:
                toPrint += '+' + str(elem)
            else:
                toPrint += str(elem)
            toPrint += ' '
        print(toPrint[:-1])

if __name__ == "__main__":
    

    file = open('data/greedySorting.txt', 'r')

    intialPermutation = [int(i) for i in file.readline().split(' ')]

    printSteps(greedySorting(intialPermutation))