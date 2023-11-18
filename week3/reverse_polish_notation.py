from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # using last in first out approach for reverse polish notation (ex: 3-4+5 --> 3 4- 5+)

        stacks = []
        for token in tokens: 
            if token in "+-*/":  # Corrected operators
                b, a = stacks.pop(), stacks.pop()
                if token == '+':
                    stacks.append(a + b)
                elif token == '-':
                    stacks.append(a - b)
                elif token == '*':
                    stacks.append(a * b)
                elif token == '/':
                    stacks.append(int(a / b)) #needed to add int for the truncation to zero
            else: 
                stacks.append(int(token))  # used to convert numeric strings to integers
        return stacks.pop()

'''
-check for the specific operator 
-then pop the last two numbers
-perform the operation
-push the result back to the stack
-return the last element in the stack

time comp: O(N)
space comp: O(N)
'''