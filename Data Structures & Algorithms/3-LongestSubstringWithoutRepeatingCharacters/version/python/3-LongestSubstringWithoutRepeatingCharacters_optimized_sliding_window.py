# Last updated: 8/5/2026, 7:34:34 PM
1class Solution:
2    def lengthOfLongestSubstring(self, s: str) -> int:
3        char_map = {}
4        left, max_len = 0,0
5
6        for right, char in enumerate(s):
7            if char in char_map and char_map[char] >= left:
8                left = char_map[char] + 1
9            char_map[char] = right
10            max_len = max(max_len, right - left + 1)
11        return max_len
12
