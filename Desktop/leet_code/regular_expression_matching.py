class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # "*" = set("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z")
        # if len(s) != len(p):
        #     return False
        
        x, y = len(s), len(p)
        # for i, j in zip(s, p):
        #     if i == j:
        #         return True
        #     else:
        #         if j == ".":
        #             j == i
                
        #         if j == "*":
        i = 0
        while i < x:
            if s[i] == p[i]:
                i += 1
            else:
                if p[i] == ".":
                    p[i] == s[i]
                    i = 0
                if p[i] == "*":
                    if i == 0:
                        p[i] == None
                    else:
                        if s[i] 
                i += 1
            return True
        


        
test = Solution()
print(test.isMatch(s = "aa", p = "a"))
print(test.isMatch(s = "aa", p = "a*"))
print(test.isMatch(s = "aa", p = ".*"))
print(test.isMatch(s = "aab", p = "c*a*b"))