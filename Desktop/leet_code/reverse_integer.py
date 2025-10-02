class Solution:
    def reverse(self, x: int) -> int:
        neg = 0
        if x < 0:
            neg = -1
        elif x > 0:
            neg = 1
        else:
            neg = 0

        x = int(str((abs(x)))[::-1])

        if int(x) >= 2**31 -1 or int(x) <= -2**31:
            return 0
        return neg * x


test = Solution()
test.reverse(x = 123)
test.reverse(x = -123)
test.reverse(x = 120)
test.reverse(x = 1534236469)