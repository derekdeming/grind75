#  42 

from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        l_max, r_max = 0, 0
        res = 0
        while l < r:
            if height[l] < height[r]:
                if height[l] >= l_max:
                    l_max = height[l]
                else:
                    res += l_max - height[l]
                l += 1
            else:
                if height[r] >= r_max:
                    r_max = height[r]
                else:
                    res += r_max - height[r]
                r -= 1
        return res
    
'''
use two pointers to scan the array from both sides

the water level at a specific index is determined by the minimum of the max heights of the left and right sides

if the water level at the current index is lower than the water level at the other side, then the water level at the current index is determined by the max height of the left side

'''