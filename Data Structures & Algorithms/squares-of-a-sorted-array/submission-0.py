class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        res = []
        for i in nums:
            res.append(i*i)
        for j in range(len(nums)):
            nums[j] = res[j]

        nums.sort()
        return nums