import numpy as np

def lcsBackTrack(u, v, w):

    n = len(u)
    m = len(v)
    o = len(w)

    backTrackMatrix = [[[0 for i in range(o)] for j in range(m)] for k in range(n)]     
    distances = [[[0 for i in range(o+1)] for j in range(m+1)] for k in range (n+1)]

    # # Fill 1st row
    # for j in range(1,m+1):
    #     distances[0][j] = distances[0][j-1] - indelPenalty

    # # Fill 1st column
    # for i in range(1,n+1):
    #     distances[i][0] = distances[i-1][0] - indelPenalty

    # Fill the rest of the table
    for i in range(1,n+1):
        for j in range(1, m+1):
            for k in range(1,o+1):
                match = 0
                if u[i-1] == w[k-1] and v[j-1] == w[k-1]:
                    match = 1
            
       
                
                delVW = distances[i-1][j][k] 
                delUV = distances[i][j][k-1]
                delUW = distances[i][j-1][k]
                delU = distances[i][j-1][k-1]
                delV = distances[i-1][j][k-1]
                delW = distances[i-1][j-1][k]
                diag = distances[i-1][j-1][k-1] + match
                distances[i][j][k] = max(delUV, delUW, delVW, delV, delU, delW, diag)

                if distances[i][j][k] == delUV:
                    backTrackMatrix[i-1][j-1][k-1] = 'delUV'
                elif distances[i][j][k] == delVW:
                    backTrackMatrix[i-1][j-1][k-1] = 'delVW'
                elif distances[i][j][k] == delUW:
                    backTrackMatrix[i-1][j-1][k-1] = 'delUW'
                elif distances[i][j][k] == delV:
                    backTrackMatrix[i-1][j-1][k-1] = 'delV'
                elif distances[i][j][k] == delW:
                    backTrackMatrix[i-1][j-1][k-1] = 'delW'
                elif distances[i][j][k] == delU:
                    backTrackMatrix[i-1][j-1][k-1] = 'delU'
                elif distances[i][j][k] == diag:
                    backTrackMatrix[i-1][j-1][k-1] = 'diag'

    # print(distances)
    # print(backTrackMatrix)
    return (distances, backTrackMatrix)


def outputLCS(backtrack, u, v, w, i, j, k, alignU, alignV, alignW):

    print(backtrack[i][j][k])
    if i < 0 and j < 0 and k < 0:
        return (alignU[::-1], alignV[::-1], alignW[::-1])
    
    if i < 0 and j < 0:
        newAlignU = alignU + '-'
        newAlignV = alignV + '-'
        newAlignW = alignW + w[k]
        return outputLCS(backtrack,u,v,w,i,j,k-1, newAlignU, newAlignV, newAlignW)

    if i < 0 and k < 0:
        newAlignU = alignU + '-'
        newAlignV = alignV + v[j]
        newAlignW = alignW + '-'
        return outputLCS(backtrack,u,v,w,i,j-1,k, newAlignU, newAlignV, newAlignW)

    if j < 0 and k < 0:
        newAlignU = alignU + u[i]
        newAlignV = alignV + '-'
        newAlignW = alignW + '-'
        return outputLCS(backtrack,u,v,w,i-1,j,k, newAlignU, newAlignV, newAlignW)

    if i < 0:
        newAlignU = alignU + '-'
        newAlignV = alignV + v[j]
        newAlignW = alignW + w[k]
        return outputLCS(backtrack,u,v,w,i,j-1,k-1, newAlignU, newAlignV, newAlignW)

    if j < 0:
        newAlignU = alignU + u[i]
        newAlignV = alignV + '-'
        newAlignW = alignW + w[k]
        return outputLCS(backtrack,u,v,w,i-1,j,k-1, newAlignU, newAlignV, newAlignW)


    if k < 0:
        newAlignU = alignU + u[i]
        newAlignV = alignV + v[j]
        newAlignW = alignW + '-'
        return outputLCS(backtrack,u,v,w,i-1,j-1,k, newAlignU, newAlignV, newAlignW)





    if backtrack[i][j][k] == 'delUW':
        newAlignU = alignU + '-'
        newAlignV = alignV + v[j]
        newAlignW = alignW + '-'
        return outputLCS(backtrack,u,v,w,i,j-1,k,newAlignU,newAlignV,newAlignW)
    elif backtrack[i][j][k] == 'delVW':
        newAlignU = alignU + u[i]
        newAlignV = alignV + '-'
        newAlignW = alignW + '-'
        return outputLCS(backtrack,u,v,w,i-1,j,k,newAlignU,newAlignV,newAlignW)
    elif backtrack[i][j][k] == 'delUV':
        newAlignU = alignU + '-'
        newAlignV = alignV + '-'
        newAlignW = alignW + w[k]
        return outputLCS(backtrack,u,v,w,i,j,k-1,newAlignU,newAlignV,newAlignW)
    elif backtrack[i][j][k] == 'delU':
        newAlignU = alignU + '-'
        newAlignV = alignV + v[j]
        newAlignW = alignW + w[k]
        return outputLCS(backtrack,u,v,w,i,j-1,k-1,newAlignU,newAlignV,newAlignW)
    elif backtrack[i][j][k] == 'delV':
        newAlignU = alignU + u[i]
        newAlignV = alignV + '-'
        newAlignW = alignW + w[k]
        return outputLCS(backtrack,u,v,w,i-1,j,k-1,newAlignU,newAlignV,newAlignW)
    elif backtrack[i][j][k] == 'delW':
        newAlignU = alignU + u[i]
        newAlignV = alignV + v[j]
        newAlignW = alignW + '-'
        return outputLCS(backtrack,u,v,w,i-1,j-1,k,newAlignU,newAlignV,newAlignW)
    elif backtrack[i][j][k] == 'diag':
        newAlignU = alignU + u[i]
        newAlignV = alignV + v[j]
        newAlignW = alignW + w[k]
        return outputLCS(backtrack,u,v,w,i-1,j-1,k-1,newAlignU,newAlignV,newAlignW)


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

def multipleAlignment(u,v,w):

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

    scoreMatrix = readScoreMatrix('data/BLOSUM62.txt')
    indelPenalty = 5


    n = len(u)
    m = len(v)
    o = len(w)
    distances, backtrack = lcsBackTrack(u,v, w)
    alignU, alignV, alignW = outputLCS(backtrack, u, v, w, n-1, m-1, o-1, "", "", "") 

    return (distances[n][m][o], alignU, alignV, alignW)


if __name__ == "__main__":
    
    file = open('data/multipleAlignment.txt', 'r')

    u = file.readline().rstrip('\n')
    v = file.readline().rstrip('\n')
    w = file.readline().rstrip('\n')

    print(u,v,w)
    score, alignU, alignV, alignW = multipleAlignment(u,v,w)

    print(score)
    print(alignU)
    print(alignV)
    print(alignW)