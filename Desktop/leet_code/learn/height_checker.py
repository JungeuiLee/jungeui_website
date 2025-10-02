from typing import List

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorted(heights)
        change = 0
        for i in range(len(heights)):
            if heights[i] != expected[i]:
                change += 1
        return change


test = Solution()
print(test.heightChecker(heights = [1,1,4,2,1,3]))
print(test.heightChecker(heights = [5,1,2,3,4]))
print(test.heightChecker(heights = [1,2,3,4,5]))