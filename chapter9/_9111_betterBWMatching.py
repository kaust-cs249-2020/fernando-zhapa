def firstOcurrences(array):
    array = sorted(array)
    occurs = {}
    for i in range(len(array)):
        if not array[i] in occurs:
            occurs[array[i]] = i 
    
    return occurs

def count(symbol, bound, array):
    occur = 0
    for i in range(bound):
        if array[i] == symbol:
            occur += 1
    
    return occur


def betterBWMatching(lastCol, pattern):

    top = 0
    bottom = len(lastCol) - 1

    firstOcurrence = firstOcurrences(lastCol)

    while top <= bottom:
        if bool(pattern):
            symbol = pattern[-1]
            pattern = pattern[:-1]

            try:
                top = lastCol.index(symbol, top, bottom+1)
            except:
                return 0
            
            top = firstOcurrence[symbol] + count(symbol, top, lastCol) 
            bottom = firstOcurrence[symbol] + count(symbol, bottom+1, lastCol) - 1


        else:
            return bottom - top + 1


def betterBWMatching_Multiple(lastCol, patterns):

    return list(map(lambda x: betterBWMatching(lastCol,x), patterns))


if __name__ == "__main__":
    
    file = open('data/betterBWMatching.txt', 'r')

    lastCol = file.readline().rstrip('\n')

    patterns = file.readline().rstrip('\n').split(' ')


    print(*betterBWMatching_Multiple(lastCol, patterns))