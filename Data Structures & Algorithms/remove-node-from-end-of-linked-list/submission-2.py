# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        a, b = head, head
        for _ in range(0, n):   
            if b:
                b = b.next
        ap = None
        if not b and head:
            return head.next
        while b:
            if a:
                ap = a
                a = a.next
            b = b.next
        if ap and a:
            ap.next = a.next
        return head