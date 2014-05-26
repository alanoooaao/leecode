# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
        if l1 == None and l2 == None:
            return None
        elif l1 == None and l2 != None:
            l1 = ListNode(0)
        elif l2 == None and l1 != None:
            l2 = ListNode(0)
        
        result = ListNode(0)
        result.val = l1.val + l2.val
        if result.val >= 10:
            result.val = result.val % 10
            if l1.next == None:
                l1.next = ListNode(1)
            else:
                l1.next.val += 1
        
        result.next = self.addTwoNumbers(l1.next, l2.next)
        return result