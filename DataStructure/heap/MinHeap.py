class MinHeap:
    def __init__(self) -> None:
        self.heap = []
    
    
    
    def getParentIndex(self, index):
        return (index - 1) // 2
    
    def getLeftChild(self, index):
        return 2 * index - 1
    
    def getLeftChild(self, index):
        return 2 * index + 1
    
    def getRightChild(self, index):
        return 2 * index + 2
    
    def swap(self, ind1, ind2):
        temp = self.heap[ind1]
        self.heap[ind1] = self.heap[ind2]
        self.heap[ind2] = temp
        
    def add(self, value):
        index = len(self.heap)
        self.heap.append(value)
        parentIndex = self.getParentIndex(index)    
        while index > 0 and self.heap[index] < self.heap[parentIndex]:
            self.swap(index, parentIndex)
    
    
if __name__ == "__main__":
    heap = MinHeap()
    
    heap.add(6)
    heap.add(4)
    heap.add(2)
    heap.add(50)
    print(heap.heap)