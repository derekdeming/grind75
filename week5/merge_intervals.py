# 56

from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        intervals.sort(key=lambda x: x[0]) #sort based on start time 

        merged = [intervals[0]]
        for i in range(1, len(intervals)):
            if intervals[i][0] <= merged[-1][1]: # if current interval overlaps with the last interval in merged, then we merge them
                merged[-1][1] = max(merged[-1][1], intervals[i][1])
            else:
                merged.append(intervals[i]) # just add the current interval to merged otherwise 
        
        return merged
    

'''

Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals

sort the intervals by start time

initialize merged list with the first interval
'''