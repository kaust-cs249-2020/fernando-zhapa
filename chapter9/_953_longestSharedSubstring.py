from _951_suffixTree import Node
from copy import deepcopy

class ColoredNode(Node):


    def __init__(self, position = None, symbol = None, startPos =  None, length = None, children = {}, color = 'gray'):
        super().__init__(position, symbol, startPos, length, children) 

        self.color = color

    def isRoot(self):
        return self.symbol == 'ROOT'
    def coloringTree(self, lenStr1):

        if self.children == {}:
            if self.position < lenStr1:
                self.color = 'blue'
            else:
                self.color = 'red'

            return

        blues = 0
        reds = 0
        purples = 0
        for _, child in self.children.items():
            child.coloringTree(lenStr1)
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
        

    def deepestPurpleNode(self, wholeText, currString=""):
        sharedStr = currString

        for _, child in self.children.items():
            if child.color == 'purple':
                start = child.position
                length = child.length
                stringInNode = currString + wholeText[start:start+length+1]
                candidateStr = child.deepestPurpleNode(wholeText, stringInNode)

                sharedStr = max([sharedStr,candidateStr], key=len)

        return sharedStr

    # For SHORTEST NON-SHARED SUBSTRING
    def shallowestNonPurpleNode(self, wholeText, currString=''):
        nonshared = wholeText # Just to have an starting value for "min" operation

        for _, child in self.children.items():
            if child.color == 'purple':
          
                start = child.position
                length = child.length

                string = currString + wholeText[start: start+length]

                if not '$' in string and not '#' in string:
                    candidate = child.shallowestNonPurpleNode(wholeText, string)
                    nonshared = min([nonshared, candidate], key=len)

            elif child.color == 'blue':

                start = child.position
                string = currString + wholeText[start]
                if not '#' in string:

                    if len(string)<len(nonshared):
                        nonshared = string 

                        
            elif child.color == 'red':
                start = child.position
                string = currString + wholeText[start]
                if not '$' in string:
                    if len(string)<len(nonshared):
                        nonshared = string 
 

            else:
                print("NON ADMITTED COLOR")
                return


    
        return nonshared #


    def printColors(self):
        if self.children == '{{}}':
            return
        
        print(str(self.symbol) + ': ' + str(self.color))

        for _, child in self.children.items():
            child.printColors()



def modifiedSuffixTrieConstruction(text):
    rootNode = ColoredNode()
    
    for i in range(len(text)):
        currentNode = rootNode
        for j in range(i,len(text)):
            symbol = text[j]
            if symbol in currentNode.children:
                currentNode = currentNode.children[symbol]
            else:       
                newNode = ColoredNode(position= j, symbol= symbol, children={})
                currentNode.children[symbol] = deepcopy(newNode)
                currentNode = currentNode.children[symbol]

        # if currentNode.isLeaf():
        #     currentNode.position = i
    return rootNode


if __name__ == "__main__":
    

    file = open('data/longestShared.txt', 'r')

    str1 = file.readline().rstrip('\n')
    str2 = file.readline().rstrip('\n')

    wholeText = str1 + '#' + str2 + '$'

    tree = modifiedSuffixTrieConstruction(wholeText)
 

    tree.shrinkTrie(0)

    tree.coloringTree(len(str1))

    shared = tree.deepestPurpleNode(wholeText)

    print(shared)