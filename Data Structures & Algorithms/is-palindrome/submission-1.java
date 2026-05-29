class Solution {
    public boolean isPalindrome(String s) {
        // 1. Initialize pointers using the string's length
        int left = 0;
        int right = s.length() - 1;
        
        // 2. Loop until the pointers meet in the middle
        while (left < right) {
            
            // Skip non-alphanumeric characters from the left
            while (left < right && !Character.isLetterOrDigit(s.charAt(left))) {
                left++;
            }
            
            // Skip non-alphanumeric characters from the right
            while (left < right && !Character.isLetterOrDigit(s.charAt(right))) {
                right--;
            }
            
            // 3. Convert both valid characters to lowercase and compare them
            if (Character.toLowerCase(s.charAt(left)) != Character.toLowerCase(s.charAt(right))) {
                return false; // Not a palindrome!
            }
            
            // 4. Step both pointers inward
            left++;
            right--;
        }
        
        return true;
    }
}