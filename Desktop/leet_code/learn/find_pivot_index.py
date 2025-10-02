from typing import List

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sumLeft = []
        sumRight = []
        for i in range(len(nums)):
            sumLeft = nums[0:i]
            sumRight = nums[i+1:len(nums)]

            if sum(sumLeft) == sum(sumRight):
                return i
        return -1
test = Solution()
print(test.pivotIndex(nums = [1,7,3,6,5,6]))
print(test.pivotIndex(nums = [1,2,3]))
print(test.pivotIndex(nums = [2,1,-1]))