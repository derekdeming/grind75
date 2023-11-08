# 409 

class Solution: 
    def longestPalindrome(self, s: str) -> int: 
        char_cnt = {}
        for char in s:
            char_cnt[char] = char_cnt.get(char,0) + 1 # storing freq of char in str 
        longest_palindrome = 0
        odd_char_cnt = 0 
        
        for count in char_cnt.values():
            if count % 2 == 0:
                longest_palindrome += count
            else:
                longest_palindrome += count - 1
                odd_char_cnt = 1
        
        if odd_char_cnt > 0:
            longest_palindrome += min(odd_char_cnt, 1)
        return longest_palindrome

'''
iterating over dict for char counts 
if count is even, add to longest palindrome
if count is odd, include at most one occurrence of char in palind
add extra length from odd occurrences (minimum of two or one depending on whether there are more than one odd chars)
'''