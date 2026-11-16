class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        import math

        l, r = (1, max(piles))

        while r > l:
            k = (l + r)//2
            spend = 0
            for p in piles:
                spend += math.ceil(p/k)
            
            if spend <= h:
                r = k
            else:
                l = k + 1
            
        return r
