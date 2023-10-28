class Solution:
    def isValid(self, s: str) -> bool:
        x = []
        brackets = {')': '(', '}': '{', ']': '['}
        
        for char in s: 
            if char in brackets:
                top = x.pop() if x else '_'
                if brackets[char] != top:
                    return False 
            else: 
                x.append(char)
        return not x 
    
parentheses = Solution()
print(parentheses.isValid("()[]{}"))