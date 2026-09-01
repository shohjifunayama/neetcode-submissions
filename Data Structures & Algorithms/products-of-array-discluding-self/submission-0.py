class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1]*n
        prefix = nums[0]
        suffix = nums[-1]
        for i in range(n-1): 
            ans[i+1] = ans[i+1] * prefix
            ans[-i-2] = ans[-i-2] * suffix
            prefix = prefix * nums[i+1]
            suffix = suffix * nums[-i-2]

        return ans