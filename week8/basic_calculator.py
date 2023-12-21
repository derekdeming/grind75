# 224. Basic Calculator

class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        op = 0
        res = 0
        sign = 1

        for ch in s:
            if ch.isdigit():
                op = op * 10 + int(ch)
            elif ch == "+":
                res += sign * op
                sign = 1
                op = 0
            elif ch == "-":
                res += sign * op
                sign = -1
                op = 0
            elif ch == "(": # push the result first, then sign
                stack.append(res)
                stack.append(sign)
                sign = 1
                res = 0
            elif ch == ")":
                res += sign * op
                res *= stack.pop() # stack pop should give the sign before the parenthesis
                res += stack.pop() # this one should give the result calculated before the parenthesis
                op = 0

        return res + sign * op


'''
white spaces: Ignore them as they do not affect the calculation

digits: since numbers can be more than one digit long, accumulate the value until you encounter a non-digit character

operators (+ and -): its how the following number should be added to the result

parentheses: When you encounter an opening parenthesis (, push the current result and the last sign onto a stack and reset them for evaluating the expression inside the parentheses. When encountering a closing parenthesis ), pop the last sign and result from the stack and use them to update the current result

stack: used to store results and signs corresponding to each opened parenthesis.
'''