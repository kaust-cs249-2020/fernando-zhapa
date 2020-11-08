import numpy as np

def lcsBackTrack(v, w):

    n = len(v)
    m = len(w)

    backTrackMatrix = [[0 for i in range(m)] for j in range(n)]     
    distances = [[0 for i in range(m+1)] for j in range(n+1)]


    for i in range(1,n+1):
        for j in range(1, m+1):
            if v[i-1] == w[j-1]:
                match = 1
            else:
                match = -2
   
            
            incomingUp = distances[i-1][j] - 2
            incomingLeft = distances[i][j-1] - 2
            incomingDiag = distances[i-1][j-1] + match
            distances[i][j] = max(incomingUp,incomingLeft,incomingDiag)

            if distances[i][j] == incomingUp:
                backTrackMatrix[i-1][j-1] = 'up'
            elif distances[i][j] == incomingLeft:
                backTrackMatrix[i-1][j-1] = 'left'
            elif distances[i][j] == incomingDiag:
                backTrackMatrix[i-1][j-1] = 'diag'

    # print(distances)
    # print(backTrackMatrix)
    return distances, backTrackMatrix


def outputLCS(backtrack, v, w, i, j, alignV, alignW):
    if i < 0 and j < 0:
        return (alignV[::-1], alignW[::-1])
    
    if i < 0:
        newAlignV = alignV + '-'
        newAlignW = alignW + w[j]
        return outputLCS(backtrack,v,w,i,j-1, newAlignV, newAlignW)

    if j < 0:
        return (alignV[::-1], alignW[::-1])


    if backtrack[i][j] == 'up':
        newAlignV = alignV + v[i]
        newAlignW = alignW + '-'
        return outputLCS(backtrack,v,w,i-1,j, newAlignV, newAlignW)
    elif backtrack[i][j] == 'left':
        newAlignV = alignV + '-'
        newAlignW = alignW + w[j]
        return outputLCS(backtrack,v,w,i,j-1, newAlignV, newAlignW)
    elif backtrack[i][j] == 'diag':
        newAlignV = alignV + v[i]
        newAlignW = alignW + w[j]
        return outputLCS(backtrack,v,w,i-1,j-1, newAlignV, newAlignW)



def overlapAlignment(v,w):

    n = len(v)
    m = len(w)

    distances, backtrack = lcsBackTrack(v, w)

    distances = np.array(distances)

    reverseLastRow =  distances[n,:][::-1]

    j = len(reverseLastRow) - np.argmax(reverseLastRow) - 1 #last index of maximum value


    prefixW = w[:j]

    score = distances[n][j]
    alignV, alignW = outputLCS(backtrack, v, prefixW, n-1, j-1, "", "")


    return score , alignV, alignW


if __name__ == "__main__":
    
    file = open('data/overlapAlignment.txt', 'r')

    v = file.readline().rstrip('\n')
    w = file.readline().rstrip('\n')

    score, alignV, alignW = overlapAlignment(v,w)

    print(score)
    print(alignV)
    print(alignW)