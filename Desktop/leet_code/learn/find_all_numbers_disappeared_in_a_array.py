from typing import List

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # n = len(nums)
        # lst = []

        # for i in range(1, n + 1):
        #     if i not in nums:
        #         lst.append(i)
        # return lst

        for num in nums:
            index = abs(num) - 1
            nums[index] = -abs(nums[index])
            
        return [i + 1 for i in range(len(nums)) if nums[i] > 0]

test = Solution()
print(test.findDisappearedNumbers(nums = [4,3,2,7,8,2,3,1]))
print(test.findDisappearedNumbers(nums = [1,1]))