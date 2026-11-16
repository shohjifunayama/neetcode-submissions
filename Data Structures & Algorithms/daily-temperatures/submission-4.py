class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        stack = []
        res = [0 for i in temperatures]

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                idx = stack.pop()[1]
                res[idx] = i - idx

            stack.append([t, i])

        return res