class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l, r = (0, n-1)
        rot = n
        while r > l and nums[l] > nums[r]:
            m = (l + r)//2 

            if nums[m] >= nums[l]:
                l = m + 1
                rot = l
            else: 
                r = m
                rot = m

            if nums[l] < nums[r]:
                rot = l
                break
        
        if target >= nums[0]:
            l, r = (0, rot - 1)
        elif target <= nums[-1]:
            l,r = (rot, n-1)
        else:
            return -1

        while r > l:
            m = (l + r)//2
            if nums[m] == target:
                return m
            elif nums[m] > target:
                r = m - 1
            else:
                l = m + 1

        return l if l < n and nums[l] == target else -1
            
        