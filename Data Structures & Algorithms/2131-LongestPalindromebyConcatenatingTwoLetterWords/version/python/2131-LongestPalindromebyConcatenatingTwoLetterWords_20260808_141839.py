# Last updated: 8/8/2026, 2:18:39 PM
1class Solution:
2    def longestPalindrome(self, words: List[str]) -> int:
3        counts = Counter(words)
4        length = 0
5        hasCenter = False
6
7        seen = set()
8
9        for word, count in counts.items():
10            if word in seen:
11                continue
12            revWord = word[::-1]
13
14            if revWord == word:
15                length += (count // 2) * 4 
16                if count % 2 == 1:
17                    hasCenter = True
18            else: 
19                if revWord in counts:
20                    length += min(count, counts[revWord]) *4
21                    seen.add(revWord)
22            seen.add(word)
23
24        if hasCenter:
25            length += 2
26        return length 
27