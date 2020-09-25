from _331_pathToGenome import pathToGenome

def readGappedSequence(strings):
    sequence = []
    for item in strings:
        gappedKmers = item.split('|')
        initial = gappedKmers[0]
        terminal = gappedKmers[1]
        sequence.append((initial,terminal))
    return sequence


def stringSpelledByGappedPatterns(k, d, sequence):

    # Input: Integers k and d followed by a sequence of (k, d)-mers (a1|b1), … , (an|bn) such that Suffix(ai|bi) = Prefix(ai+1|bi+1) for 1 ≤ i ≤ n-1.
    # Output: A string Text of length k + d + k + n - 1 such that the i-th (k, d)-mer in Text is equal to (ai|bi)  for 1 ≤ i ≤ n (if such a string exists).
    firstPatterns = []
    secondPatterns = []

    for item in sequence:
        firstPatterns.append(item[0])
        secondPatterns.append(item[1])

    prefixString = pathToGenome(firstPatterns)
    suffixString = pathToGenome(secondPatterns)

    
    for i in range(k+d,len(prefixString)):
        if prefixString[i] != suffixString[i-k-d]:
            return "there is no string spelled by the gapped patterns"
    return prefixString[:k+d] + suffixString




if __name__ == "__main__":
    file = open("/home/ferynando7/KAUST/Fall2020/CS249/fernando-zhapa/data/gappedSequence.txt", 'r')
    sequenceStr = [line.rstrip('\n') for line in file]
    sequence = readGappedSequence(sequenceStr)


  
    print(stringSpelledByGappedPatterns(50,200,sequence))