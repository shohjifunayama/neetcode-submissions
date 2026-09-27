class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l = 0
        r = n
        j = n + 3
        while l < r:
            i = (l + r) // 2
            if nums[i] == target:
                return i
            elif nums[i] > target:
                r = i
            elif nums[i] < target:
                l = i

            if j == i:
                break
            j = i
        return -1