# Longest Substring Without Repeating Characters

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char = set()
        maxLength = 0
        start = 0 

        for idx in range(len(s)): 
            while s[idx] in char:
                char.remove(s[start])
                start+=1

            char.add(s[idx])
            maxLength = max(maxLength, idx-start+1)
        return maxLength
    

'''
Time comp: O(N) 
Space comp: O((N, M))
'''