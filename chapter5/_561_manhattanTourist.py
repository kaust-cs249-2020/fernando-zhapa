def manhattanTourist(n,m,down,right):
    # Input: Integers n and m, followed by an n × (m + 1) matrix Down and an (n + 1) × m matrix Right. The two matrices are separated by the "-" symbol.
    # Output: The length of a longest path from source (0, 0) to sink (n, m) in the rectangular grid whose edges are defined by the matrices Down and Right.

    maxDistances = [[0 for i in range(m+1)] for j in range(n+1)]

    maxDistances[0][0] = 0

    # Fill 1st row
    for j in range(1,m+1):
        maxDistances[0][j] = maxDistances[0][j-1] + right[0][j-1]

    # Fill 1st column
    for i in range(1,n+1):
        maxDistances[i][0] = maxDistances[i-1][0] + down[i-1][0]

    # Fill the rest of the table
    for i in range(1,n+1):
        for j in range(1, m+1):
            incomingUp = maxDistances[i-1][j] + down[i-1][j]
            incomingLeft = maxDistances[i][j-1] + right[i][j-1]

            maxDistances[i][j] = max(incomingUp, incomingLeft)

    print(maxDistances)
    return maxDistances[n][m]


if __name__ == "__main__":
    
    file = open('data/manhattanTourist.txt','r')
    n,m = tuple([int(i) for i in file.readline().split(' ')])

    down = []
    for i in range(n):
        row = [int(i) for i in file.readline().split(' ')]
        down.append(row)
    
    file.readline()
    
    right = []
    for i in range(n+1):
        row = [int(i) for i in file.readline().split(' ')]
        right.append(row)

    print(manhattanTourist(n,m,down,right))