class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # for i in range(k):
        #     nums.insert(0, nums[-1])
        #     nums.pop()

        n = len(nums)
        k = k % n
        nums.reverse()
        print(nums)
        nums[:k] = reversed(nums[:k])
        print(nums)
        nums[k:] = reversed(nums[k:])
        print(nums)

test = Solution()
print(test.rotate(nums = [1,2,3,4,5,6,7], k = 3))
print(test.rotate(nums = [-1,-100,3,99], k = 2))