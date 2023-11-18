class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        i, n = 0, len(intervals)

        # 1
        while i < n and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1

        # 2
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
            i += 1

        result.append(newInterval)

        # 3
        while i < n:
            result.append(intervals[i])
            i += 1

        return result

'''1. finding the Insert Position: We iterate over intervals, adding intervals to the result that end before newInterval starts. make sure that the result remains sorted

2. merging Intervals: If we find intervals that overlap with newInterval (they start before newInterval ends), merge them with newInterval. This merging updates newInterval to be the union of itself and the other overlapping intervals.

3. add Remaining Intervals:  add the rest of the intervals to the result after newInterval has been placed and merged

time com: O(N) -- # of intervals for each interval is processes once
space comp: O(N) -- output list and input isn't modified 
'''
