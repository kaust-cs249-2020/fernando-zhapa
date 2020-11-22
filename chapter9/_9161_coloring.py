from copy import deepcopy

class Node():

    def __init__(self, value = None, color = 'gray', children={}):
        self.value = value
        self.color = color
        self.children = children

    def coloringTree(self):

        if self.color != 'gray':
            return

        blues = 0
        reds = 0
        purples = 0
        for _, child in self.children.items():
            child.coloringTree()
            if child.color == 'blue':
                blues += 1
            elif child.color == 'red':
                reds += 1
            elif child.color == 'purple':
                purples += 1
            else:
                print(child.color)
                print("ERROR IN COLORING TREE")

        if purples > 0:
            self.color = 'purple'
        elif blues == 0:
            self.color = 'red'
        elif reds == 0:
            self.color = 'blue'
        else:
            self.color = 'purple'
        

    def printColors(self):
        if self.children == '{{}}':
            return
        
        print(str(self.value) + ': ' + str(self.color))

        for _, child in self.children.items():
            child.printColors()



def buildTree(strings, leavesColors):
    colors = {}
    for line in leavesColors:
        value, color =  tuple(line.split(': '))
        colors[int(value)] = color

    nodes = {}
    while bool(strings):
        string = strings[0]
        value, children = tuple(string.split(' -> '))
        value = int(value)
  
        if children == "{"+ "}":
            newNode =  Node(value=int(value), children={})
            newNode.color = colors[value]
            nodes[value] = deepcopy(newNode)
            strings.pop(0)
        else:
            children = [int(i) for i in children.split(',')]
            allExist = True

            for child in children:
                if not child in nodes:
                    allExist = False
                    break
            
            if allExist:
                newNode = Node(value=value, children={})
                for child in children:
                    newNode.children[child] = deepcopy(nodes[child])
                    del nodes[child]
                nodes[value] = deepcopy(newNode)
                strings.pop(0)
            else:
                strings = strings[1:] + [strings[0]]

    if len(nodes) == 1:
        return list(nodes.items())[0][1]
    else:
        return "ERROR IN BUILD TREE"




if __name__ == "__main__":
    
    file = open("data/coloring.txt", 'r')

    internal = []
    leavesColors = []

    line = file.readline().rstrip('\n')
    while line != '-':
        internal.append(line)
        line = file.readline().rstrip('\n')

    leavesColors = [line.rstrip('\n') for line in file.readlines()]

    tree = buildTree(internal, leavesColors)

    tree.coloringTree()

    tree.printColors()