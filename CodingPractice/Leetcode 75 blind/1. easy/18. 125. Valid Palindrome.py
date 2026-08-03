# 125. Valid Palindrome

# "https://leetcode.com/problems/valid-palindrome/"
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s= s.lower()

        l , r = 0, len(s)-1
        while l < r:
            while l < r and not self.is_alphanum(s[l]):
                l += 1
            while l < r and not self.is_alphanum(s[r]):
                r -= 1
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True

    def is_alphanum(self, c):
        return (
        ord("a") <= ord(c) <= ord("z") or 
        ord("A") <= ord(c) <= ord("Z") or 
        ord("0") <= ord(c) <= ord("9") 
        )

        