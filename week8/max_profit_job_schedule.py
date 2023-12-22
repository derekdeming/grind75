#1235 max profit in job schedule

from typing import List
import bisect

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(zip(startTime, endTime, profit), key=lambda x: x[1])
        dp = [[0, 0]]
        for s, e, p in jobs:
            i = bisect.bisect(dp, [s + 1]) - 1
            if dp[i][1] + p > dp[-1][1]:
                dp.append([e, dp[i][1] + p])
        return dp[-1][1]
    
'''

use DP for this prob 

sort jobs by end time -- organize the jobs by end times. Zip lists together and sort by end times so that all potential previous jobs have been already considered 

dp table -- tracking max profit achievable by the end of each job. The first element of the dp table is [0, 0] which indicates that the max profit at the end of the first job is 0. The second element of the dp table is [e, p] where e is the end time of the first job and p is the profit of the first job

process jobs in sorted order -- iterate through the jobs in sorted order. Use bisect to do binary search to find the index of the first job that ends after the start time of the current job 

index i is found by bisect.bisect(dp, [s + 1]) - 1 points to the job that ends right before the current job's start time.


algo essentially iterates through the jobs in ascending order of their end times and keeps track of the max profit that can be obtained at each time interval. By considering the previous jobs that end before the current job's start time, it determines whether including the current job in the schedule would result in a higher profit. DP + binary search approach allows for efficient computation of the max profit by avoiding silly repeated calcs
'''