class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        # for i in range(len(haystack)):
        #     if needle in haystack:
        #         return i
        #     return -1

        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1
        

test = Solution()
print(test.strStr(haystack = "sadbutsad", needle = "sad"))
print(test.strStr(haystack = "leetcode", needle = "leeto"))
print(test.strStr(haystack = "hello", needle = "ll"))