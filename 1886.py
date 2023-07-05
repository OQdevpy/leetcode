url = "https://leetcode.com/problems/determine-whether-matrix-can-be-obtained-by-rotation/"
from typing import List
class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        return next((1 for _ in range(4) if target==self.rotate(mat)), 0)

    
    def rotate(self, matrix: List[List[int]]):
        n = len(matrix)
        for i in range(n // 2 ):
            matrix[i], matrix[n - i - 1] = matrix[n - i - 1], matrix[i]
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i]= matrix[j][i], matrix[i][j]
        return matrix