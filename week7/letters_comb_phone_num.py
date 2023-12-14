from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        phone = {'2': ['a','b','c'],
                '3': ['d','e','f'],
                '4': ['g','h','i'],
                '5': ['j','k','l'],
                '6': ['m','n','o'],
                '7': ['p','q','r','s'],
                '8': ['t','u','v'],
                '9': ['w','x','y','z']}
        res = []
        def backtrack(i, curr):
            if len(curr) == len(digits):
                res.append(curr)
                return
            for letter in phone[digits[i]]:
                backtrack(i+1, curr+letter)
        backtrack(0, '')
        return res
    
# time comp: O(3^N * 4^M) -- N is the number of digits in the input that maps to 3 letters and M is the number of digits in the input that maps to 4 letters

'''
The idea is to generate all possible combinations of letters by using backtracking approach.

create a dict that maps every digit to all its possible letters. 

standard backtracking problem with a twist: need to keep track of the position in the original digits string, so that we can add the correct letter to the final answer
'''