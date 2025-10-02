from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # n1 = len(l1)
        # n2 = len(l2)
        # newl1 = l1.reverse()
        # newl2 = l2.reverse()
        # # print(n1) #3
        # # print(n2) #3
        # for i in range(n1):
        #     for j in range(n2):
        #         print(newl1[i] + newl2[j])
        #         if (newl1[i] + newl2[j]) < 10:
        #             [newl1[i] + newl2[j]]
        #         else:
        #             [(newl1[i] + newl2[j]) / 10]
        # return []
        dummyhead = ListNode(0)
test = Solution()
print(test.addTwoNumbers(l1 = [2,4,3], l2 = [5,6,4]))
# print(test.addTwoNumbers(l1 = [0], l2 = [0]))
# print(test.addTwoNumbers(l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]))