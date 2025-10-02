class Solution:
    def longestPalindrome(self, s: str) -> str:
        def is_pal(seq):
            return seq == seq[::-1]
        lst = []
        pst = []
        longest = ""
        for i in range(len(s)):
            # lst.append(s[i])
            for j in range(i + 1, len(s)+1):
                substring = s[i:j]
                if is_pal(substring) and len(substring) > len(longest):
                    longest = substring
        return longest
                # lst.append(s[j])
                # print(lst, lst[::-1])
        #         if lst == lst[::-1]:
        #             pst = lst
        #     lst = []
        # print(pst)

test = Solution()
print(test.longestPalindrome(s = "babad"))
print(test.longestPalindrome(s = "cbbd"))