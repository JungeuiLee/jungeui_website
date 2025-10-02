class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        result = ""
        shortest_len = len(min(strs, key=len))
        i = 0
        if not strs:
            return ""
        for i in range(shortest_len):
            char = strs[0][i]
            for word in strs:
                if word[i] != char:
                    return result
            result += char
        # while (i < shortest_len):
        #     for str in range(len(strs)):
        #         prev = strs[str][0]
        #         curr = strs[str][i]
        #         if prev == curr:
        #             prev = curr
        #             curr = strs[str][i+1]
        #     print(prev, curr)
        #         # if strs[str][i] 
        #             # result += strs[str][i]

        #     i+=1
        return result

test = Solution()
print(test.longestCommonPrefix(strs = ["flower","flow","flight"]))
print(test.longestCommonPrefix(strs = ["dog","racecar","car"]))