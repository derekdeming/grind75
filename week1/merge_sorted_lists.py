# Definition for singly-linked list.

from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        temp = ListNode(-1)
        current = temp 
        
        while list1 is not None and list2 is not None: 
            if list1.val < list2.val: 
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        
        if list1 is not None:
            current.next = list1
        if list2 is not None: 
            current.next = list2
        return temp.next   

# Time Complexity: O(n + m) where n is the length of list1 and m is the length of list2
sorted_lists = Solution
list1 = ListNode(1, ListNode(2, ListNode(4)))
list2 = ListNode(1, ListNode(3, ListNode(4)))
print(sorted_lists.mergeTwoLists(sorted_lists, list1, list2))