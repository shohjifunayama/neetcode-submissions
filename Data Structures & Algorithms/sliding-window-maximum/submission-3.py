class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = sorted(nums, reverse=True)

        d = defaultdict(list)
        n = len(nums)

        for i in range(n):
            d[nums[i]].append(i)
        
        res = [float('inf')] * (n - k + 1)

        for que in queue:
            for idx in d[que]:
                for i in range(-k+1, 1):
                    if 0 <= i + idx < n - k + 1 and res[i + idx] == float('inf'):
                        res[i + idx] = que

            if float('inf') not in res:
                return res 
        return res