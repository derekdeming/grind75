# 8: String to Integer (atoi)
from typing import List

class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip() # remove leading and trailing whitespace
        if not s: # if str is empty
            return 0
        sign = 1
        i = 0
        if s[0] == '-':
            sign = -1
            i += 1
        elif s[0] == '+':
            i += 1
        res = 0
        while i < len(s) and s[i].isdigit():
            res = res * 10 + int(s[i])
            i += 1
        return max(-2**31, min(sign * res, 2**31 - 1))
'''
we can use linear scan approach is a method where we iterate through the data in a linear fashion, starting from the first item in a set and moving sequentially through the rest of the items 

ex: num 123 -- we need to build the integer: 
res = 0
res = res * 10 + 1
res = res * 10 + 2
res = res * 10 + 3
res = 123

crux: res = res * 10 + int(s[i]) -- used to shift the currently built number one decimal place to the left and add the new digit, thereby constructing the integer representation of the string one digit at a time

'''
