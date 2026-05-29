class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        isDupli = False
        # Loop by index using range()
        for i in range(len(nums)-1):
                if nums[i] == nums[i+1]:
                    isDupli = True
                    return isDupli
                    
        return isDupli