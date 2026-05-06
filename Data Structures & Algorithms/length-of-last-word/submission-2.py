class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        res = 0
        i = len(s) - 1
        while s[i] == " ":
            i -= 1
        while s[i] != " " and i >= 0:
            i -= 1
            res += 1
        return res

