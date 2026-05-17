class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        i = 0
        j = 1
        pairs = len(nums) - 1
        count = 0

        if len(nums) == 1:
            return True

        else:
            while j != len(nums):
                if nums[i] % 2 == 0 and nums[j] % 2 != 0:
                    count += 1

                elif nums[j] % 2 == 0 and nums[i] % 2 != 0:
                    count += 1

                i += 1
                j += 1

        if count == pairs:
            return True

        return False
