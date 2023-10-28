
from typing import List
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        initial_col = image[sr][sc]

        if initial_col == color:
            return image
        
        def boundary(i,j):
            if i<0 or i>=len(image) or j<0 or j>=len(image) or image[i][j]!=initial_col:
                return
            image[i][j] = color 

            # need to adjust be directions now.. up down left right
            boundary(i-1, j) 
            boundary(i+1, j)
            boundary(i, j-1)
            boundary(i, j+1)

        boundary(sr,sc)
        return image 


