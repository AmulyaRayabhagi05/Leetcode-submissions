# Last updated: 8/5/2026, 6:49:41 PM
1class Solution:
2   #sliding window method
3   
4    def findMaxAverage(self, nums: List[int], k: int) -> float:
5        # Compute the sum of the first window of size k
6        current_sum = sum(nums[:k])
7        max_sum = current_sum
8    
9         # Slide the window from index k to the end of the array
10        for i in range(k, len(nums)):
11        # Subtract the element leaving the window (nums[i - k]) 
12        # and add the new element entering (nums[i])
13         current_sum += nums[i] - nums[i - k]
14         max_sum = max(max_sum, current_sum)
15    
16        # Return the maximum average
17        return max_sum / k
