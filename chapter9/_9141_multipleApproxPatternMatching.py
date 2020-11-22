from math import floor
from _9131_multiplePatternMatching import patternMatching, counts
from _971_BWT import BWT
from _9111_betterBWMatching import firstOcurrences
from _9171_partialSuffixArray import partialSuffixArray


def hammingDistance(string1, string2):
    if (len(string1) != len(string2)):
        return -1
    hamm = 0
    for i in range(len(string1)):
        if string1[i] != string2[i]:
            hamm += 1
    return hamm


def multipleApproxPatternMatching(text, patterns, threshold):
    text = text +'$'
    lengthText = len(text)
    lastCol = BWT(text)
    firstOcurrence = firstOcurrences(lastCol)
    kk = 100
    countMat = counts(lastCol, kk)
    partialSuffixArr = partialSuffixArray(text, kk)

    realPositions = []
    for pattern in patterns:
        n = len(pattern)
        k = floor(n/(threshold+1))

        patternPositions = set()
        for i in range(threshold +1):
            subPattern = pattern[k*i:k*i + k]
         
            positions = patternMatching(lastCol, subPattern, lengthText, firstOcurrence, countMat, kk, partialSuffixArr)

            for position in positions:
                subString = text[position-i*k:position-i*k + n]
                if hammingDistance(subString, pattern) <= threshold:
                    patternPositions.add(position-i*k)

        realPositions += list(patternPositions)

    return sorted(realPositions)




if __name__ == "__main__":
    
    file = open('data/multipleApproxPatternMatching.txt', 'r')

    lastCol = file.readline().rstrip('\n')

    patterns = file.readline().rstrip('\n').split(' ')
    threshold = int(file.readline().rstrip('\n'))

    positions = multipleApproxPatternMatching(lastCol, patterns, threshold)
    print(*positions)
    # for item in positions:
    #     print(item)
