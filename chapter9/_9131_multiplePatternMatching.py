from _971_BWT import BWT
from _9101_BWMatching import k_occurrences
from _9111_betterBWMatching import firstOcurrences
from _9171_partialSuffixArray import partialSuffixArray
from math import floor
from copy import deepcopy
import itertools
import numpy as np
def counts(array, k):

    dict = {'$': 0, 'A': 1, 'C': 2, 'G': 3, 'T': 4}

    arrays = []

    currArray = [0,0,0,0,0]

    for i in range(len(array)):

        if i%k == 0:
            arrays.append(deepcopy(currArray))

        position = dict[array[i]]
        currArray[position] += 1

  
    return arrays


def getCount(countMat, k, symbol, bound, array):

    dict = {'$': 0, 'A': 1, 'C': 2, 'G': 3, 'T': 4}

    idx = floor(bound/k)

    position = idx*k

    occurs = 0 
    while position < bound:
        if array[position] == symbol:
            occurs += 1
        position += 1
 
    return countMat[idx][dict[symbol]] + occurs



def patternMatching(lastCol, pattern, lengthText, firstOcurrence, countMat, k, partialSuffixArr):

    top = 0
    bottom = len(lastCol) - 1


    while top <= bottom:
        if bool(pattern):
            symbol = pattern[-1]
            pattern = pattern[:-1]

            try:
                top = lastCol.index(symbol, top, bottom+1)
            except:
                return []
            
            top = firstOcurrence[symbol] + getCount(countMat, k, symbol, top, lastCol) 
            bottom = firstOcurrence[symbol] + getCount(countMat, k, symbol, bottom+1, lastCol) -1 
        else:

            firstCol = k_occurrences(sorted(lastCol))
            lastCol = k_occurrences(lastCol)

            startPoss = []
            for i in range(top, bottom+1):

                found = False
                backSteps = 0
                aux = i
                while not found:
                    lastCol_elem = lastCol[aux]
                    aux = firstCol.index(lastCol_elem)
                    backSteps += 1

                    for idx, suffixPos in partialSuffixArr:
                        if aux == idx:
                            startPoss.append((suffixPos + backSteps)%lengthText)
                            found = True
                            break




            return startPoss

            #return bottom - top + 1

def multiplePatternMatching(text, patterns):
    text = text +'$'
    lengthText = len(text)
    lastCol = BWT(text)
    firstOcurrence = firstOcurrences(lastCol)
    k = 100
    countMat = counts(lastCol, k)
    partialSuffixArr = partialSuffixArray(text, k)

    positions = list(map(lambda x: patternMatching(lastCol, x, lengthText, firstOcurrence, countMat, k, partialSuffixArr), patterns))
    positions = list(itertools.chain(*positions))
    return sorted(positions)


if __name__ == "__main__":
    
    file = open('data/multiplePatternMatching.txt', 'r')

    lastCol = file.readline().rstrip('\n')

    patterns = [line.rstrip('\n') for line in file.readlines()]

    positions = multiplePatternMatching(lastCol, patterns)
    print(*positions)
    # for item in positions:
    #     print(item)
