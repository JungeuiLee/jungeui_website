class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        lst  = nums1 + nums2
        mid1 = 0
        mid2 = 0
        lst.sort()
        if (len(lst) % 2 == 0):
            mid1 = lst[len(lst)//2-1]
            mid2 = lst[len(lst)//2]
            return (mid1 + mid2) / 2
        else:
            return lst[len(lst)//2]
test = Solution()
print(test.findMedianSortedArrays(nums1 = [1,2], nums2 = [3,4]))