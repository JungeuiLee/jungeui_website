from typing import List

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        count = 0
        for num in range(len(arr)):
            if arr[num] == 0:
                count += 1
                
        i = len(arr) - 1
        j = len(arr) + count - 1
        
        while i < j:
            if j < len(arr):
                arr[j] = arr[i]

            if arr[i] == 0:
                j -= 1
                if j < len(arr):    
                    arr[j] = 0

            i -= 1
            j -= 1 

        print(arr)
        
test = Solution()
print(test.duplicateZeros([1,0,2,3,0,4,5,0]))