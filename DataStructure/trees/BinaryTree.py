import queue
class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.value)
    
    def add(self, node, value):
        if node.value > value:
            if node.left is None:
                node.left = Node(value)
                return
            self.add(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
                return
            self.add(node.right, value)

    def print(self, node):
        if node.left is not None:
            self.print(node.left)
        print(node.value)
        if node.right is not None:
            self.print(node.right)

    def toArray(self, node):
        res = []
        if node.left is not None:
            res = res + self.toArray(node.left)
        res.append(node.value)
        if node.right is not None:
            res = res + self.toArray(node.right)

        return res
    
    def find(self, node, value):
        if node is None:
            return -1

        if node.value > value:
           return self.find(node.left, value)
        elif node.value < value :
            return self.find(node.right, value)
        elif node.value == value:
            return node
        
    def breadthFisrtSearch(self):
        _queue = queue.Queue()
        _queue.put(self)
        # print(_queue.empty())
        while not _queue.empty():
            node = _queue.get()
            print(node.value)
            if (node.left):
                _queue.put(node.left)
            if (node.right):
                _queue.put(node.right)
        
             
    # def isValidBtree(self):
    #     if self.left is None and self.right is None:
    #         return True
    #     validBtree = True
    #     if self.right is not None:
    #         if self.value >= self.right.value:
    #             return False
    #         validBtree = validBtree and self.right.isValidBtree()
    #     if self.left is not None:
    #         if self.value <= self.left.value:
    #             return False
    #         validBtree = validBtree and self.left.isValidBtree()
        
    #     return "Yes" if validBtree  else "No"
    
class BinaryTree:
    def __init__(self, root: int) -> None:
        self.root = Node(root)

    def add(self, value: int):
        self.root.add(self.root, value)

    def print(self):
        self.root.print(self.root)

    def toArray(self):
        return self.root.toArray(self.root)
    
    def find(self, value):
        return self.root.find(self.root, value)
    
    def breadthFisrtSearch(self):
        return self.root.breadthFisrtSearch()
    

if __name__ == "__main__":
    btree = BinaryTree(21)

    btree.add(10)

    btree.add(50)

    btree.add(3)

    btree.print()

    print(btree.toArray())
    # print(btree.find(5))
    # print(btree.find(21))
    # print(btree.find(3))
    
    btree.add(5)
    # btree.print()
    # print(btree.find(5))
    
    # print("-----------------------------")
    btree.add(4)
    btree.add(65)
    # btree.print()
    print("bread")
    print(btree.toArray())
    btree.breadthFisrtSearch()   
    
    # node = Node(26) 
    # node.left = Node(28)
    # node.left.left = Node(1)
    # node.right = Node(35)
    
    # print(node.isValidBtree())
    
    # @todo compare 2 trees