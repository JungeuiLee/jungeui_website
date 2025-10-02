class Solution:
    def addBinary(self, a: str, b: str) -> str:
        d0 = 0
        d1 = 1
        d2 = 10
        d3 = 11
        d4 = 100
        d5 = 101
        d6 = 110
        d7 = 111
        d8 = 1000
        d9 = 1001
        # print(self.tran(int(a)), self.tran(int(b)))

        powerA, resultA = 0, 0
        for num in reversed(a):
            resultA += (2**powerA) * int(num)
            powerA += 1

        powerB , resultB = 0, 0
        for num in reversed(b):
            resultB += (2**powerB) * int(num)
            powerB += 1

        # print(resultA, resultB)
        total = resultA + resultB
        # print(total)
        if total == 0:
            return "0"
        binary = ""
        while total > 0:
            binary = str(total%2) + binary
            total = total // 2
            # print(binary)
        return binary
    
    # def tran(self, x: int):
    #     power = 0
    #     result = 0
    #     for num in x:
    #         result += (2**power) * num
    #         power += 1
    #     return result
            

test = Solution()

print(test.addBinary(a = "11", b = "1"))
print(test.addBinary(a = "1010", b = "1011"))