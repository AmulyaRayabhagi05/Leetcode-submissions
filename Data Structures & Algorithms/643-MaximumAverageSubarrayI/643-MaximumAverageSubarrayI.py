# Last updated: 8/5/2026, 7:05:32 PM
class Solution:
   #sliding window method
   
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # Compute the sum of the first window of size k
        current_sum = sum(nums[:k])
        max_sum = current_sum
    
         # Slide the window from index k to the end of the array
        for i in range(k, len(nums)):
        # Subtract the element leaving the window (nums[i - k]) 
        # and add the new element entering (nums[i])
         current_sum += nums[i] - nums[i - k]
         max_sum = max(max_sum, current_sum)
    
        # Return the maximum average
        return max_sum / k