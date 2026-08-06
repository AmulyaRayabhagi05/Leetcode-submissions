# Last updated: 8/5/2026, 7:18:12 PM
1class Solution:
2    def lengthOfLongestSubstring(self, s: str) -> int:
3        char_set = set()
4        left = 0
5        max_length = 0
6        # Expand the window using the right pointer
7        for right in range(len(s)):
8        # If the character is already in the set, shrink window from the left
9            while s[right] in char_set:
10                char_set.remove(s[left])
11                left += 1
12        # Add the current character to the set and update max_length
13            char_set.add(s[right])
14            max_length = max(max_length, right - left + 1)
15        return max_length
