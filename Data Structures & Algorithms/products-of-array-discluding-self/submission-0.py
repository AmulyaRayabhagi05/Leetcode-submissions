class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n  # This space is required for the output, so it's O(1) extra space.
        
        # Loop 1: O(N) Time
        left_val = 1
        for i in range(n):
            res[i] = left_val
            left_val *= nums[i]
            
        # Loop 2: O(N) Time
        right_val = 1
        for i in range(n - 1, -1, -1):
            res[i] *= right_val
            right_val *= nums[i]
            
        return res