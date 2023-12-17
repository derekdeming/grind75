# 76 

from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""
        dict_t = Counter(t)
        req = len(dict_t) # num of unique chars in t needed for window 
        l, r = 0, 0
        formed = 0
        window_counts = {} # dict to keep track of all unique chars in the current window
        ans = float("inf"), None, None # (window length, left, right)
        while r < len(s):
            character = s[r]
            window_counts[character] = window_counts.get(character, 0) + 1 # add char to window 
            if character in dict_t and window_counts[character] == dict_t[character]:
                formed += 1

            while l <= r and formed == req: # contract the window from the left
                character = s[l]
                if r - l + 1 < ans[0]:
                    ans = (r - l + 1, l, r)

                # char at the position pointed by the left pointer is removed from the window
                window_counts[character] -= 1
                if character in dict_t and window_counts[character] < dict_t[character]:
                    formed -= 1
                l += 1    

            r += 1 # expand the window from the right 
        return "" if ans[0] == float("inf") else s[ans[1]:ans[2] + 1]



"""
find the min window in s which will contain all the characters in t

create dict_t where the keys = unique chars in t & values = counts of those chars in t

req = num of unique chars in t that need to be included in the window

use left and right pointers for the sliding window

dict window_counts keeps track of all unique char in the current window.

tuple used to store the length of the smallest window and its left and right indices. initialized with infinity for the length and None for the indices.

outer while loop moves the right pointer r across the string s. If the current char exists in dict_t and its count equals the count in dict_t, formed is incremented by 1 

the inner while loop contracts the window from the left by moving the left pointer l to the right. If the window size is smaller than the current smallest window size, ans is updated. If the character being removed from the window exists in dict_t and its count in the window is less than the count in dict_t, formed is decremented.

return the smallest window found. If no such window is found, it returns an empty string.
"""

