class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        res = -1
        for i in range(len(s)):
            for j in range(i, len(s)):
                if s[i] == s[j]:
                    distance = j - i - 1
                    res = max(res, distance)
                    
        return res

 