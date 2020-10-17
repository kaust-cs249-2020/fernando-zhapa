import numpy as np
from math import ceil, floor
import os

from _5131_middleEdge import middleEdge
from _5101_globalAlignment import readScoreMatrix

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


# LinearSpaceAlignment(v, w, top, bottom, left, right)
#     if left = right
#         output path formed by bottom − top vertical edges
#     if top = bottom
#         output path formed by right − left horizontal edges
#     middle ← ⌊ (left + right)/2⌋
#     midEdge ← MiddleEdge(v, w, top, bottom, left, right)
#     midNode ← vertical coordinate of the initial node of midEdge 
#     LinearSpaceAlignment(v, w, top, midNode, left, middle)
#     output midEdge
#     if midEdge = "→" or midEdge = "↘"
#         middle ← middle + 1
#     if midEdge = "↓" or midEdge ="↘"
#         midNode ← midNode + 1 
#     LinearSpaceAlignment(v, w, midNode, bottom, middle, right)

def linearSpaceAlignment(v, w, top, bottom, left, right, indelPenalty):
    middle = floor((left+right)/2)
    # print(top, bottom, left, right, v, w, middle)

    scoreMatrix = readScoreMatrix('data/BLOSUM62.txt')

    if len(v) != bottom-top:
        print(v)
        print(bottom,top)
        print("v and bottom-top do not have the same size")
        return ['errorTB']
    if len(w) != right-left:
        print("v and right-left+1 do not have the same size")
        
        return ['errorRL']



    if left == right:
        # indexW =  aminos[w[0]]
        # indexV = aminos[v[-1]]      
        # match = scoreMatrix[indexV][indexW]
        return 0, ["down"]*(bottom-top)
    if top == bottom:
        # indexW =  aminos[w[-1]]
        # indexV = aminos[v[0]]      
        # match = scoreMatrix[indexV][indexW]
        return 0, ["right"]*(right-left)
    
    # middle = floor((left+right)/2)
    midEdge = middleEdge(v, w, 5)

    start, end, score, dirMidEdge = midEdge  
    # print(start, end, dirMidEdge)
    # print('\n\n')
    ini, ter = start
    middle = ter
    midNode = ini

    (scoreFirst, firstHalf) = linearSpaceAlignment(v[0:midNode],w[0:middle],0,midNode,0,middle, indelPenalty)


    # print('middel ', middle)    
    if dirMidEdge == 'right':
        middle += 1
    elif dirMidEdge == 'down': 
        midNode += 1
    elif dirMidEdge == 'diag':
        middle += 1
        midNode += 1

    
    # print("startend", end, (midNode, middle), bottom)
    # print("VVVVVV: ", v[midNode:bottom])
    revV = (v[midNode:bottom])[::-1]
    revW = (w[middle:right])[::-1]
    (scoreSecond, secondHalf) = linearSpaceAlignment( revV,revW, 0, bottom-midNode, 0, right-middle, indelPenalty)


    return (score + scoreSecond, firstHalf + [dirMidEdge] + secondHalf[::-1])


def backtrack(v,w,path):
    alignV = ""
    alignW = ""

    idxV = 0
    idxW = 0
    for elem in path:
        if elem == 'diag':
            alignV += v[idxV]
            alignW += w[idxW]
            idxV += 1
            idxW += 1
        elif elem == 'right':
            alignV += '-'
            alignW += w[idxW]
            idxW += 1
        elif elem == 'down':
            alignV += v[idxV]
            alignW += '-'
            idxV += 1
    return alignV, alignW


if __name__ == "__main__":
   
    file = open('data/linearSpaceAlignment.txt', 'r')

    v = file.readline().rstrip('\n')
    w = file.readline().rstrip('\n')

    n = len(v)
    m = len(w)

    indelPenalty = 5

    score ,path = linearSpaceAlignment(v, w, 0, n, 0, m, indelPenalty)
    alignV, alignW = backtrack(v,w,path)

    print(score)
    print(path)
    print(alignV)
    print(alignW)



