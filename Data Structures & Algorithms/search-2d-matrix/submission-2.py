class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        header = [row[0] for row in matrix]

        n = len(header)
        l = 0
        r = n-1

        while l <= r:
            i = l + (r - l) // 2

            if header[i] == target:
                return True
            elif header[i] > target:
                r = i-1
            elif header[i] < target:
                l = i+1
        while header[i] > target and i > 0:
            i -= 1
        
        col = matrix[i][:]
        n = len(col)
        l = 0
        r = n-1

        while l <= r:
            i = l + (r - l) // 2

            if col[i] == target:
                return True
            elif col[i] > target:
                r = i-1
            elif col[i] < target:
                l = i+1

        return False
