class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        n = len(s2)
        m = len(s1)
        ans = {}
        con = {}
        
        kind = set(s1) | set(s2)
        for c in kind:
            ans[c] = s1.count(c)
            con[c] = s2[0:m].count(c)
        if con == ans:
                return True

        for l in range(n-m):
            con[s2[l+m]] += 1
            con[s2[l]] -= 1
            if con == ans:
                return True

        return False