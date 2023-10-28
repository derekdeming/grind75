class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered_str = ''.join([char for char in s.lower() if char.isalnum()])
        
        return filtered_str==filtered_str[::-1]
    
palindrome = Solution()
print(palindrome.isPalindrome("A man, a plan, a canal: Panama"))
