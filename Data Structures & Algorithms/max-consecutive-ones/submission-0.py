class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res, count = 0, 0
        for i in nums:
            if i == 1:
                count += 1
            else:
                if count > res:
                    res = count
                count = 0
        return max(res, count)