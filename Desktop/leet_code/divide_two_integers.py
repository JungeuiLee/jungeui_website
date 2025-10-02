class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1

        if divisor == 1:
            return dividend
        
        out = 0
        max_shift = dividend.bit_length() - divisor.bit_length()
        negative = (dividend < 0) != (divisor < 0)
        if max_shift < 0:
            return 0
        dividend = abs(dividend)
        divisor = abs(divisor)

        for shift in range(max_shift, -1, -1):
            if dividend >= (divisor << shift):
                dividend -= divisor << shift
                out += 1 << shift

        while dividend >= divisor:
            dividend -= divisor
            out += 1

        return -out if negative else out
        

test = Solution()

print(test.divide(dividend= 7, divisor= -3))
print(test.divide(dividend= 2147483647, divisor= 2))