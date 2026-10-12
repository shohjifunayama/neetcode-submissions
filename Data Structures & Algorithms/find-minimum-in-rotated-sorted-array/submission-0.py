class Solution:
    def findMin(self, nums: List[int]) -> int:

        while True:
            n = len(nums)
        # 2つにわける
            r = n - 1
            l = (n - 1) // 2

        #  それぞれの最後尾を比較, 小さい方に注目
            is_l_st_r = nums[l] < nums[r]
            tail = l if is_l_st_r else r

        # 小さい方の1個前がそいつより大きかったら、最小はそれ
            if tail == 0 or nums[tail - 1] > nums[tail]:
                return nums[tail] 

        # 違ったら（気合い）
            nums = nums[0:l+1] if is_l_st_r else nums[l+1:r+1]