import numpy as np
from _5101_globalAlignment import readScoreMatrix

def lcsBackTrack(v, w, indexAmino, scoreMatrix, openGapPenalty, extendGapPenalty):

    n = len(v)
    m = len(w)

    upperLevel  = [[0 for i in range(m+1)] for j in range(n+1)]
    middleLevel = [[0 for i in range(m+1)] for j in range(n+1)]
    lowerLevel  = [[0 for i in range(m+1)] for j in range(n+1)]

    backTrackUpper  = [["" for i in range(m)] for j in range(n)]
    backTrackLower  = [["" for i in range(m)] for j in range(n)]
    backTrackMiddle = [["" for i in range(m)] for j in range(n)]


    # Fill the three levels
    for i in range(1,n+1):
        for j in range(1, m+1):
           

            #Lower level recurrence
            extendingGap = lowerLevel[i-1][j] - extendGapPenalty
            openingGap = middleLevel[i-1][j] - openGapPenalty
            lowerLevel[i][j] = max(extendingGap,openingGap)

            if lowerLevel[i][j] == extendingGap:
                backTrackLower[i-1][j-1] = 'lower'
            else:
                backTrackLower[i-1][j-1] = 'middle_lower'


            #Upper level recurrence
            extendingGap = upperLevel[i][j-1] - extendGapPenalty
            openingGap = middleLevel[i][j-1] - openGapPenalty
            upperLevel[i][j] = max(extendingGap,openingGap)

            if upperLevel[i][j] == extendingGap:
                backTrackUpper[i-1][j-1] = 'upper'
            else:
                backTrackUpper[i-1][j-1] = 'middle_upper'


            #Middle level recurrence
            indexV = indexAmino[v[i-1]]
            indexW =  indexAmino[w[j-1]]
            match = scoreMatrix[indexV][indexW]
            

            fromLower = lowerLevel[i][j]
            fromUpper = upperLevel[i][j]
            fromDiag =  middleLevel[i-1][j-1] + match
            middleLevel[i][j] = max(fromLower, fromUpper, fromDiag)

            if middleLevel[i][j] == fromLower:
                backTrackMiddle[i-1][j-1] = 'lower_middle'
            elif middleLevel[i][j] == fromUpper:
                backTrackMiddle[i-1][j-1] = 'upper_middle'
            else:
                backTrackMiddle[i-1][j-1] = 'middle'
    # print(distances)
    # print(backTrackMatrix)
   # return (distances, backTrackMatrix)

    return middleLevel[n][m], backTrackUpper, backTrackLower, backTrackMiddle



def outputLCS(backtrackMatrices, v, w, i, j, level, alignV, alignW):

    upper, lower, middle = backtrackMatrices

    if level == 'upper':
        backtrack = upper
    elif level == 'lower':
        backtrack = lower
    elif level == 'middle':
        backtrack = middle

    if i < 0 and j < 0:
        return (alignV[::-1], alignW[::-1])
    
    # if i < 0:
    #     newAlignV = alignV + '-'
    #     newAlignW = alignW + w[j]
    #     return outputLCS(backtrackMatrices,v,w,i,j-1, 'upper', newAlignV, newAlignW)

    # if j < 0:
    #     newAlignV = alignV + v[i]
    #     newAlignW = alignW + '-'
    #     return outputLCS(backtrackMatrices,v,w,i-1,j, 'lower', newAlignV, newAlignW)

    if backtrack[i][j] == 'lower':
        newAlignV = alignV + v[i]
        newAlignW = alignW + '-'
        return outputLCS(backtrackMatrices,v,w,i-1,j, 'lower', newAlignV, newAlignW)
    elif backtrack[i][j] == 'upper':
        newAlignV = alignV + '-'
        newAlignW = alignW + w[j]
        return outputLCS(backtrackMatrices,v,w,i,j-1, 'upper', newAlignV, newAlignW)
    elif backtrack[i][j] == 'middle':
        newAlignV = alignV + v[i]
        newAlignW = alignW + w[j]
        return outputLCS(backtrackMatrices,v,w,i-1,j-1, 'middle', newAlignV, newAlignW)
    elif backtrack[i][j] == 'middle_lower':
        newAlignV = alignV + v[i]
        newAlignW = alignW + '-'
        return outputLCS(backtrackMatrices,v,w,i-1,j, 'middle', newAlignV, newAlignW)
    elif backtrack[i][j] == 'middle_upper':
        newAlignV = alignV + '-'
        newAlignW = alignW + w[j]
        return outputLCS(backtrackMatrices,v,w,i,j-1, 'middle', newAlignV, newAlignW)
    elif backtrack[i][j] == 'lower_middle':
        newAlignV = alignV
        newAlignW = alignW
        return outputLCS(backtrackMatrices,v,w,i,j, 'lower', newAlignV, newAlignW)
    elif backtrack[i][j] == 'upper_middle':
        newAlignV = alignV
        newAlignW = alignW
        return outputLCS(backtrackMatrices,v,w,i,j, 'upper', newAlignV, newAlignW)



def affineGapAlignment(v,w):

    n = len(v)
    m = len(w)

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
    extendGapPenalty = 1
    openGapPenalty = 15

    score, btUpper, btLower, btMiddle = lcsBackTrack(v,w,aminos,scoreMatrix,openGapPenalty, extendGapPenalty)
    alignV, alignW = outputLCS((btUpper, btLower, btMiddle), v, w, n-1, m-1, 'middle', "", "")

    return score, alignV, alignW

if __name__ == "__main__":
    
    file = open('data/affineGapAlignment.txt', 'r')

    v = file.readline().rstrip('\n')
    w = file.readline().rstrip('\n')

    score, alignV, alignW = affineGapAlignment(v,w)
    print(score)
    print(alignV)
    print(alignW)