from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common = ""
        shortest = strs[0]
        for i in range(len(strs)):
            if len(strs[i]) < len(shortest):
                shortest = strs[i]

        for i in range(len(shortest)):
            char = shortest[i]
            # print(char)
            for j in strs:
                # print(strs[i][j])
                # if strs[i][j] != char:
                #     return strs[i:j]
                if j[i] != char:
                    return shortest[:i]
        return shortest
        # return char
test = Solution()
print(test.longestCommonPrefix(strs = ["flower","flow","flight"]))
print(test.longestCommonPrefix(strs = ["dog","racecar","car"]))