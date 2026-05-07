class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]

        for i in range(numRows - 1):
            prev_row = res[-1]
            temp = [0] + prev_row + [0]

            new_row = []

            for j in range(len(temp) - 1):
                new_row.append(temp[j] + temp[j + 1])

            res.append(new_row)
        return res