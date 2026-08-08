# Last updated: 8/8/2026, 3:33:49 PM
1class Solution:
2    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
3        ROWS, COLS = len(matrix), len(matrix[0])
4
5        top, bot = 0, ROWS-1
6
7        while top <= bot:
8            row = (top+bot) //2
9            if target > matrix[row][-1]:
10                top = row + 1
11            elif target < matrix[row][0]:
12                bot = row - 1
13            else: 
14                break
15        row  = (top+bot) // 2
16        l,r = 0,COLS-1
17        while l <=r:
18            m = (l+r) // 2
19            if target > matrix[row][m]:
20                l = m +1
21            elif target < matrix[row][m]:
22                r = m-1
23            else:
24                return True
25        return False
26        
27