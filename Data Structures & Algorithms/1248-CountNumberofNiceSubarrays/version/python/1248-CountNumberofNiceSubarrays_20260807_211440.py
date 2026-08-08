# Last updated: 8/7/2026, 9:14:40 PM
1class Solution:
2    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
3        
4        res = 0 
5        odd = 0
6        l,m = 0,0
7
8        for r in range(len(nums)):
9            if nums[r] %2:
10                odd +=1
11
12            if odd > k:
13                l = m+1
14                m = l
15                odd -= 1
16            if odd ==k:
17                while not nums[m]%2:
18                    m +=1 
19                res += (m-l) + 1
20        return res