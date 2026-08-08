# Last updated: 8/7/2026, 7:20:39 PM
1class Solution:
2    def longestConsecutive(self, nums: list[int]) -> int:
3        longest = 0
4        s = set(nums)
5        for n in s:
6            if (n-1) not in s:
7                length=1
8                while(n+length) in s:
9                    length+=1
10                longest=max(length,longest)
11        return longest
12        