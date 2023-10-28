from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_hash = {}
        for idx, num in enumerate(nums):
            comp = target - num 
            if comp in num_hash: 
                return [num_hash[comp], idx]
            num_hash[num] = idx 
            
sums = Solution()
print(sums.twoSum([2,7,11,15], 9))
print(sums.twoSum([3,2,4], 6))

        