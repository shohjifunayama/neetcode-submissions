class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        n = len(nums)
        ans = []

        for i in range(1,n-1):
            s = -nums[i]
            l = 0
            r = n-1
            while l < i and i < r:
                m = nums[l] + nums[r]
                if s == m:
                    if [nums[l], -s, nums[r]] not in ans:
                        ans.append([nums[l], -s, nums[r]])
                    
                if s >= m:
                    l += 1
                if s <= m:
                    r -= 1


            
            

        return ans
            
