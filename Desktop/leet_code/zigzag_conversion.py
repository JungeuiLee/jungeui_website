class Solution:
    def convert(self, string: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(string):
            return string
    
        # midlst = [''] * numRows
        # fst, scd = 0, 0
        # # midlst[0] += 'a'
        # # print(midlst[0])
        # for i in s:
        #     if 
        # print(midlst)
        rows = [''] * numRows
        index, step = 0, 1
        result = ''
        for i in string:
            rows[index] += i

            if index == 0:
                step = 1
            
            elif index == numRows - 1:
                step = -1
            index += step
        for row in rows:
            result += row
        return result

test = Solution()
test.convert(string = "PAYPALISHIRING", numRows = 3)
test.convert(string = "PAYPALISHIRING", numRows = 4)
test.convert(string = "A", numRows = 1)