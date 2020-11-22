
def k_occurrences(column):

    column = [char for char in column]
    dict = {}

    for i in range(len(column)):
        if not column[i] in dict:
            dict[column[i]] = 1
            column[i] = ( dict[column[i]], column[i])

        else:
            dict[column[i]] += 1
            column[i] = ( dict[column[i]], column[i])
    
    return column

def BWMatching(lastCol, pattern):

    firstCol = sorted(lastCol)

    firstColExt = k_occurrences(firstCol)

    lastColExt = k_occurrences(lastCol)

    lastToFirst = [firstColExt.index(lastColExt[i]) for i in range(len(lastColExt))]


    top = 0
    bottom = len(lastCol) - 1

    while top <= bottom:
        if bool(pattern):
            symbol = pattern[-1]
            pattern = pattern[:-1]

            try:
                top = lastCol.index(symbol, top, bottom+1)
            except:
                return 0
           

            for i in range(top,bottom+1):
                if lastCol[i] == symbol:
                    bottom = i
            
            top = lastToFirst[top]
            bottom = lastToFirst[bottom]
        else:
            return bottom - top + 1


def BWMatching_Multiple(lastCol, patterns):

    return list(map(lambda x: BWMatching(lastCol,x), patterns))


if __name__ == "__main__":
    
    file = open('data/BWMatching.txt', 'r')

    lastCol = file.readline().rstrip('\n')

    patterns = file.readline().rstrip('\n').split(' ')


    print(*BWMatching_Multiple(lastCol, patterns))