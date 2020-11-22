from _951_suffixTree import Node
import ast
from copy import deepcopy

class PNode(Node):
    def __init__(self, position = None, symbol = None, startPos =  None, length = None, children = {}, descent = None, parent = None):
        super().__init__(position, symbol, startPos, length, children) 

        self.descent = descent
        self.parent = parent


    def printTree(self, text):
        
        if self.children != {}:
            for _, child in self.children.items():
                # print(child.__position, child.__length)
                # print(child)
                start = child.position
                length = child.length
                descent = child.descent
                print(text[start:start+length], start, length)
                child.printTree(text)


def fromSuffixArray(text, suffixArray, lcp):
    tree = PNode(children={}, descent=0)
    
    lastAdded =  None
    for i in range(len(suffixArray)):
        print(i)
        # lastAdded = tree
        # while lastAdded.children != {}:
        #     symbol, lastAdded = list(lastAdded.children.items())[-1]
       
            # print(i)
        currLCP = lcp[i]
        if currLCP == 0:
            position = suffixArray[i]
            symbol = text[position] #not important, just to fill Node object # 
           
            length = len(text[position:])
            descent = length
            parent = tree
                
            newNode = PNode(symbol=symbol, descent=descent, parent=deepcopy(parent), position=position, length=length)

            parent.children[symbol] = deepcopy(newNode)
            
            lastAdded = deepcopy(tree.children[symbol])
            #lastAddedSymbol = symbol

        else:
            currNode = lastAdded

            while currNode.descent > currLCP:
              #  child = deepcopy(currNode)
                currNode = currNode.parent
                

            if currNode.descent == currLCP:
                parent = currNode
                position = suffixArray[i] + lcp[i]
                length = len(text[position:])
                descent = lcp[i] + length
                symbol = text[position]
                newNode = PNode(symbol=symbol, position=position, length=length, parent= deepcopy(parent), children={}, descent=descent)
                
                parent.children[symbol] = deepcopy(newNode)

                # parent.children[child.symbol] = deepcopy(child)`
                lastAdded = parent.children[symbol]
                # lastAddedSymbol = symbol

            else:
                parent = currNode
                symbolRighMost, rightMost = list(parent.children.items())[-1]
                
                del parent.children[symbolRighMost]

                #########
                interSymbol = text[suffixArray[i]]
                
                interNodeLength = suffixArray[i] + lcp[i] - suffixArray[i] - parent.descent
                interNode = PNode(symbol= interSymbol, position=suffixArray[i]+parent.descent, length= interNodeLength, descent= lcp[i], parent=parent, children={})

               
                ##########


                ########################
                rightMost.position = suffixArray[i-1] + lcp[i]
                rightMost.length = rightMost.descent - lcp[i]
                rightMost.parent = interNode
                symbol = text[rightMost.position]
                rightMost.symbol = symbol
                interNode.children[symbol] = deepcopy(rightMost)
                ########################


                #####
                position = suffixArray[i] + lcp[i]
                length = len(text[position:])
                symbol = text[position]
                descent = lcp[i] + length
                newNode = PNode(symbol=symbol, position=position, length=length, descent= descent, parent=interNode, children={})

                interNode.children[symbol] = deepcopy(newNode)
                #####


                parent.children[interSymbol] = deepcopy(interNode)

                lastAdded =  parent.children[interSymbol].children[symbol]
                # lastAddedSymbol = symbol

    root = lastAdded
    while root.parent != None:
        root =  root.parent

    return root


if __name__ == "__main__":
    
    file = open('data/fromSuffixArray.txt', 'r')

    text = file.readline().rstrip('\n')
    suffixArray = ast.literal_eval(file.readline())
    lcp = ast.literal_eval(file.readline())

    tree = fromSuffixArray(text, suffixArray, lcp)

    tree.printTree(text)