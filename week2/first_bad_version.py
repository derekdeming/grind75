# 278
def isBadVersion(version: int) -> bool:
    pass # for the sake of errors -- on leetcode this func is already defined 

class Solution: 
    def firstBadVersion(self, n: int) -> int: 
        left = 1
        right = n
        while left < right: 
            mid = left + (right - left) // 2
            if isBadVersion(mid): 
                right = mid 
            else: 
                left = mid + 1
        return left