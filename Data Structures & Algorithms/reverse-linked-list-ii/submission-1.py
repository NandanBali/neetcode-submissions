# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        a = head
        l = None
        for _ in range(1, left):
            if a:
                l = a
                a = a.next
        b = a
        for _ in range(left, right):
            if b:
                b = b.next
        prev = None
        curr = a
        while prev != b and curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        if a:
            a.next = curr
        if l:
            l.next = b
            return head
        else:
            return b
