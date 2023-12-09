# 54: The Spiral Matrix Problem

from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix: # empty matrix
            return []
        res = []
        rowBegin = 0
        rowEnd = len(matrix) - 1
        colBegin = 0
        colEnd = len(matrix[0]) - 1

        while rowBegin <= rowEnd and colBegin <= colEnd:
            for i in range(colBegin, colEnd + 1): # right traversal
                res.append(matrix[rowBegin][i])
            rowBegin += 1

            for i in range(rowBegin, rowEnd + 1): # down traversal
                res.append(matrix[i][colEnd])
            colEnd -= 1

            if rowBegin <= rowEnd: # left traversal
                for i in range(colEnd, colBegin - 1, -1):
                    res.append(matrix[rowEnd][i])
                rowEnd -= 1

            if colBegin <= colEnd: # up traversal
                for i in range(rowEnd, rowBegin - 1, -1):
                    res.append(matrix[i][colBegin])
                colBegin += 1
        return res

'''
basically iterate over the matrix in 4 directions: right, down, left, and up, while adjusting the boundaries after each dir

sets the initial boundaries for matrix

while Loop conditions: rowBegin is less than or equal to rowEnd and colBegin is less than or equal to colEnd (used so that we dont go outside of the matrix) 

right: from left to right along the top row and adds those elements to res. After traversing, it increments rowBegin since the top row has been fully processed.

down: it then moves down along the rightmost column and adds those elements to res. After traversing, it decrements colEnd

left: Before traversing left, it checks if rowBegin is still less than or equal to rowEnd to ensure it's not processing a row that's already been traversed. Then it traverses from right to left along the bottom row. After traversing, it decrements rowEnd.

up: it checks if colBegin is still less than or equal to colEnd before traversing up along the leftmost column. Then it increments colBegin.


time complexity of O(N) - for traversing only once
space complexity of O(N) - storing the entire matrix ( i think)

'''