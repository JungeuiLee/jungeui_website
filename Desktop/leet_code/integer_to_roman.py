class Solution:
    def intToRoman(self, num: int) -> str:
        digits = []
        digit = 1
        result = ""
        # symbol = {1 : "I",
        #           5 : "V",
        #           10 : "X",
        #           50 : "L",
        #           100 : "C",
        #           500 : "D",
        #           1000: "M"}
        val_to_symbol = [
            (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
            (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
            (10, "X"), (9, "IX"), (5, "V"), (4, "IV"),
            (1, "I")
        ]

        for value, symbol in val_to_symbol:
            while num >= value:
                result += symbol
                num -= value
        # while num > 0:
        #     digits.append(num % 10)
        #     num //= 10

        # for i in range(len(digits)):
        #     digits[i] = digits[i] * digit
        #     digit *= 10
        # digits.reverse()

        # for j in range(len(digits)):
        #     # if digits[j] // 1000 != 0:
        #         # result += (digit[j] // 1000)*symbol[1000]

        #     if digits[j] // 500 == 1:
        #         if digits[j] / 900 == 1.0:
        #             digits[j] = (100 + 1000)
        #     elif digits[j] // 500 == 0:
        #         if digits[j] / 400 == 1.0:    
        #             digits[j] = (100 + 500)
        #         # result += symbol[500]
        #         # digit[j] -= 500
        #         # if digit[j] // 100 != 0:
        #         #     result += (digit[j] // 100)*symbol[100]
        #     # elif digits[j] // 500 == 0:
        #     #     result += (digits[j] // 100)*symbol[100]
            
        #     if digits[j] // 50 == 1:
        #         if digits[j] / 90 == 1.0:
        #             digits[j] = (10 + 100)
        #         # result += symbol[50]
        #         # digits[j] -= 50
        #         # if digits[j] // 10 != 0:
        #         #     result += (digits[j] // 10)*symbol[10]
        #     elif digits[j] // 50 == 0:
        #         if digits[j] / 40 == 1.0:
        #             digits[j] = (10 + 50)
        #         # result += (digits[j] // 10)*symbol[10]

        #     if digits[j] // 5 == 1:
        #         if digits[j] / 9 == 1.0:
        #             digits[j] = (1 + 10)
        #         # result += symbol[5]
        #         # digits[j] -= 5
        #         # if digits[j] // 1 != 0:
        #         #     result += (digits[j] // 1)*symbol[1]
        #     elif digits[j] // 5 == 0:
        #         if digits[j] / 4 == 1.0:
        #             digits[j] = (1 + 5)
        #         # result += (digits[j] // 1)*symbol[1]


        # for k in range(len(digits)):
        #     print(digits)
        #     if digits[0] // 1000 != 0:
        #         result += (digits[k] // 1000)*symbol[1000]
        #         digits[k] -= (digits[k] // 1000)*1000

        #     if digits[1] // 100 != 0:
        #         if digits[k] // 500 == 1:
        #             result += (digits[k] // 500)*symbol[500]
        #             digits[k] -= 500
        #         if digits[k] // 100 != 0:
        #             result += (digits[k] // 100)*symbol[100]

        #     if digits[2] // 10 != 0:
        #         if digits[k] // 50 == 1:
        #             result += (digits[k] // 50)*symbol[50]
        #             digits[k] -= 50
        #         if digits[k] // 10 != 0:
        #             result += (digits[k] // 10)*symbol[10]

        #     if digits[3] // 1 != 0:
        #         if digits[k] // 5 == 1:
        #             result += (digits[k] // 5)*symbol[5]
        #             digits[k] -= 5
        #         if digits[k] // 1 != 0:
        #             result += (digits[k] // 1)*symbol[1]


        return(result)

test = Solution()
print(test.intToRoman(num = 3749))
print(test.intToRoman(num = 58))
print(test.intToRoman(num = 1994))
print(test.intToRoman(num = 94))