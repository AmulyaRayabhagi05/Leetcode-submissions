# Last updated: 8/8/2026, 11:24:13 AM
1class Solution:
2    def numPairsDivisibleBy60(self, time: list[int]) -> int:
3        songD = defaultdict(int)
4        count = 0
5
6        for val in time:
7            remainder = val % 60
8            target = (60 - remainder) % 60
9            
10            # Add matching pairs found so far
11            count += songD[target]
12            
13            # Record current remainder in hash map
14            songD[remainder] += 1
15            
16        return count
17        # create a hashmap
18        # create a counter
19        #loop through the values and keep adding it to the 
20        # we'll check if the new value can be added would that give us something that is divisble by 60 if yes up the counter variable if no add it to the hashmap