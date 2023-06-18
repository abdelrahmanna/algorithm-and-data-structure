class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
	
 
    def _getNumberOfRemainingNodes(self):
        count = 1
        if self.next is None:
            return count
        
        node = self.next
        while node.next is not None:
            count += 1
            node = node.next
            
        return count

def getIntersectionNode(head1, head2):
    c1 = head1._getNumberOfRemainingNodes()
    c2 = head2._getNumberOfRemainingNodes()
    
    if (c1 > c2):
        d = c1 - c2
        for _ in range(d):
            head1 = head1.next
    else:
        d = c2 - c1
        for _ in range(d):
            head2 = head2.next
            
    while head1 is not None and head2 is not None:
        if (head1 is head2):
            return head1.data
        
        
        head1 = head1.next
        head2 = head2.next
    
    return -1




if __name__ == '__main__':
    
    intersection = Node(30)
    
    head1 = Node(1)
    head1.next = intersection
    head1.next.next = Node(3)
    head1.next.next.next = Node(4)
    head1.next.next.next.next = Node(13)
    
    head2 =  Node(5)
    head2.next =  Node(20)
    head2.next.next = intersection
    
    results = getIntersectionNode(head1, head2)
    
    print(results)