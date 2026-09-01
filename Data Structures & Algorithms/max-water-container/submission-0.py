class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)

        l = 0
        r = n - 1
        height = 0
        maxh = 0

        while l < r:
            hl = heights[l]
            hr = heights[r]
            height = min(hl, hr) * (r - l)
            maxh = max(height, maxh)

            if hl <= hr:
                while heights[l] <= hl and l < r:
                    l += 1
            elif hl >= hr:
                while heights[r] <= hr and l < r:
                    r -= 1
        
        return maxh