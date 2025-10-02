class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        result = []
        nums.sort()
        for i in range(len(nums)-2):
            x = nums[i]
            # y = nums[i + 1]

            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # 포인터 두개 사용
            #  x좌표 처음으로 박아두고 y는 그 다음부터 z는 마지막 요소부터
            left = i + 1
            right = len(nums) - 1

            while left < right:
                y = nums[left]
                z = nums[right]
                total = x + y + z

                if total == 0:
                    result.append([x,y,z])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    left += 1
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1
        return result

test = Solution()
print(test.threeSum(nums = [-1,0,1,2,-1,-4]))
print(test.threeSum(nums = [0,1,1]))
print(test.threeSum(nums = [0,0,0]))
print(test.threeSum(nums = [0,0,0,0]))