class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sset = set(s)
        tset = set(t)

        if sset != tset:
            return False
        
        for char in sset:
            if s.count(char) != t.count(char):
                return False
        return True