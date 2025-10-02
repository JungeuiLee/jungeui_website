class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        nums.sort()
        n = len(nums)
        return nums[n//2]
test = Solution()
print(test.majorityElement(nums = [9, 8, 8, 9, 6, 7, 9]))
print(test.majorityElement(nums = [2,2,1,1,1,2,2]))