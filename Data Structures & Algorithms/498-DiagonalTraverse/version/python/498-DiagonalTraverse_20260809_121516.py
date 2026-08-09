# Last updated: 8/9/2026, 12:15:16 PM
1class Solution:
2    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
3        if not matrix or not matrix[0]:
4            return []
5
6        m, n = len(matrix), len(matrix[0])
7        result = []
8        row = col = 0
9
10        for _ in range(m * n):
11            result.append(matrix[row][col])
12
13            if (row + col) % 2 == 0:
14                if col == n - 1:
15                    row += 1
16                elif row == 0:
17                    col += 1
18                else:
19                    row -= 1
20                    col += 1
21            else:
22                if row == m - 1:
23                    col += 1
24                elif col == 0:
25                    row += 1
26                else:
27                    row += 1
28                    col -= 1
29
30        return result