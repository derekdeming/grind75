from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# using floyds cycle-finding algorithm
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next: 
            return False
        
        s, f = head, head.next

        while s != f: 
            if not f or not f.next:
                return False
            s = s.next
            f = f.next.next
        
        return True
        