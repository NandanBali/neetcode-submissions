# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast = head
        slow = fast
        lslow = None
        if head == None or head.next == None:
            return
        while fast != None:
            if fast.next == None:
                break
            fast = fast.next.next
            lslow = slow
            if slow != None:
                slow = slow.next
        
        if fast != None:
            lslow = slow
            if slow != None:
                slow = slow.next

        # lslow is mpt, slow is mpt+1
        a = slow
        b = slow
        if slow != None:
            b = slow.next
        
        t = False
        while b != None:
            n = b.next
            if not t and a != None:
                a.next = None
                t = True
            b.next = a
            a = b
            b = n
        if lslow != None:
            lslow.next = None
        
        x = head

        while a != None and x != None:
            c = x
            b = a
            if c != None:
                c = c.next
            if b != None:
                b = b.next
            x.next = a
            if c != None and b != None:
                a.next = c
            x = c
            a = b
        if fast != None:
            h = head
            while h != None and h.next != None:
                h = h.next
            if h != None:
                h.next = lslow
            