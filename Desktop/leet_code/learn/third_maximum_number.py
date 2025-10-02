from typing import List

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        # change = 0
        # max = 0
        # nums.sort()
        # nums.reverse()
        # lst = []
        # for i in range(len(nums)):
        #     if nums[i] > max:
        #         max = nums[i]
        #         change += 1
            
        #     if change == 2:
        #         return i + 1

        # for i in range(1, len(nums)):
        #     if nums[i] != nums[i - 1]:
        #         lst.append(nums[i])

        # print(lst)

        nums = list(set(nums))
        print(nums)
        nums.sort(reverse=True)

        if len(nums) >= 3:
            return nums[2]
        else:
            return nums[0]
        

test = Solution()
print(test.thirdMax(nums = [3,2,1]))
print(test.thirdMax(nums = [1,2]))
print(test.thirdMax(nums = [2,2,3,1]))