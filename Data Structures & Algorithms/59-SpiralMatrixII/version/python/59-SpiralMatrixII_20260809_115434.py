# Last updated: 8/9/2026, 11:54:34 AM
1class Solution:
2    def rotate(self, matrix: List[List[int]]) -> None:
3        """
4        Do not return anything, modify matrix in-place instead.
5        """
6
7        for row in range(len(matrix)):
8            for col in range(row,len(matrix)):
9                temp = matrix[row][col]
10                matrix[row][col] = matrix[col][row]
11                matrix[col][row] = temp
12
13        #reverse
14        for row in matrix:
15            row.reverse()
16
17