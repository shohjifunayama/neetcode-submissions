class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        l, r = 0, 0
        out = 0
        d = dict.fromkeys(set(s), 0)
        d[s[0]] += 1
        while True:
            if r - l + 1 - max(list(d.values())) <= k :
                out = max(out, r - l + 1)
                r += 1
                if r < n:
                    d[s[r]] += 1
                else:
                    return out
            else:
                d[s[l]] -= 1
                l += 1