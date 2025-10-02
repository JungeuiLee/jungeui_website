class Solution:
    def isPalindrome(self, x: int) -> bool:
        test = str(x)
        # print(test[::-1])
        if test[::-1] == test:
            return True
        else:
            return False
        # elif test[::-1] != test:
        #     return False

test = Solution()
print(test.isPalindrome(x = 121))
print(test.isPalindrome(x = -121))
print(test.isPalindrome(x = 10))