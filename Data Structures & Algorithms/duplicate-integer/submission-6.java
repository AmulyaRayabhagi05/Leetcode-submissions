class Solution {
    public boolean hasDuplicate(int[] nums) {
        boolean isDuplicate = false;
        for(int i=0; i<nums.length-1; i++){
            for(int j=i; j<nums.length-1; j++){
            if(nums[i]== nums[j+1]){
                isDuplicate = true;
                return isDuplicate;
            }
        }
        }

        return isDuplicate;
    }
}