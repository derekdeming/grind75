# 84 largest rectangle in histogram

from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        return self.helper(heights, 0, len(heights) - 1)
    
    def helper(self, heights: List[int], start: int, end: int) -> int:
        if start > end:
            return 0
        if start == end:
            return heights[start]
        
        min_idx = self.find_min(heights, start, end)
        left = self.helper(heights, start, min_idx - 1)
        right = self.helper(heights, min_idx + 1, end)
        
        return max(left, right, heights[min_idx] * (end - start + 1))
    
    def find_min(self, heights: List[int], start: int, end: int) -> int:
        min_idx = start
        for i in range(start, end + 1):
            if heights[i] < heights[min_idx]:
                min_idx = i
        return min_idx
    
'''
main func: recursive process to call helper w/ entire range of histogram 

helper func: recursive func that takes in the histogram, start index, and end index. If start > end, return 0. If start == end, return the height at start. Find the index of the minimum height in the range and recursively call helper on the left and right subranges. Return the max of the left, right, and the area of the minimum height.
'''