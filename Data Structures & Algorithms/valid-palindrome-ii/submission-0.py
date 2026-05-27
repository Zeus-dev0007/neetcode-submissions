class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s == s[::-1]:
            return True
        res = ""
        for i in range(len(s)):
            res = s[0:i] + s[i+1:]
            if res == res[::-1]:
                return True

        return False


