# 416. Partition Equal Subset Sum
from typing import List
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1: 
            return False
        target = total // 2 # target sum for each subset is half total sum 
        dp = [False] * (target + 1)
        dp[0] = True # dp[0] is set to True because a sum of 0 is always possible
        for num in nums:
            for i in range(target, num - 1, -1):
                dp[i] = dp[i] or dp[i - num]
        return dp[-1] 
    
'''
algo uses a dp approach to solve the problem and is optimized for space 

first compute total sum of all numbers in the array

if the total sum is odd (== 1), return False because we cant divide an odd sum into two equal integer sums

if the total sum is even, we can divide it into two equal integer sums

dp[i] lets us know the subset that sums up to i 

dp[0] is set to True because a sum of 0 is always possible

iterate over the array of numbers in reverse 

main trouble: dp[i] = dp[i] or dp[i - num] (checks and updates the subsets that sum up to i)

1. this will check if dp[i] is True, if it is, then dp[i] will remain True
2. if dp[i - num] is true it means that there is a subset that sums up to i - num. if we add the curr num to this subset, we will get a subset that sums up to i which makes it true? 

'''