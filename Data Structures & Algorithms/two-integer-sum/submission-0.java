class Solution {
    public int[] twoSum(int[] nums, int target) {
        int[] pair = new int[2];
        for(int i=0; i<nums.length-1;i++){
            for(int j=nums.length-1; j>i; j--){
                if(nums[i]+nums[j] == target){
                    pair[0] = i;
                    pair[1] = j;
                }
            }
        }
        return pair;
    }
}
