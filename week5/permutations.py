# 6

from typing import List 
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start=0):
            if start == len(nums): # if current permutation is done, add a copy 
                result.append(nums[:])
                return
            for i in range(start, len(nums)):
                nums[start], nums[i] = nums[i], nums[start] #switch the current element with the start element
                # recursion:  build the permutation with the next num
                backtrack(start + 1)
                nums[start], nums[i] = nums[i], nums[start] # backtrack by swapping back

        result = []
        backtrack()
        return result
    
    '''
    If the current permutation is of the same length as the input array, it means a complete permutation is formed and then we add this permutation to the list of perms

    Otherwise, we go through the array and look for the first element that has not been used in the current permutation yet. We then add this element to the current permutation and proceed to add more elements to the permutation via a recursive call. Once we are done searching through the array for the current permutation, we backtrack by removing the last element from the current permutation.
    
    '''