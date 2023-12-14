# 621  

from typing import List
from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_counts = list(Counter(tasks).values())
        max_task = max(task_counts)
        num_max_t = task_counts.count(max_task)
        return max(len(tasks), (max_task - 1) * (n + 1) + num_max_t)
    
    '''
    use greedy algo -- greedy always makes the choice that seems to be the best at that moment. This means that it makes a locally-optimal choice in the hope that this choice will lead to a globally-optimal solution.
    
    in this problem, the greedy algorithm schedules the most frequent tasks as often as possible, with the constraint that no two identical tasks occur within n interval
    
    count occurences of each task
    find the max frequency of a task (max_task)
    find the number of tasks that have the max frequency (num_max_t)
    compute the max number of intervals
    
    
    the max num of intervals is calculated as the max between the length of the tasks and the expression "(max_task - 1) * (n + 1) + num_max_t".
    
    the expression "(max_task - 1) * (n + 1) + num_max_t" ==== the max num of intervals considering the most frequent task and the constraint that no two identical tasks occur within n interval.

    '''