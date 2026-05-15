class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            left_sum = right_sum = 0

            for l in range(i):
                left_sum += nums[l]

            for r in range(i + 1, n):
                right_sum += nums[r]

            if left_sum == right_sum:
                return i

        return -1

