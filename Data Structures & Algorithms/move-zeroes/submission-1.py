class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        temp = []
        for i in nums:
            if i != 0:
                temp.append(i)

        for j in range(len(nums)):
            if j < len(temp):
                nums[j] = temp[j]
            else:
                nums[j] = 0