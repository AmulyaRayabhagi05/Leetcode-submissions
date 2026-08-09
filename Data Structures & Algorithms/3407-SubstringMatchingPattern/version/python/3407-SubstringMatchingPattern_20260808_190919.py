# Last updated: 8/8/2026, 7:09:19 PM
1class Solution:
2    def hasMatch(self, s: str, p: str) -> bool:
3        prefix, suffix = p.split("*")
4        
5        # Try all possible starting positions where prefix matches
6        for i in range(len(s) - len(prefix) + 1):
7            # Check if s[i:] starts with prefix
8            if s[i:].startswith(prefix):
9                # Check if suffix appears in the remaining part of s
10                remaining_s = s[i + len(prefix):]
11                if suffix in remaining_s:
12                    return True
13                    
14        return False