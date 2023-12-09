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
expand function is used to expand outwards from the center of the string to find the longest palindrome

the for loop is used to iterate through the string and expand outwards from the center of the string to find the longest palindrome

the left and right pointers are used to keep track of the current position in the string



'''
