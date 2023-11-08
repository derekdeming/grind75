# 252 

from typing import List
class Solution: 
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool: 
        intervals.sort(key= lambda x: x[0])
        ending = []
        for interval in intervals:
            if ending and interval[0] < ending[0]:
                return False
            ending.append(interval[1])
        return True
    
'''
sort the intervals, use the min heap to keep track of the ending of the meetings

the heap ensures that that earliest endings are at the top 

iterate though, check for an overlap -- if the current intervals start time is less than the earliest ending (at the top of the heap), it means theres an overlap

if no overlap, put current intervals ending to heap
'''