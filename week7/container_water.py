# 11

from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height)-1 # left and right pointers
        m_area = 0 
        while l < r:
            m_area = max(m_area, min(height[l], height[r]) * (r - l))
            if height[l] < height[r]:
                l += 1
            else: 
                r -= 1
        return m_area

# time comp: O(n) -- linear scan

'''
the intuition behind this approach is that the area formed between the lines will always be limited by the height of the shorter line

further, the farther the lines, the more will be the area obtained

use a two-pointer technique with l at the beginning and r at the end of the array

While the left pointer is less than the right:
    - calculate the max area between l & r and update the max area if the calculated area is greater
    - It then checks which pointer is pointing to the shorter line. The pointer pointing to the shorter line is moved one step towards the other end.

The reason behind moving the pointer of the shorter line is that the area is always limited by the height of the shorter line and moving the pointer of the taller line wouldn't help.

The process is repeated until the two pointers meet.

'''