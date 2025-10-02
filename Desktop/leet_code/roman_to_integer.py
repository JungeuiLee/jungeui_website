class Solution:
    def romanToInt(self, s: str) -> int:
        lst = []
        lst2 = []
        result = 0
        # sym_to_val = [ 
        #     ("CM", 900), ("CD", 400),
        #     ("XC", 90), ("XL", 40), 
        #     ("IX", 9), ("IV", 4)
        # ]
        sym_to_val = {"M": 1000, "D": 500, "C": 100, 
                      "L": 50, "X": 10, 
                      "V": 5, "I": 1
        }
        lst = list(s)

        # lst 안에 있는 요소들 2개씩 묶어서 검사
        # for i in range(len(s) - 1, -1, -1):
        #     test = ""
        #     test += s[i-1]
        #     test += s[i]
        #     lst2.append(test)
        # lst2.reverse()
        # lst2 = lst2[1:]

        # new_lst2 = []
        # for ele in lst2:
        #     found = False
        #     for sym, val in sym_to_val:
        #         if ele == sym:
        #             new_lst2.append(val)
        #             found = True
        #     if not found:
        #         new_lst2.append(ele)

        total = 0
        prev_value = 0

        for char in reversed(s):
            curr_value = sym_to_val[char]
            if curr_value < prev_value:
                total -= curr_value
            else:
                total += curr_value
            prev_value = curr_value
        return total


        # for sym, val in sym_to_val:
        #     for i in lst2[::]:
        #         if i == sym:
        #             lst2[lst2.index(i)] = val
        #         else:
        #             lst2.remove(i)
        # print(lst2)
                    
            
        # print(result)

test=Solution()
print(test.romanToInt(s = "III"))
print(test.romanToInt(s = "LVIII"))
print(test.romanToInt(s = "MCMXCIV"))