from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        for i in range(len(nums)- 2):
            if i > 0 and nums[i] == nums[i-1]: # to avoid dups 
                continue 
            left, right = i + 1, len(nums)-1
            while left < right: 
                tot = nums[i] + nums[left] + nums[right]
                if tot < 0: 
                    left += 1 
                elif tot > 0: 
                    right -=1
                else: 
                    result.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left +1 ]:
                        left += 1
                    while left < right and nums[right] == nums[right -1]:
                        right -= 1 
                    left += 1
                    right -= 1 
        return result 
    
'''
- sort, then iterate through each element as a potential firt element of the triplet
- use two pointers to find the remaining two elements
- to avoid duplicates, skip the same element if it's already been used as the first element of the triplet

time comp: O(n^2)
space comp: O(n) for the sort 
'''