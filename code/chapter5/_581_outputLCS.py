import sys
sys.setrecursionlimit(1500)

def lcsBackTrack(v, w):
    # Input: two strings v and w
    # Output: a BackTrack matrix where each b_ij stores which edge was used to get to s_ij (positions in the distances matrix)

    n = len(v)
    m = len(w)

    backTrackMatrix = [[0 for i in range(m)] for j in range(n)]     
    distances = [[0 for i in range(m+1)] for j in range(n+1)]

    # Fill 1st row
    for j in range(1,m+1):
        distances[0][j] = 0

    # Fill 1st column
    for i in range(1,n+1):
        distances[i][0] = 0

    # Fill the rest of the table
    for i in range(1,n+1):
        for j in range(1, m+1):
            match = 0
            if v[i-1] == w[j-1]:
                match = 1
            
            incomingUp = distances[i-1][j]
            incomingLeft = distances[i][j-1]
            incomingDiag = distances[i-1][j-1] + match
            distances[i][j] = max(incomingUp,incomingLeft,incomingDiag)

            # if distances[i][j] == incomingDiag:
            #     backTrackMatrix[i-1][j-1] = 'diag'
            if distances[i][j] == incomingUp:
                backTrackMatrix[i-1][j-1] = 'up'
            elif distances[i][j] == incomingLeft:
                backTrackMatrix[i-1][j-1] = 'left'
            elif distances[i][j] == incomingDiag:
                backTrackMatrix[i-1][j-1] = 'diag'

    # print(distances)
    # print(backTrackMatrix)
    return backTrackMatrix


def outputLCS(backtrack, v, i, j):
    # Input: backtrack matrix, word v, indices i and j to start backtracking
    # Output: longest common subsequence from v to another word w used in an outer context of this function
  
    if i < 0 or j < 0:
        return ""
    
    if backtrack[i][j] == 'up':
        return outputLCS(backtrack,v,i-1,j)
    elif backtrack[i][j] == 'left':
        return outputLCS(backtrack,v,i,j-1)
    elif backtrack[i][j] == 'diag':
        return outputLCS(backtrack,v,i-1,j-1) + v[i]


def LCS(s,t):
    # Input: Two strings s and t.
    # Output: A longest common subsequence of s and t. (Note: more than one solution may exist, in which case you may output any one.)

    backTrackMatrix = lcsBackTrack(s,t)

    n = len(s) - 1
    m = len(t) - 1

    return outputLCS(backTrackMatrix, s, n, m)

if __name__ == "__main__":
    
    file = open('data/backtrack.txt', 'r')

    s = file.readline().rstrip('\n')
    t = file.readline().rstrip('\n')

    print(LCS(s,t))