class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        arr = set()
        for i in nums:
            if i in arr:
                arr.remove(i)

            else:
                arr.add(i)

        return len(arr) == 0