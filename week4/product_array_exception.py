# 238

from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1] * n 

        # calc left and right products
        lp = 1
        for i in range(n):
            result[i] = lp
            lp *= nums[i]

        rp = 1
        for i in range(n - 1, -1, -1):
            result[i] *= rp
            rp *= nums[i]

        return result
