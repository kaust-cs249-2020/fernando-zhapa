from _961_suffixArrays import suffixArray

def partialSuffixArray(text, k):

    suffixes = suffixArray(text)

    partialSuffixes = []
    
    for i in range(len(suffixes)):

        if suffixes[i]%k ==0:
            partialSuffixes.append((i,suffixes[i]))

    return partialSuffixes



if __name__ == "__main__":
    
    file = open('data/partialSuffixArray.txt', 'r')

    text = file.readline().rstrip('\n')
    k = int(file.readline().rstrip('\n'))
    

    partialSuffixes = partialSuffixArray(text, k)

    toPrint = ''

    for idx, position in partialSuffixes:
        toPrint += str(idx) + ',' + str(position) + '\n'

    print(toPrint[:-1])