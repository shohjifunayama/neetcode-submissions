class TimeMap:

    def __init__(self):
        from collections import defaultdict
        self.timelines = defaultdict(list)
        self.values = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timelines[key].append(timestamp)
        self.values[key].append(value)

    def get(self, key: str, timestamp: int) -> str:
        nums = self.timelines[key]

        if (not nums) or nums[0] > timestamp:
            return ""
        else:
            # 探索
            l = 0
            r = len(nums) - 1
            
            while l < r:
                m = (r + l + 1) // 2
                if nums[m] <= timestamp:
                    l = m
                else: 
                    r = m-1

            # nums[l] <= timestamp < nums[l+1] にしたい
            return self.values[key][l]



