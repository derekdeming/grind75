# 207 
from typing import List
class Solution: 
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool: 
        # use depth first search as algo
        # use dict to store graph 
        g = {i: [] for i in range(numCourses)}
        for course, prereq in prerequisites: 
            g[course].append(prereq)

        # track which nodes we have seen 
        seen = set()

        # use recursion function for seen nodes 
        def dfs(course, path): 
            if course in path:
                return False # this will detect the cycle 
            if course in seen: 
                return True # we won't cycle through this node 
            path.add(course)
            for prereq in g[course]: 
                if not dfs(prereq, path):
                    return False
            path.remove(course)
            seen.add(course)
            return True 
    
        # iterate through all the nodes
        for course in list(g):
            if not dfs(course, set()):
                return False
        return True
    
    '''
    courses are nodes and prereqs are directed edges between nodes

    keys = courses
    values = prereqs for each course  

    using DFS on graphs to detect cycles and check if its possible to finish coursees 

    DFS: check if course in path, if it is it means a cycle is detected and if not, it means it is not. Then check if current course is in set. 
    
    '''