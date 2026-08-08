# Last updated: 8/7/2026, 7:47:42 PM
1class Solution:
2    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
3        sums_ab = defaultdict(int)
4        total_tuples = 0
5        
6        # Step 1: Store all (a + b) sums in the map
7        for a in nums1:
8            for b in nums2:
9                sums_ab[a + b] += 1
10                
11        # Step 2: Check for matching -(c + d) in the map
12        for c in nums3:
13            for d in nums4:
14                target = -(c + d)
15                total_tuples += sums_ab[target]
16                
17        return total_tuples