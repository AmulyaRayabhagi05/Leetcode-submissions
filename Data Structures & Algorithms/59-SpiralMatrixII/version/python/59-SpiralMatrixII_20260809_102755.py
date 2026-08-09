# Last updated: 8/9/2026, 10:27:55 AM
1class Solution:
2    def generateMatrix(self, n: int) -> List[List[int]]:
3        #left pointer, right pointer, top pointer, bottom pointer
4
5        #square matrix = light and right pointer
6        mat = [[0] * n for i in range(n)]
7        
8        left,right = 0, n-1
9        top, bottom = 0, n-1
10
11        val = 1
12
13        while left <= right:
14            # fill every val in top row
15            for c in range(left,right + 1):
16                mat[top][c]= val
17                val+=1
18            top+=1
19            #fill every val in right col
20            for r in range(top, bottom+1):
21                mat[r][right] = val
22                val+=1
23            right -=1
24            #fill every val in bottom row(reverse order)
25            for c in range(right, left - 1, -1):
26                mat[bottom][c] = val
27                val+=1
28            bottom -=1
29
30            # fill every val in left col ( reverse order)
31            for r in range(bottom,top-1, -1):
32                mat[r][left]=val
33                val+=1
34            left+=1
35        return mat