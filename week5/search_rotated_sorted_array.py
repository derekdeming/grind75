# 33
from typing import List

class Solution: 
    def search(self, nums: List[int], target:int) -> int: 
        if not nums: 
            return -1
        l = 0
        r = len(nums) - 1
        while l <= r: 
            mid = (l + r) // 2
            if nums[mid] == target: 
                return mid
            if nums[l] <= nums[mid]: #check if on left side is sorted
                if nums[l] <= target <= nums[mid]: #check if target is on left side 
                    r = mid - 1
                else: 
                    l = mid + 1
            else: 
                if nums[mid] <= target <= nums[r]: 
                    l = mid + 1
                else: 
                    r = mid - 1
        return -1

'''
determine which part of the array (rotated vs not) the target is and then do binary search 

'''