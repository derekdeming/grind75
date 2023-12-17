# 438 

from typing import List

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # use sliding window approach
        p_count = {}
        s_count = {}
        for c in p:
            p_count[c] = p_count.get(c, 0) + 1
        res = []
        for i in range(len(s)):
            s_count[s[i]] = s_count.get(s[i], 0) + 1
            if i >= len(p):
                if s_count[s[i - len(p)]] == 1:
                    del s_count[s[i - len(p)]]
                else:
                    s_count[s[i - len(p)]] -= 1
            if s_count == p_count:
                res.append(i - len(p) + 1)
        return res
    
    
    '''
    prob could use Counter class from collections module
    
    algorithm is used to find all the start indices of p's anagrams in s. 

    use sliding window approach to compare the count of characters in p and the current window of s
    
    if the count matches, it means the curr window is an anagram of p, and we append the start index of the window to the result
    
    we use two dictionaries to store the count of characters in p and the current window of s. 
    
    iterates over s, and for each character, it increases the count in s_count 
    
    If the window size is larger than the length of p, it decreases the count of the character at the start of the window in s_count

    If the count becomes 0, it removes the character from s_count

    Then it compares s_count with p_count. If they are the same, it means the current window is an anagram of p, and it appends the start index of the window to the result
    
    
    '''