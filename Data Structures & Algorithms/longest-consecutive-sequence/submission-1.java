class Solution {
    public int longestConsecutive(int[] nums) {
        // Step 1: Dump all numbers into a HashSet for O(1) lookups
        Set<Integer> numSet = new HashSet<>();
        for (int n : nums) {
            numSet.add(n);
        }

        int longest = 0;

        // Step 2: Iterate through the array to find sequence starters
        for (int n : nums) {
            // Check if 'n' is the absolute start of a sequence
            if (!numSet.contains(n - 1)) {
                int length = 0;
                
                // Count how far the consecutive sequence goes
                while (numSet.contains(n + length)) {
                    length++;
                }
                
                // Keep track of the maximum length found so far
                longest = Math.max(length, longest);
            }
        }

        return longest;
    }
}