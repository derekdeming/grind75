# 39

from typing import List
class Solution: 
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(start, combination, curr_sum): 
            if curr_sum == target:
                result.append(combination.copy())
                return 
            elif curr_sum > target: 
                return 
            for i in range(start, len(candidates)):
                combination.append(candidates[i])
                backtrack(i, combination, curr_sum + candidates[i])
                combination.pop()

        result = []
        backtrack(0, [], 0)
        return result 
    

    '''
    find all unique combinations of nums that sum to the target value. each num can be used multiple times in the combination 

    use backtracking (recursive algo to find all solutions by checking all potential candidates and removing those that fail condition)

    
    
    '''