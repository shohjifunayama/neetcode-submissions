class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        n = len(s)
        maxl = 0
        while r < n:
            if s[r] in s[l:r]:
                l += 1
            else: 
                maxl = max(maxl, r - l + 1)
                r += 1
                
        return maxl
