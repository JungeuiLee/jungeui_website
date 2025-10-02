class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        previous = 0
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []

test = Solution()
print(test.twoSum(nums = [2,7,11,15], target = 9))
print(test.twoSum(nums = [3,2,4], target = 6))
print(test.twoSum(nums = [3,2,3], target = 6))
print(test.twoSum(nums = [3, 3], target = 6))
        # for i in nums:
        #     if i + i == target:
        #         continue
        #     previous = i
        #     if i + previous == target:
        #         return i, previous


        # for i in range(len(nums)-1):
        #     current = nums[i]
        #     for j in range(len(nums)):
        #         next = nums[j]
        #         if current == next:
        #             i+1
        #         if current + next == target:
        #             return (i, j)

            # current = nums[i]
            # previous = nums[0]
            # if current == previous:
            #     previous = nums[i]
            # if current + previous == target:
            #     return (i, i+1)

            # if nums[i] == nums[i]:
            #     i
            # if nums[i] + nums[i+1] == target:
            #     i + 1
            #     return (i, i+1)

test = Solution()
print(test.twoSum(nums = [2,7,11,15], target = 9))
print(test.twoSum(nums = [3,2,4], target = 6))
print(test.twoSum(nums = [3,2,3], target = 6))
print(test.twoSum(nums = [3, 3], target = 6))