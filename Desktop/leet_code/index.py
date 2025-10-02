class Solution:
    def findNumbers(self, nums: list[int]) -> int:
        check = 0
        int = 0
        for i in nums:
            while i % 10:
                check += 1
                if check % 2 == 0: #even
                    int += 1
        return int



test = Solution()
test.findNumbers(nums = [12,345,2,6,7896])
test.findNumbers(nums = [555,901,482,1771])