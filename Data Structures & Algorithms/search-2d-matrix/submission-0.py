class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix)
        while l < r:
            m = l + (r - l) // 2
            if matrix[m][0] >= target:
                r = m
            else:
                l = m + 1
        if l < len(matrix) and matrix[l][0] == target:
            return True
        if l == 0:
            return False
        row = l - 1
        l, r = 0, len(matrix[row]) - 1
        while l <= r:
            m = l + (r - l) // 2
            if matrix[row][m] == target:
                return True
            elif matrix[row][m] < target:
                l = m + 1
            else:
                r = m - 1
        return False