from typing import List
from collections import defaultdict

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m, n = len(mat), len(mat[0])
        max = m + n
        d = {}

        for i in range(m):
            for j in range(n):
                if i + j not in d:
                    d[i+j] = [mat[i][j]]
                else:
                    d[i+j].append(mat[i][j])
        print(d)

        ans = []
        for k in d.items():
            if k[0] % 2 == 0:
                [ans.append(x) for x in k[1][::-1]]
            else:
                [ans.append(x) for x in k[1]]
        return ans


test = Solution()
print(test.findDiagonalOrder(mat = [[1,2,3],[4,5,6],[7,8,9]]))
print(test.findDiagonalOrder(mat = [[1,2],[3,4]]))