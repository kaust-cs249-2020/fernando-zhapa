file = open('data/extra.txt', 'r')

text =  [int(i) for i in file.readline().rstrip('\n').split(' ')]

text.sort()

for item in text:
    print(item)