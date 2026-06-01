# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        iter = head
        ln = None
        while iter != None:
            ln = ListNode(val=iter.val, next=ln)
            iter = iter.next
        return ln