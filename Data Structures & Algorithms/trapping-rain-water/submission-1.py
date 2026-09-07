class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n == 1 or n == 2:
            return 0 
        lmax = 0
        rmax = 0
        ls = [0] * n
        rs = [0] * n

        for i in range(n):
            if lmax < height[i]:
                lmax = height[i]
            if rmax < height[n-1-i]:
                rmax = height[n-1-i]
            ls[i] = lmax
            rs[n-i-1] = rmax

        res = 0
        for i in range(n):
            res += max(min(ls[i], rs[i]) - height[i], 0)

        return res