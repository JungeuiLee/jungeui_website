class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        result = 0
        sign = 1
        while i < len(s) and s[i] == " ":
            i += 1

        if i < len(s) and (s[i] == "+" or s[i] == "-"):
            sign = -1 if s[i] == "-" else 1
            i += 1

        while i < len(s) and s[i].isdigit():
            result = result * 10 + int(s[i])
            i+=1

            if result * sign >= 2**31:
                return 2**31 -1
            if result * sign < -(2**31):
                return -2**31
        
        return(result * sign)

test = Solution()
test.myAtoi("42")
# test.myAtoi("  -042")
# test.myAtoi("1337c0d3")
# test.myAtoi("0-1")
# test.myAtoi("words and 987")
print(test.myAtoi(s = "2147483648"))

        # char = 0
        # step1 = ''
        # for i in s:
        #     if i == " ":
        #         continue
        #     else:
        #          step1 +=i

        # step2 = ''
        # sign = 0
        # # if step1[0] == "+":
        # #     sign = -1
        # # elif step1[0] == "-":
        # #     sign = 1
        # # for i in range(1, len(step1)):
        # #     if step1[i] == "0":
        # #          continue
        # #     step2 += step1[i]
        # if char < len(step1) and (step1[char] == "+" or step1[char] == "-"):
        #     sign = -1 if step1[i] == '-' else 1
        #     char += 1
                


        #     # if int(i) == True:
        #     #         answer += i
        # print(step2)