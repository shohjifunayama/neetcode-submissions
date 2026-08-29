class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        N = len(nums)
        if N <= 1:
            return False
        for i in range(N-1):
            popped = nums.pop(0)
            if popped in nums:
                return True

        return False
        