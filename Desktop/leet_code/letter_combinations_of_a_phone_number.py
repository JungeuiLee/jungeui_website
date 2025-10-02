class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if not digits:
            return []
        letter = [""]
        lst = []
        digitToLetter = {"2":['a', 'b', 'c'],
                         "3":['d', 'e', 'f'],
                         "4":['g', 'h', 'i'],
                         "5":['j', 'k', 'l'],
                         "6":['m', 'n', 'o'],
                         "7":['p', 'q', 'r', 's'],
                         "8":['t', 'u', 'v'],
                         "9":['w', 'x', 'y', 'z'],
                         }
        for i in digits:
            if i in digitToLetter:
                # for alp in digitToLetter[i]:
                #     letters += alp
                lst.append(digitToLetter[i])

        # letter.append(lst[0][0] + lst[1][0])
        # letter.append(lst[0][0] + lst[1][1])
        maxLen = 0
        for j in lst:
            if maxLen < (len(j)):
                maxLen = len(j)
        
        for n in lst:
            temp = []
            for a in letter:
                for b in n:
                    temp.append(a + b)
            letter = temp
        # return letter

        
                
test = Solution()
print(test.letterCombinations(digits = "23"))
# print(test.letterCombinations(digits = ""))
# print(test.letterCombinations(digits = "2"))