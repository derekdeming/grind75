# 721

from collections import defaultdict
from typing import List

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # Building the graph
        email_graph = defaultdict(list)
        email_to_name = {}
        for account in accounts:
            name = account[0]
            for email in account[1:]:
                email_graph[account[1]].append(email)
                email_graph[email].append(account[1])
                email_to_name[email] = name

        # DFS to find connected components
        def dfs(email, emails):
            if email not in visited:
                visited.add(email)
                emails.append(email)
                for next_email in email_graph[email]:
                    dfs(next_email, emails)

        # Visited set to keep track of explored emails
        visited = set()
        merged_accounts = []
        for email in email_graph:
            if email not in visited:
                emails = []
                dfs(email, emails)
                merged_accounts.append([email_to_name[email]] + sorted(emails))

        return merged_accounts

'''
build the graph and then dfs to find connected things 

union find 
'''