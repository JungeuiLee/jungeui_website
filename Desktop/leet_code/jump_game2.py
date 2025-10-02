class Solution:
    def jump(self, nums: list[int]) -> int:
        max_jump = 0
        count = 0
        for i in range(len(nums)):
            if i > max_jump:
                return False
            max_jump = max(max_jump, i + nums[i])
            count += 1
            print(max_jump, i + nums[i], count)
        return True




test = Solution()
print(test.jump(nums = [2,3,1,1,4]))
print(test.jump(nums = [2,3,0,1,4]))