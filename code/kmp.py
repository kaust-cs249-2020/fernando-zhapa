def buildTable(string):
    table = [0]
    marker = 0
    for i in range(1,len(string)):
        if string[i] == string[marker]:
            marker += 1
            table.append(table[i-1] + 1)
        else:
            while marker > 0 and string[table[marker-1]] != string[i]:
                marker = table[marker-1]
            if marker == 0:
                table.append(0)
            else:
                table.append(table[marker-1] + 1)
    return table

# print(buildTable("ABCDABD"))        #[0, 0, 0, 0, 1, 2, 0]
# print(buildTable("ABCDABCA"))       #[0, 0, 0, 0, 1, 2, 3, 1]
# print(buildTable("AABAABAAA"))      #[0, 1, 0, 1, 2, 3, 4, 5, 2]


def kmp(text, word):
    i = 0
    k = 0
    count = 0
    table = buildTable(word)
    positions = []
    while i < len(text):
        if text[i] == word[k]:
            k+=1
            i+=1
            if k == len(word):
                positions.append(i-k)
                count +=1
                k = table[k-1]
        else:
            # k = table[k-1]
            # # if k == 0:
            # #     i+=1
            # #     k+=1
            if k == 0:
                i+=1
            else:
                k = table[k-1]        
    return count, positions