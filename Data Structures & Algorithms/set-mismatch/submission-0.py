class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        dup = 0
        miss = 0
        count = Counter(nums)
        for i in range(1, len(nums) + 1):
            if count[i] == 2:
                dup += i
            elif count[i] == 0:
                miss += i

        return [dup, miss]

        

