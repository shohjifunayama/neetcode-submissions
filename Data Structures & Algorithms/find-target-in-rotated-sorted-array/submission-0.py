class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        r = len(nums)-1
        l = 0

        while l < r:
            n = (r-l+1)//2 # 左側のブロックの長さ
            # 1. 2個に分けた先頭を比較

            l_st_r = nums[l] < nums[l+n] 

            # 2. target がどっちに入りうるか確認
            if l_st_r:
                can_t_in_l = nums[l] <= target <= nums[l+n-1]
            else:
                can_t_in_l = not (nums[l+n] <= target <= nums[r])

            # 3. l, r を更新
            if can_t_in_l:
                r = l + n - 1
            else:
                l = l + n
        
        if nums[l] == target:
            return l
        else:
            return -1


