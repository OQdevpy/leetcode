from typing import List
url = "https://leetcode.com/problems/rotate-image/"
matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]



class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        for i in range(n // 2 ):
            matrix[i], matrix[n - i - 1] = matrix[n - i - 1], matrix[i]
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i]= matrix[j][i], matrix[i][j]
        return matrix



a = Solution()
print(a.rotate(matrix))
