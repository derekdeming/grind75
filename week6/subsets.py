# 78: Subsets

from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start, path): 
            res.append(path)
            for i in range(start, len(nums)):
                backtrack(i + 1, path + [nums[i]])
        res = []
        backtrack(0, [])
        return res
        

'''
backtracking is an algorithm for finding all solutions by exploring all potential candidates. If the solution candidate turns to be not a solution (or at least not the last one), backtracking algorithm discards it by making some changes on the previous step, i.e. backtracks and then try again. (thanks github copilot for the definition lol)

backtracking is a form of recursion. But it involves choosing only option out of any possibilities. We begin by choosing an option and backtrack from it, if we reach a state where we conclude that this specific option does not give the required solution. We repeat these steps by going across each available option until we get the desired solution. (thanks geeksforgeeks for the definition lol -- really copilot)

initialize an empty res array for storing the subsets

call backtrack function with 2 parameters: start index and path
    - start index: used to keep track of the current index in nums
    - path: used to keep track of the current subset

append the current subset to res

iterate over the nums array from start to the end
    - call backtrack with i + 1 as the start index and path + [nums[i]] as the current subset
return res



'''