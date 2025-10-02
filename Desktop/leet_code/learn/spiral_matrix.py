from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        max = m + n
        # d = {}
        # for i in range(m):
        #     for j in range(n):
        #         if i + j not in d:
        #             d[i+j] = [matrix[i][j]]
        #         else:
        #             d[i+j].append(matrix[i][j])
        # print(d)

        ans = []
        top = 0
        bottom = m-1
        left = 0
        right = n-1
        while top <= bottom and left <= right:
            #right
            for i in range(left, right + 1):
                ans.append(matrix[top][i])
            top += 1
            #down
            for i in range(top, bottom + 1):
                ans.append(matrix[i][right])
            right -= 1
            #left
            if top <= bottom:
                for i in range(right, left - 1, -1):
                    ans.append(matrix[bottom][i])
                bottom -= 1
            #up
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    ans.append(matrix[i][left])
                left += 1
        return ans


test = Solution()
print(test.spiralOrder(matrix = [[1,2,3],[4,5,6],[7,8,9]]))
print(test.spiralOrder(matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]])) 