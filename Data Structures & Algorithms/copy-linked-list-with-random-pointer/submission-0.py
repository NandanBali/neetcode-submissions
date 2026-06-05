"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        d: Dict[Node, Node] = {}
        it = head
        while it:
            d[it] = Node(it.val)
            it = it.next
        
        it = head
        while it:
            if it.next:
                d[it].next = d[it.next]
            if it.random:
                d[it].random = d[it.random]
            it = it.next
        if head:
            return d[head]
        else:
            return None