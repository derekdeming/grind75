# 23. Merge k Sorted Lists

from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]
        
        mid = len(lists) // 2
        left = self.mergeKLists(lists[:mid])
        right = self.mergeKLists(lists[mid:])
        
        return self.merge(left, right)
    
    def merge(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1:
            return l2
        if not l2:
            return l1
        
        if l1.val < l2.val:
            l1.next = self.merge(l1.next, l2)
            return l1
        else:
            l2.next = self.merge(l1, l2.next)
            return l2
    

'''
main func: takes in a list of linked lists and recursively divides them into smaller sublists until each sublist contains only one element and then merge sublists together w/ merge func

merge func: takes in two linked lists and merges them together in sorted order. Compares the values of the nodes in l1 and l2 and recursively merges the remaining nodes in l1 and l2. Returns the merged list.

Time complexity: O(nlogk) where n is the total number of nodes in all lists and k is the number of lists. The merge function takes O(n) time and the mergeKLists function takes O(logk) time.
'''
