from typing import List

class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        # max = 0
        # maxInd = 0
        # twice = 0
        # nums.sort()
        # for i in range(len(nums)):
        #     twice = max
        #     if nums[i]> max:
        #         max = nums[i]
        #         maxInd = i

        # if twice * 2 > max:
        #     return -1
        # else:
        #     return maxInd

        max_val = max(nums)
        max_index = nums.index(max_val)

        for i in range(len(nums)):
            if i != max_index and nums[i] * 2 > max_val:
                return -1
        return max_index

test = Solution()
print(test.dominantIndex(nums = [3,6,1,0]))
print(test.dominantIndex(nums = [1,2,3,4]))