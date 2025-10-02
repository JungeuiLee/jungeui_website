class Solution:
    def canJump(self, nums: list[int]) -> bool:
        # n = len(nums)
        # if n == 1:
        #     return True

        # for i in range(len(nums)-1):
        #     if nums[i] + (i+1) >= n:
        #         # print(nums[i], (i+1), n)
        #         return True
        # return False

        max_reach = 0
        for i in range(len(nums)):
            if i > max_reach:
                return False
            max_reach = max(max_reach, i + nums[i])
        return True

test = Solution()
print(test.canJump(nums = [2,3,1,1,4]))
print(test.canJump(nums = [3,2,1,0,4]))
print(test.canJump(nums = [1,2,3]))
print(test.canJump(nums = [0,2,3]))
print(test.canJump(nums = [1,0,1,0]))
