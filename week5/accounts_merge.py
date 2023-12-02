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
Create an empty dictionary called email_to_name to store the mapping of email addresses to names.
Iterate over each account in the accounts list.
Extract the name from the first element of the account and assign it to the name variable.
For each email address in the account (excluding the name), do the following:
Add the email address as a key in the email_graph dictionary and initialize it with an empty list if it doesn't exist.
Append the current email address to the list of values for the corresponding account[1] key in the email_graph dictionary.
Add the email address and its corresponding name to the email_to_name dictionary.
Define a depth-first search (DFS) function called dfs that takes an email address and a list of emails as parameters.
Inside the dfs function, check if the current email address has not been visited before.
If the email address is not in the visited set, add it to the set and append it to the emails list.
Recursively call the dfs function for each email address in the email_graph dictionary that is connected to the current email address.
Create an empty set called visited to keep track of the explored email addresses
'''