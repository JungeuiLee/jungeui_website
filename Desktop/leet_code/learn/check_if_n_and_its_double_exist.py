from typing import List

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        for i in range(len(arr)):
            for j in range(len(arr)):
                if (arr[i] == 2 * arr[j]):
                    return True
        return False
        

        
test = Solution()
print(test.checkIfExist(arr = [10,2,5,3]))
print(test.checkIfExist(arr = [3,1,7,11]))
print(test.checkIfExist([7,1,14,11]))