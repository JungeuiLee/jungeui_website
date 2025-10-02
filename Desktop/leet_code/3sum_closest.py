class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        n = len(nums)
        nums.sort()
        closest = float('inf')
        for i in range(n - 2):
            x = nums[i]
            left = i + 1
            right = n - 1

            while left < right:
                y = nums[left]
                z = nums[right]
                total = x + y + z

                if abs(target - total) < abs(target - closest):
                    closest = total
                
                if total < target:
                    left += 1
                elif total > target:
                    right -= 1
                else:
                    return total
        return closest
                    

test = Solution()
print(test.threeSumClosest(nums = [-1,2,1,-4], target = 1))
print(test.threeSumClosest(nums = [0,0,0], target = 1))
print(test.threeSumClosest(nums = [0,1,2], target = 0))