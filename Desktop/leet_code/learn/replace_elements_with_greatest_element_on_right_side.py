from typing import List

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # lst = []
        # for i in range(len(arr) - 1):
        #     lst.append(max(arr[i + 1 :]))

        # lst.append(-1)
        # return lst

        max_val = -1
        for i in range(len(arr) - 1, -1, -1):
            arr[i], max_val = max_val, max(arr[i], max_val)
        return arr
        

test = Solution()
print(test.replaceElements(arr = [17,18,5,4,6,1]))
# Output: [18,6,6,6,1,-1]
# Explanation: 
# - index 0 --> the greatest element to the right of index 0 is index 1 (18).
# - index 1 --> the greatest element to the right of index 1 is index 4 (6).
# - index 2 --> the greatest element to the right of index 2 is index 4 (6).
# - index 3 --> the greatest element to the right of index 3 is index 4 (6).
# - index 4 --> the greatest element to the right of index 4 is index 5 (1).
# - index 5 --> there are no elements to the right of index 5, so we put -1.
print(test.replaceElements(arr = [400]))