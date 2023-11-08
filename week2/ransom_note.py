from collections import Counter

class Solution: 
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # 383. Ransom Note
        # Given two stings ransomNote and magazine, return true if ransomNote can be constructed from magazine and false otherwise.
        counter = Counter(magazine)
        for c in ransomNote:
            if counter[c] <= 0:
                return False
            counter[c] -= 1
        return True