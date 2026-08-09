# Last updated: 8/9/2026, 12:24:32 PM
1class Solution:
2    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
3        # checking if something on the right is bigger:
4
5        #stack is monotonic decreasing
6
7        res = [0]*len(temperatures)
8        stack = [] # pair of values so index always enumerate temp and index
9
10        for i,t in enumerate (temperatures):
11            while stack and t >stack[-1][0]:
12                stackT, stackInd = stack.pop()
13                res[stackInd] = i - stackInd
14            stack.append([t,i])
15        return res
16
17