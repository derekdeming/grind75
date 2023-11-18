from typing import List

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        if not mat:
            return []
        rows, cols = len(mat), len(mat[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        queue = []
        dist = [[float('inf')] * cols for _ in range(rows)]

        # get the zeros of matrix
        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    dist[r][c] = 0
                    queue.append((r, c))

        # bfs from each zero
        while queue:
            r, c = queue.pop(0)
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and dist[nr][nc] > dist[r][c] + 1:
                    dist[nr][nc] = dist[r][c] + 1
                    queue.append((nr, nc))
        return dist
'''

using breadth first search for queue and dequeue and checking neighbors 

Time comp: O(m * n) where m and n are the dimens. of the the matrix. Issues with list.pop(0) so prob added cost here 
Space comp: O(m * n) for the queue and the dist matrix
'''