class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        N = len(nums)
        for i in range(N):
            popped = nums.pop(0)
            if popped in nums:
                return True

        return False
        