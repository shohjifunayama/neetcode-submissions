class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        m = max(piles)

        bot = 1
        top = m
        res = float('inf')

        while bot <= top:
            k = bot + (top - bot) // 2 
            s = 0
            for p in piles:
                s += (p - 1) // k + 1

            if s > h:
                bot = k + 1
            else:
                res = min(res, k)
                top = k - 1
        
        return res
        