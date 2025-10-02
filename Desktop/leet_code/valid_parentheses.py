class Solution:
    def isValid(self, s: str) -> bool:
        # a = ['(', ')']
        # b = ['{', '}']
        # c = ['[', ']']

        # if len(s) % 2 == 1:
        #     return False
        
        # if (s[0] == a[1] or s[0] == b[1] or s[0] == c[1]):
        #     return False

        
        # stack = []

        # s_reverse = s[::-1]
        # for i in range(len(s)):
        #     step = i

        #     if s[i] in a[0]:
        #         if s_reverse[i] in a[1]:
        #             return True
        #         else:
        #             step = i + 1
        #             if s[step] in a[1]:
        #                 return True
        #             else:
        #                 return False
            
        #     if s[i] in b[0]:
        #         if s_reverse[i] in b[1]:
        #             return True
        #         else:
        #             step = i + 1
        #             if s[step] in b[1]:
        #                 return True
        #             else:
        #                 return False
                
        #     if s[i] in c[0]:
        #         if s_reverse[i] in c[1]:
        #             return True
        #         else:
        #             step = i + 1
        #             if s[step] in c[1]:
        #                 return True
        #             else:
        #                 return False

        stack = []
        mapping = {'(' : ')',
                   '[' : ']',
                   '{' : '}'
                   }
        
        a = ['(', ')']
        b = ['{', '}']
        c = ['[', ']']
        for char in s:
            if char in mapping:
                stack.append(char)
            elif char in mapping.values():
                if not stack or mapping[stack.pop()] != char:
                    return False
            else:
                return False
        return not stack
            
test = Solution()
print(test.isValid(s = "()"))
print(test.isValid(s = "()[]{}"))
print(test.isValid(s = "(]"))
print(test.isValid(s = "([])"))
print(test.isValid(s = "(){}}{"))