# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow_node = head 
        fast_node = head 
        
        while fast_node is not None and fast_node.next is not None:
            slow_node = slow_node.next  
            fast_node = fast_node.next.next 
        return slow_node
    
    
        
# basically same as last week with the tortoise and the haire 
# initialize and then have 1 step vs 2 steps 