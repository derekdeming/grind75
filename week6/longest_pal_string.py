# 5: Longest Palindromic Substring

class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                # expand outwards from the center
                left -= 1
                right += 1
            return left + 1, right - 1
        start, end = 0, 0
        for i in range(len(s)):
            left1, right1 = expand(i, i) # odd case
            left2, right2 = expand(i, i + 1)# even case
            # get the max length
            if right1 - left1 > end - start:
                start, end = left1, right1
            if right2 - left2 > end - start:
                start, end = left2, right2
        return s[start:end + 1]
'''
there is a linear time solution: Manacher's algorithm (example down below)

expand function is used to expand outwards from the center of the string to find the longest palindrome

the for loop is used to iterate through the string and expand outwards from the center of the string to find the longest palindrome

the left and right pointers are used to keep track of the current position in the string





Manachers algorithm:

0(n) time complexity and 0(n) space complexity. It uses a clever algorithm to reduce the time complexity from O(n^2) to O(n). However, it is not a very intuitive algorithm and i have NOOOO idea how to implement it so i asked chatgpt: 

class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Preprocess the string to insert '#'
        T = '#'.join('^{}$'.format(s))
        
        n = len(T)
        P = [0] * n
        C = R = 0
        
        for i in range(1, n - 1):
            P[i] = (R > i) and min(R - i, P[2 * C - i])  # equals to min(remaining mirror length, already known palindrome length)
            # Attempt to expand palindrome centered at i
            while T[i + P[i] + 1] == T[i - P[i] - 1]:
                P[i] += 1

            # If palindrome centered at i expands past R, adjust the center C and right boundary R
            if i + P[i] > R:
                C, R = i, i + P[i]

        # Find the maximum element in P
        maxLen, centerIndex = max((n, i) for i, n in enumerate(P))
        return s[(centerIndex - maxLen)//2: (centerIndex + maxLen)//2]

'''
