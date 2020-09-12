#####################################
##########PROBABILITY###############

def generateAllStrings(length,alphabet):
    if length == 1:
        return alphabet
    strings = []
    for character in alphabet:
        for string in generateAllStrings(length-1, alphabet):
            strings.append(character+string)
    return strings

#spacedPrint(generateAllStrings(4,['0','1']))

def probSubstring(substr, length, alphabet):
    allStrings = generateAllStrings(length, alphabet)
    count = 0
    for string in allStrings:
        if substr in string:
            count += 1
    return count/len(allStrings)

print(probSubstring("01", 25, ['0','1']))

