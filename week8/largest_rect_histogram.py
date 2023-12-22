# 84 largest rectangle in histogram

from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        for i in range(len(heights)):
            while stack and heights[stack[-1]] > heights[i]:
                height = heights[stack.pop()]
                width = i - stack[-1] - 1 if stack else i
                max_area = max(max_area, height * width)
            stack.append(i)
        
        while stack:
            height = heights[stack.pop()]
            width = len(heights) - stack[-1] - 1 if stack else len(heights)
            max_area = max(max_area, height * width)
        
        return max_area
    
'''

revised; stack solution -- track the potential start of each rectangle. when a shorter bar is encountered, pop the stack and calculate the area of the rectangle.

use stack to track the indices of bars which are the potential start positions of rect. the stack ensures that the heights of the bars are in non-decreasing order 

handle shorter bar: when shorter bar is found, it indicates the end of a potential rectangle. we then repeatedly pop the stack and calculate the area of rectangle formed between the current element and the bar at the top of the stack. keep track of the max area.

height of the rect is determined by the height of the ppopped bar. width is determined by the current index of the bar we are processing and the bar at the top of the stack (for empty stack, it is the current index). If it is not empty, the current index - the index of the bar at the top of the stack - 1

update max area: after calculating the area, update the max area if necessary

processing remaining bars in stack: after processing all the bars in the histogram, check the stack. if not empty, repeat the above step for the remaining bars.if the stack is empty the width is the total length of histogram

'''



# this solution below is not accepted bc it exceeds time limit

class Solution2:
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