# Last updated: 8/9/2026, 1:06:17 PM
1class Solution:
2    def threeSumMulti(self, arr: List[int], target: int) -> int:
3        count=0
4        MOD = 10**9 + 7
5        for i in range(len(arr)):
6            freq=Counter()
7            for j in range(i+1,len(arr)):
8                count+=freq[target-arr[i]-arr[j]]
9                freq[arr[j]]+=1
10
11        return count%MOD
12
13
14