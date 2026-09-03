class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        localmins = []
        n = len(prices)
        if n > 1 and prices[1] - prices[0] > 0:
            localmins.append(0)

        for i in range(n-2):
            if prices[i+2] - prices[i+1] >= 0 and prices[i+1] - prices[i] <= 0:
                localmins.append(i+1)

        out = 0

        for idx in localmins:
            sell = max(prices[idx+1:])
            if out < sell - prices[idx]:
                out = sell - prices[idx]

        return out