# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        a = l1
        b = l2
        res = ListNode()
        x = res
        c = 0
        while a or b:
            s = c
            if a:
                s += a.val
                a = a.next
            if b:
                s += b.val
                b = b.next
            if s > 9:
                c = 1
                s -= 10
            else:
                c = 0
            res.next = ListNode(s)
            res = res.next
        
        if c >= 1:
            res.next = ListNode(c)
        
        return x.next
