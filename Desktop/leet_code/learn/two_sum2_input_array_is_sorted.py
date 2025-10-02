from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        while left < right:
            if numbers[left] + numbers[right] > target:
                right -= 1

            if numbers[left] + numbers[right] < target:
                left += 1

            if numbers[left] + numbers[right] == target:
                return [left + 1, right + 1]

test = Solution()
print(test.twoSum(numbers = [2,7,11,15], target = 9))
print(test.twoSum(numbers = [2,3,4], target = 6))
print(test.twoSum(numbers = [-1,0], target = -1))