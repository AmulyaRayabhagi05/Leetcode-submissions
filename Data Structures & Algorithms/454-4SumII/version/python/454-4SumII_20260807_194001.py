# Last updated: 8/7/2026, 7:40:01 PM
1class Solution:
2    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
3        
4        return c if not (n:=collections.Counter([n1+n2 for n1 in nums1 for n2 in nums2])) or (c:=0) or [(c:= c+n[-(n3+n4)]) for n3 in nums3 for n4 in nums4 if -(n3+n4) in n] else 0