# 155 

class MinStack:

    def __init__(self):
        # Initialize an empty stack
        self.stack = []

    def push(self, val: int) -> None:
        # If the stack is empty, the current minimum is the value itself
        current_min = val if not self.stack else min(val, self.stack[-1][1])
        # Push the value and current minimum as a pair
        self.stack.append((val, current_min))

    def pop(self) -> None:
        # Pop the top element from the stack
        self.stack.pop()

    def top(self) -> int:
        # Return the first element of the top pair (the last value pushed)
        return self.stack[-1][0]

    def getMin(self) -> int:
        # Return the second element of the top pair (the current minimum)
        return self.stack[-1][1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
