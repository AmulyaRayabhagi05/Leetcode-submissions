class Solution:
   #Brute Force method
   
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_sum = float('-inf')
        n = len(nums)
         # Iterate through every starting position for a subarray of length k
        for i in range(n - k + 1):
            current_sum = 0
            # Calculate the sum of the current subarray of length k
            for j in range(i, i + k):
             current_sum += nums[j] 
             # Track the maximum sum found
            max_sum = max(max_sum, current_sum)
        # Divide the largest sum by k to get the maximum average
        return max_sum / k
