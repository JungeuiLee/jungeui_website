from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # i = 0
        # j = 0
        # while len(nums1) == m + n:
        #     # if len(nums1) == m + n:
        #     #     break

        #     if nums1[i] >= nums2[j]:
        #         i += 1
            
        #     if nums1[i] < nums2[j]:
        #         nums1[i] = nums2[j]
        #         j += 1

        #     print(nums1)
        for i in range(n):
            nums1[m+i] = nums2[i]
        nums1.sort()
        print(nums1)

test = Solution()
print(test.merge(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3))
print(test.merge(nums1 = [1], m = 1, nums2 = [], n = 0))
print(test.merge(nums1 = [0], m = 0, nums2 = [1], n = 1))