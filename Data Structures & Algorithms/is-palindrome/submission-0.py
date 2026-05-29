class Solution:
    def isPalindrome(self, s: str) -> bool:
        cc = [char.lower() for char in s if char.isalnum()]
        s = "".join(cc)
        return( s==s[::-1] )