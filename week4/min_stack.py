# 155 

class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        # if empty then the curr min is the value itself
        current_min = val if not self.stack else min(val, self.stack[-1][1])
        # psh the value and curr min as a pair
        self.stack.append((val, current_min))

    def pop(self) -> None:
        # top element popped from stack
        self.stack.pop()

    def top(self) -> int:
        # return the first element of the top pair (the last value pushed)
        return self.stack[-1][0]

    def getMin(self) -> int:
        # return second element of the top pair (the current minimum)
        return self.stack[-1][1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
