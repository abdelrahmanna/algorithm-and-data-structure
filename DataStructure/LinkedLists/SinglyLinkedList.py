class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
	
 
    def _getNumberOfRemainingNodes(self):
        count = 1
        if self.next is None:
            return count
        
        node = self.next
        while node.next is not None:
            count += 1
            
        return count
    
    def reverseList(self, head):
        current = head
        prev = None
        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        
        
        while prev is not None:
            print(prev.value)
            prev = prev.next

if __name__ == "__main__":
    node = Node(5)
    node.next = Node(-1)
    node.next.next = Node(60)
    node.next.next.next = Node(14)
    node.next.next.next.next = Node(14)
    
    node.reverseList(node)