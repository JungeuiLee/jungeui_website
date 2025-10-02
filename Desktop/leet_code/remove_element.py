class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        lst = []

        for i in nums:
            if i != val:
                lst.append(i)
        nums[:] = lst
        
        

test = Solution()
print(test.removeElement(nums = [3,2,2,3], val = 3))
print(test.removeElement(nums = [0,1,2,2,3,0,4,2], val = 2))