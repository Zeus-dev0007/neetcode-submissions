class Solution:
    def largestGoodInteger(self, num: str) -> str:
        res = ""
        i , j = 0, 2
        while j < len(num):
            if num[i] == num[i+1] and num[i] == num[j]:
                res = max(res, num[i] + num[i+1] + num[j])
            i += 1
            j += 1

        return res
        