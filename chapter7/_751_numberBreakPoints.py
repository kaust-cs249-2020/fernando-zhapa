def numberOfBreakpoints(permutation):
    p = len(permutation)
    permutation = [0] + permutation[:] + [p+1]
    breakpoints = 0
    for i in range(p):
        if(permutation[i+1] - permutation[i]) != 1:
            breakpoints += 1
    return breakpoints


if __name__ == "__main__":
    file = open('data/numberBreakpoints.txt', 'r')

    permutation = [int(i) for i in file.readline().split(' ')]

    print(numberOfBreakpoints(permutation))