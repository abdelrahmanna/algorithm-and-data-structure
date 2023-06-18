class Node:
    def __init__(self,key, value):
        self.value = value
        self.key = key
        self.next=None
        self.prev = None
        
    def __str__(self):
        startNode = self
        while startNode.prev is not None:
            startNode = startNode.prev

        output = ""
        while startNode is not None:
            output += startNode.key + ", " + startNode.value, "--->"

        
        return output


class Lru:
    def __init__(self,lenth) -> None:
        self.lenth = lenth
        self.elCount = 0
        self.leastUsed = None
        self.recent = None
        self.memory = dict()
        
    def add(self, key, value) -> None:
        newNode = Node(key, value)
        if (self.leastUsed is None):
            self.recent = newNode
            self.leastUsed = self.recent
            self.memory[key] = self.recent
            return
    
        if (self.lenth == len(self.memory)):
            # delete from memory
            del self.memory[self.leastUsed.key]
            self.leastUsed = self.leastUsed.next
            self.leastUsed.prev = None

        
        self.recent.next = newNode
        newNode.prev = self.recent
        self.recent = self.recent.next
        self.memory[key] = self.recent
        if len(self.memory) == 2:
            self.leastUsed.next = self.recent
        
    def __str__(self):
        startNode = self.leastUsed

        output = ""
        while startNode is not None:
            output +="("+ str(startNode.key) + ", " + str(startNode.value)+ ")" + "--->" 
            startNode = startNode.next

        
        return output
    def get(self, key):
        node = self.memory[key]
        
        if (self.recent.key == node.key):
            return node.value
                    
        # remove the node from it's place
        if (node.prev is not None):
            node.prev.next = node.next
            
        if (node.next is not None):
            node.next.prev = node.prev

        if (self.leastUsed.key == key):
            self.leastUsed = node.next
            
        # add the node to the top of the queue
        node.next = None
        self.recent.next = node
        node.prev = self.recent
        self.recent = self.recent.next

        return node.value
        
if __name__ == '__main__':
    lru = Lru(3)
    
    lru.add(1, "test")
    print(str(lru))
    
    lru.add(2, "test521")
    print(str(lru))
    
    lru.add(3, "testfasd")
    print(str(lru))
    
    lru.add(4, "testfasd")
    print(str(lru))
    
    lru.get(2)
    print(str(lru))
    
    lru.add(5, "testfasd")
    print(str(lru))
    
    lru.get(5)
    print(str(lru))
    
    lru.get(2)
    print(str(lru))

    lru.get(4)
    print(str(lru))