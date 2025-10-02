from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        count = 0
        max_length = 0
        left = 0
        sum = 0

        for i in range(len(nums)):
            if sum + nums[i] != target:
                sum = sum + nums[i]
                count += 1
                max_length = max(count, max_length)
            else:
                count = 0
                max_length = max(count, max_length)
            return max_length


test = Solution()
print(test.minSubArrayLen(target = 7, nums = [2,3,1,2,4,3]))
print(test.minSubArrayLen(target = 4, nums = [1,4,4]))
print(test.minSubArrayLen(target = 11, nums = [1,1,1,1,1,1,1,1]))