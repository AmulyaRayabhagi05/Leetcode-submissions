# Last updated: 8/7/2026, 7:41:45 PM
1class Solution:
2    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
3        sums, res = defaultdict(int), 0
4
5        for x in nums1:
6            for y in nums2:
7                sums[x + y] += 1
8                
9        for i in nums3:
10            for j in nums4:
11                res += sums[0 - (i + j)]
12                
13        return res