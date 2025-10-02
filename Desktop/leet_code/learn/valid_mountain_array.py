from typing import List

class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        high_index = 0
        for i in range(len(arr)):
            if arr[i] >= arr[high_index]:
                high_index = i
        print(high_index)

        if high_index == 0 or arr[high_index] == arr[-1]:
            return False
        

        for left in range(high_index):
            if arr[left] >= arr[left + 1]:
                return False
        
        for right in range(high_index, len(arr) - 1):
            if arr[right] <= arr[right + 1]:
                return False

        return True


test = Solution()
print(test.validMountainArray(arr = [2, 1]))
print(test.validMountainArray(arr = [3, 5, 5]))
print(test.validMountainArray(arr = [0, 3, 2, 1]))