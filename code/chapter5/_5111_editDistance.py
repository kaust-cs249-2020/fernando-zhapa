def editDistance(v,w):

    n = len(v)
    m = len(w)

    distances = [[0 for i in range(m+1)] for j in range(n+1)]

     # Fill 1st row
    for j in range(1,m+1):
        distances[0][j] = distances[0][j-1] + 1

    # Fill 1st column
    for i in range(1,n+1):
        distances[i][0] = distances[i-1][0] + 1

    # Fill the rest of the table
    for i in range(1,n+1):
        for j in range(1, m+1):
            if v[i-1] == w[j-1]:
                distances[i][j] = distances[i-1][j-1]
            else:
                incomingDiag = distances[i-1][j-1]
                incomingUp =   distances[i-1][j]
                incomingLeft = distances[i][j-1]

                distances[i][j] = 1 + min(incomingDiag, incomingUp, incomingLeft)

    return distances[n][m]


if __name__ == "__main__":
    
    file = open('data/editDistance.txt', 'r')

    v = file.readline().rstrip('\n')
    w = file.readline().rstrip('\n')

    print(editDistance(v,w))