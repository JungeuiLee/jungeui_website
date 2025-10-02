class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # nums1+= nums2
        # nums1.sort()
        # # nums1 = nums1[len(nums1)-(m+n):]
        # nums1[:m-1:-1]
        # nums1.sort()

        for i in range(n):
            nums1[m+i] = nums2[i]
        nums1.sort()



test = Solution()
print(test.merge(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3))
print(test.merge(nums1 = [1], m = 1, nums2 = [], n = 0))
print(test.merge(nums1 = [0], m = 0, nums2 = [1], n = 1))
