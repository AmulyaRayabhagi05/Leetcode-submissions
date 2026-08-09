# Last updated: 8/8/2026, 9:46:46 PM
1class Solution:
2    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
3        res = [] 
4        #starting, how many cols
5        left, right = 0, len(matrix[0])
6
7        #start, how many rows
8        top,bottom = 0, len(matrix)
9
10        while left < right and top < bottom:
11            # left to right and get every value in i in the top row
12            for i in range(left,right):
13                res.append(matrix[top][i])
14            top+=1
15            #get every i in the right col
16            for i in range(top,bottom):
17                res.append(matrix[i][right-1])
18            right -=1
19            if not (left < right and top < bottom):
20                break
21            # getting bottom row
22            for i in range(right-1, left -1, -1):
23                res.append(matrix[bottom-1][i])
24            bottom -=1
25
26            # get every i in the left most common 
27            for i in range(bottom-1,top-1, -1):
28                res.append(matrix[i][left])
29            left +=1
30        return res