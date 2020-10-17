import numpy as np




def lcsBackTrack(v, w):

    n = len(v)
    m = len(w)

    backTrackMatrix = [[0 for i in range(m)] for j in range(n)]     
    distances = [[0 for i in range(m+1)] for j in range(n+1)]

    # # Fill 1st row
    # for j in range(1,m+1):
    #     distances[0][j] = distances[0][j-1] - 1 # -1 is the index penalty

    # # Fill 1st column
    # for i in range(1,n+1):
    #     distances[i][0] = distances[i-1][0] - 1

    # Fill the rest of the table
    for i in range(1,n+1):
        for j in range(1, m+1):
            if v[i-1] == w[j-1]:
                match = 1
            else:
                match = -1
   
            
            incomingUp = distances[i-1][j] - 1
            incomingLeft = distances[i][j-1] - 1
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



def fittingAlignment(v,w):

    n = len(v)
    m = len(w)

    distances, backtrack = lcsBackTrack(v, w)

    distances = np.array(distances)
    i = np.argmax(distances[:,m])
   

    substringV = v[:i]

    score = distances[i][m]
    alignV, alignW = outputLCS(backtrack, substringV, w, i-1, m-1, "", "")


    return score , alignV, alignW


if __name__ == "__main__":
    
    file = open('data/fittingAlignment.txt', 'r')

    v = file.readline().rstrip('\n')
    w = file.readline().rstrip('\n')

    score, alignV, alignW = fittingAlignment(v,w)

    print(score)
    print(alignV)
    print(alignW)