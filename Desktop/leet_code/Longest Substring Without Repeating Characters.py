class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        longest = ""
        for i in range(len(s)):
            for j in range(i+1, len(s)+1):
                substring = s[i:j]
                if len(substring) == len(set(substring)) and len(substring) > len(longest):
                    longest = substring
        return len(longest)
        
        # max = 1
        # lst1 = [s[0]]
        # lst2 = [s[0]]
        # for i in range(1, len(s)):
        #     if s[i] not in lst2:
        #         lst2.append(s[i])
        #         max += 1
        #     # elif s[i] in lst1:
        #     #     lst2 = [s[i]]
        #     # print(lst1, lst2)
        #     elif s[i] in lst2:
        #         if s[i-1] == s[i]:
        #             lst2 = [s[i]]
        #         else:
        #             lst2 = [s[i-1], s[i]]
        #     if len(lst1) < len(lst2):
        #         lst1 = lst2
        # # print(lst1, lst2)

        # # reverse case
        # reversed_s = s[::-1]
        # lst3 = [reversed_s[0]]
        # lst4 = [reversed_s[0]]
        # for i in range(1, len(reversed_s)):
        #     if reversed_s[i] not in lst4:
        #         lst4.append(reversed_s[i])
        #         max += 1
        #     # elif s[i] in lst1:
        #     #     lst2 = [s[i]]
        #     # print(lst1, lst2)
        #     elif reversed_s[i] in lst4:
        #         if reversed_s[i-1] == reversed_s[i]:
        #             lst4 = [reversed_s[i]]
        #         else:
        #             lst4 = [reversed_s[i-1], reversed_s[i]]
        #     if len(lst3) < len(lst4):
        #         lst3 = lst4
        # print(lst3, lst4)

        # if len(lst1) > len(lst3):
        #     return len(lst1)
        # else:
        #     return len(lst3)
        
        # pst = set()
        # cur = set()
        # for i in range(len(s)):
        #     if s[i] not in cur:
        #         cur.append(s[i])
        #     else:
        #         if len(pst) < len(cur):
        #             pst = cur
        #             cur = []
        #         else:
        #             cur = []
        # # print(pst, cur)
        # if len(pst) > len(cur):
        #     return len(pst)
        # else:
        #     return len(cur)
        
        # for i in range(len(s)):
        #     if s[i] not in cur:
        #         cur.add(s[i])
        #         print(pst, cur)
        #     else:
        #         if len(set(pst)) > len(set(cur)):
        #             print(pst, cur)
        #             pass
        #         else:
        #             print(pst, cur)
        #             pst = cur
        #         cur = set()
        #         cur.add(s[i])
        
        # # print(pst, cur)
        # if len(set(pst)) > len(set(cur)):
        #     return len(set(pst))
        # else:
        #     return len(set(cur))

test= Solution()
print(test.lengthOfLongestSubstring("abcabcbb"))
print(test.lengthOfLongestSubstring("bbbbb"))
print(test.lengthOfLongestSubstring("pwwkew"))
print(test.lengthOfLongestSubstring("dvdf"))
print(test.lengthOfLongestSubstring("anviaj"))
print(test.lengthOfLongestSubstring("busvutpwmu"))
print(test.lengthOfLongestSubstring("au"))
print(test.lengthOfLongestSubstring("aab"))
# 에러 1
# 중복되는 요소를 제거하여 최선의 리스트를 정렬하였지만, 테스트 케이스 3번 pw 이후에 
# 리스트 2를 빈 리스트로 재정렬을 해야됨

# 에러 2
# 새로운 테스트 케이스 dwdf 통과 x 

# 에러 3
# 새로운 테스트 케이스 anviaj 통과 x 
# 접근방식이 잘못된듯

# 에러 4
# 새로운 테스트 케이스 busvutpwmu 통과 x 
# 새로운 접근 요
# 시작점을 0으로 맞추는것이 아닌 반복문 안에서 새롭게 바꿔보기

# 에러 5
# aab 케이스를 통해 중복되는 첫 요소는 거르고 
# 두번쨰 요소는 자동적으로 추가하여 다시 반복문이 돌게 하였지만
# 에러 방생