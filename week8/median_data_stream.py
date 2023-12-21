#  295

import heapq

class MedianFinder:

    def __init__(self):
        self.heaps = [], []

    def addNum(self, num: int) -> None:
        small, large = self.heaps
        heapq.heappush(small, -heapq.heappushpop(large, num))
        if len(large) < len(small):
            heapq.heappush(large, -heapq.heappop(small))
        
    def findMedian(self) -> float:
        small, large = self.heaps
        if len(large) > len(small):
            return float(large[0])
        return (large[0] - small[0]) / 2.0
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

'''
using two heaps: max heap to store the smaller half of the input numbers, min heap to store the larger half of the input numbers

the max-heap allows us to access the largest eleemnt among the smallest half quickly and the min-heap allows us to access the smallest element among the largest half quickly

addNum adds a number to the data structure. It always pushes the number to large first. If large becomes larger than small, it pops the smallest number from large and pushes it to small. The two heaps will be balanced since we ensure that small is no larger than large

findMedian returns the median of all elements in the data structure. If the number of elements is odd, it returns the top element of large. If the number of elements is even, it returns the average of the top element of large and the top element of small
'''