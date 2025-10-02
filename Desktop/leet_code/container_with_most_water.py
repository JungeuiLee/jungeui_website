class Solution:
    def maxArea(self, height: list[int]) -> int:
        n = len(height)
        if n<2 or n > 10**5:
            return 0
        
        max_area = 0
        left, right = 0, n-1

        while left < right:
            x = right - left
            y = min(height[left], height[right])
            max_area = max(max_area, x * y)
            # area = x * y 
            # if max_area < area:
            #     max_area = area
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
            # left += 1
            print(left, right, height[left], height[right])

            # if right == left:
            #     right -= 1
            #     left = 0
            # print(left, right)
            
        return max_area

test = Solution()
print(test.maxArea(height = [1,8,6,2,5,4,8,3,7]))
# print(test.maxArea(height = [8,7,2,1])) #7 but 3