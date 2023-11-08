# 217

from typing import List
from collections import Counter

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        freq_cnts = Counter(nums)
        return any(count > 1 for count in freq_cnts.values())

        # distinct_set = set()
        # for num in nums: 
        #     if num in distinct_set: 
        #         return True
        #     distinct_set.add(num)
        # return False
        
'''
count occurrences of elements in nums 

if not in set, we add it 
'''