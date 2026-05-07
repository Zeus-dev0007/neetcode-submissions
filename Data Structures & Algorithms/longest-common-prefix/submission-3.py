class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        res = ""
        first = strs[0]
        for i in range(len(first)):
            count = 0
            for j in strs:
                if i < len(j) and first[i] == j[i]:
                    count += 1
            
            if count == len(strs):
                res += first[i]
            else:
                break

        return res
