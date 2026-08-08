# Last updated: 8/8/2026, 3:09:23 PM
1class Solution:
2    def canReorderDoubled(self, arr: List[int]) -> bool:
3        counts = Counter(arr)
4        sortedKey = sorted(counts.keys(), key =abs)
5        # gives array length as even 
6        for val in sortedKey:
7            if counts[val] == 0:
8                continue
9            target = 2*val
10            if counts[target] < counts[val]:
11                return False
12            counts[target] -= counts[val]
13            counts[val] =0
14        return True