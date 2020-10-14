import numpy as np

def lcsBackTrack(v, w, indexAmino, scoreMatrix, indelPenalty):

    n = len(v)
    m = len(w)

    backTrackMatrix = [[0 for i in range(m)] for j in range(n)]     
    distances = [[0 for i in range(m+1)] for j in range(n+1)]

    # Fill 1st row
    for j in range(1,m+1):
        distances[0][j] = distances[0][j-1] - indelPenalty

    # Fill 1st column
    for i in range(1,n+1):
        distances[i][0] = distances[i-1][0] - indelPenalty

    # Fill the rest of the table
    for i in range(1,n+1):
        for j in range(1, m+1):
        
            indexV = indexAmino[v[i-1]]
            indexW =  indexAmino[w[j-1]]
            match = scoreMatrix[indexV][indexW]
            
            incomingUp = distances[i-1][j] - indelPenalty
            incomingLeft = distances[i][j-1] - indelPenalty
            incomingDiag = distances[i-1][j-1] + match
            distances[i][j] = max(0,incomingUp,incomingLeft,incomingDiag)

            if distances[i][j] == 0:
                backTrackMatrix[i-1][j-1] = 'ride'
            elif distances[i][j] == incomingUp:
                backTrackMatrix[i-1][j-1] = 'up'
            elif distances[i][j] == incomingLeft:
                backTrackMatrix[i-1][j-1] = 'left'
            elif distances[i][j] == incomingDiag:
                backTrackMatrix[i-1][j-1] = 'diag'

    # print(distances)
    # print(backTrackMatrix)
    return (distances, backTrackMatrix)


def outputLCS(backtrack, v, w, i, j, alignV, alignW):

    
    if i < 0 and j < 0:
        return (alignV[::-1], alignW[::-1])
    
    if i < 0:
        newAlignV = alignV + '-'
        newAlignW = alignW + w[j]
        return outputLCS(backtrack,v,w,i,j-1, newAlignV, newAlignW)

    if j < 0:
        newAlignV = alignV + v[i]
        newAlignW = alignW + '-'
        return outputLCS(backtrack,v,w,i-1,j, newAlignV, newAlignW)

  
    if backtrack[i][j] == 'ride':
        newAlignV = alignV + v[i]
        newAlignW = alignW + w[i]
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


def readScoreMatrix(path):
    file = open(path, 'r')
    line = file.readline()

    matrix = []
    line = file.readline().strip('\n')
    while line != "":
        line = [int(i) for i in line.split(' ')[1:] if i != '']
        matrix.append(line)
        line = file.readline().strip('\n')

    return matrix

def localAlignment(v,w):

    aminos = {
        'A':  0, 
        'C':  1, 
        'D':  2, 
        'E':  3, 
        'F':  4, 
        'G':  5, 
        'H':  6, 
        'I':  7, 
        'K':  8, 
        'L':  9, 
        'M': 10, 
        'N': 11, 
        'P': 12, 
        'Q': 13, 
        'R': 14, 
        'S': 15, 
        'T': 16, 
        'V': 17, 
        'W': 18, 
        'Y': 19}

    scoreMatrix = readScoreMatrix('data/PAM250.txt')
    indelPenalty = 5

    n = len(v)
    m = len(w)

    distances, backtrack = lcsBackTrack(v, w, aminos, scoreMatrix, indelPenalty)

    endPath = (0,0)
    largestDist = float('-inf')
    for i in range(len(distances)):
        for j in range(len(distances[0])):
            if distances[i][j] > largestDist:
                largestDist = distances[i][j]
                endPath = (i,j)

    print(endPath)
    i,j = endPath
    alignV, alignW = outputLCS(backtrack, v, w, i-1, j-1, "", "") 

    return (distances[i][j], alignV, alignW)


if __name__ == "__main__":
    
    file = open('data/localAlignment.txt', 'r')

    v = file.readline().rstrip('\n')
    w = file.readline().rstrip('\n')

    score, alignV, alignW = localAlignment(v,w)

    print(score)
    print(alignV)
    print(alignW)