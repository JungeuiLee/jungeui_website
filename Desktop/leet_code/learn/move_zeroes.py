from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        for j in range(1, len(nums)):
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
            print(nums)

test = Solution()
print(test.moveZeroes(nums = [0,1,0,3,12]))
print(test.moveZeroes(nums = [0]))