
from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)  # dp[i] means s[:i+1] can be segmented into words in the wordDicts 
        dp[0] = True
        for i in range(len(s)):
            if dp[i]:
                for j in range(i + 1, len(s) + 1):
                    if s[i:j] in wordDict:
                        dp[j] = True
        return dp[-1]
        

'''
algo uses a dp approach to solve the problem. 

iterate over the string s. 

For each index i, check all substrings s[i:j] where j is from i+1 to len(s) 

If any of these substrings is in the dict, set dp[j] to True

this is so that the substring s[:j+1] can be segmented into words from the dictionary

'''