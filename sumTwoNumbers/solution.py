class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def addTwoNumbers(self, l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    output =  ListNode()
    nextNode = output
    remainder = 0
    while l1 or l2 or remainder:
        # sums
        if l1 and l2:
            nextNode.val = l1.val + l2.val + remainder
            l2 = l2.next
            l1 = l1.next
            if l1 or l2:
                nextNode.next = ListNode()
        elif l1:
            nextNode.val = l1.val + remainder
            l1 = l1.next
            if l1:
                nextNode.next = ListNode()
        elif l2:
            nextNode.val = l2.val +  remainder
            l2 = l2.next
        else:
            nextNode.next = ListNode(remainder)
            
        if l1 or l2 or remainder:
            nextNode.next = ListNode()
            
        if nextNode.val >= 10:
            nextNode.val -= 10
            remainder = 1
        else:
            remainder = 0
        nextNode = nextNode.next
    
    return output