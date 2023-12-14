# 79 word search 

from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(board, i, j, word):
            if len(word) == 0:
                return True
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or word[0] != board[i][j]:
                return False
            temp = board[i][j]
            board[i][j] = '#'
            res = dfs(board, i+1, j, word[1:]) or dfs(board, i-1, j, word[1:]) or dfs(board, i, j+1, word[1:]) or dfs(board, i, j-1, word[1:])
            board[i][j] = temp
            return res
        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(board, i, j, word):
                    return True
        return False
    

    '''
    depth-first search (DFS) algorithm
    
    takes a 2D board and a word as input and returns True if the word can be constructed from the letters of sequentially adjacent cells in the board
    
    implement dfs as a nested function 'dfs'. It starts from a cell in the board and explores as far as possible along each branch before backtracking.
    
    The base cases are when the word is found (when the length of the word is 0), or when the search is out of boundary or the current cell does not match the first character of the word.
    
    mark the visited cells with '#' and then explore all four directions (up, down, left, right) around the current cell.
    
    After exploration, backtrack by changing the cell back to its original character.
    
    The function 'exist' iterates over each cell in the board and starts the DFS to check if the word exists in the board.
    '''


# OTHER OPTION TO SOLVE PROLBEM: 

class Solution2: 
    def exist(self, board: List[List[str]], word: str): 
        def dfs(i, j, k): 
            if i<0 or i>=len(board) or j<0 or j>=len(board[0]) or word[k] != board[i][j]: 
                return False
            if k == len(word)-1:
                return True
            tmp = board[i][j] 
            board[i][j] = '/'
            res = dfs(i+1, j, k+1) or dfs(i-1, j, k+1) or dfs(i, j+1, k+1) or dfs(i, j-1, k+1)
            board[i][j] = tmp
            return res
        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0):
                    return True
        return False
    
    '''
    the second method using class Solution2 is a more concise version of the first method using class Solution. 
    
    main difference between the two solutions is how they handle the DFS process
    
    first solution (class Solution), the DFS function takes three parameters: the board, the current position (i, j), and the remaining word to be found. 
    It marks the visited cells with '#', explores all four directions around the current cell, and then backtracks by changing the cell back to its original character.

    second solution (class Solution2), the DFS function also takes three parameters: the current position (i, j) and the current index of the word (k). 
    It marks the visited cells with '/', explores all four directions around the current cell, and then backtracks by changing the cell back to its original character. 
    
    instead of passing the remaining word to the next DFS call, it passes the next index of the word. This makes the code more concise and easier to understand.
    '''