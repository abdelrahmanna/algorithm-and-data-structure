class Node:
    def __init__(self, value=None):
        self.children = []
        self.value = value
        self.endOfTheWord = False

    def find(self, value):
        for c in self.children:
            if c.value == value:
                return c
        return None 

class Trie:
    def __init__(self):
        self.root = Node()
    
    def add(self, value):
        node = self.root
        
        for i in value:
            children = node.children
            foundElement = False
            for ch in children:
                if i == ch.value:
                    foundElement = True
                    node = ch
                    break
            
            if not foundElement:
                temp = Node(i)
                node.children.append(temp)
                node = temp
        node.endOfTheWord = True

def replaceWords(dictionary, sentence):
    """
    :type dictionary: List[str]
    :type sentence: str
    :rtype: str
    """
    tri = Trie()
    for w in dictionary:
        tri.add(w)
    

    node = tri.root
    isEndOfWord = False
    output = ""
    i = 0
    while i < len(sentence):
        node = node.find(sentence[i])
        
        if not node:
            node = tri.root
            while i < len(sentence) and sentence[i] != " " :
                output += sentence[i]
                i += 1
            output += " "
            i += 1
            continue
            
        isEndOfWord = node.endOfTheWord
        if (not isEndOfWord):
            output += sentence[i]
        else:
            output += sentence[i]
            output += " "
            node = tri.root
            while i < len(sentence) and sentence[i] != " ": i += 1
        i += 1

    return output
