from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # left = 0
        # for i in range(len(nums)):
        #     if nums[i] != val:
        #         nums[left] = nums[i]
        #         left += 1

        # return left

        left = 0
        right = len(nums) - 1
        while left <= right:
            if nums[left] == val:
                # nums[left] = '_'
                nums[left], nums[right] = nums[right], nums[left]
                right -=1 
            else:
                left += 1
        
test = Solution()
print(test.removeElement(nums = [3,2,2,3], val = 3))
print(test.removeElement(nums = [0,1,2,2,3,0,4,2], val = 2))