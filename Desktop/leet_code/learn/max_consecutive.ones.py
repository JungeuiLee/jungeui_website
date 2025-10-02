from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # left = 0
        # max = 0

        # for i in range(left, len(nums)):
        #     count = 0
        #     if (nums[left] != nums[i]):
        #         return i + 1

        #     # if count > max:
        #     #     max = count
        #     # left += 1
        #     # return count

        count = 0
        max_count = 0
        for num in nums:
            if num == 1:
                count += 1
                max_count = max(max_count, count)
            else:
                count = 0
        return max_count


test = Solution()
print(test.findMaxConsecutiveOnes(nums = [1,1,0,1,1,1]))
print(test.findMaxConsecutiveOnes(nums = [1,0,1,1,0,1]))