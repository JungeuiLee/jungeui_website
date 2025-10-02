from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = []
        for i in range(numRows):
            row = [1] * (i + 1)
            for floor in range(1, i):
                row[floor] = ans[i - 1][floor - 1] + ans[i - 1][floor]
            ans.append(row)
        return ans

        # for floor in range(1, numRows):
        #     if ans[i][i] == (ans[floor - 1][0]):

test = Solution()
print(test.generate(numRows=5))
print(test.generate(numRows=1))