from typing import List

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # calc the squared euclid dist.
        def distance(point):
            x, y = point
            return x**2 + y**2
        # sort the points by dist. from origin
        points.sort(key=distance)
        return points[:k]

'''
use the squared distance to avoid computing the square root (not necessary for this) 
sorting in place using distance 

time comp: O(NlogN) where N is the length of points 
space comp: O(1) w/ sort done in place 
'''