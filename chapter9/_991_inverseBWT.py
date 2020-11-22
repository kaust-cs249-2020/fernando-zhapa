def inverseBWT(lastCol):

    firstCol = sorted(lastCol)
    firstCol = [char for char in firstCol]

    lastCol = [char for char in lastCol]

    dict = {}

    for i in range(len(firstCol)):
        if not firstCol[i] in dict:
            dict[firstCol[i]] = 1
            firstCol[i] = ( dict[firstCol[i]], firstCol[i])

        else:
            dict[firstCol[i]] += 1
            firstCol[i] = ( dict[firstCol[i]], firstCol[i])

    dict = {}
    
    for i in range(len(lastCol)):
        if not lastCol[i] in dict:
            dict[lastCol[i]] = 1
            lastCol[i] = ( dict[lastCol[i]], lastCol[i])

        else:
            dict[lastCol[i]] += 1
            lastCol[i] = ( dict[lastCol[i]], lastCol[i])



    inFirst = firstCol[0]
    idxInLast = lastCol.index(inFirst)

    actualStr = ''
    while idxInLast != 0:

        actualStr += str(firstCol[idxInLast][1])
        
        inFirst = firstCol[idxInLast]
        idxInLast = lastCol.index(inFirst)

    return actualStr + '$'

if __name__ == "__main__":
    

    file =  open('data/inverseBWT.txt', 'r')

    text = file.readline().rstrip('\n')

    print(inverseBWT(text))