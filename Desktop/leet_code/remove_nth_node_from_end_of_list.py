from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        result = []
        head_length = len(head)
        index = head_length - n
        result.append(head[:index])
        result.append(head[index+1:head_length])
        # print(result)
        result2 = []
        for i in result:
            if i == []:
                result.pop()
            else:
                for j in i:
                    result2.append(j)
        return result2

test = Solution()
test.removeNthFromEnd(head = [1,2,3,4,5], n = 2)
test.removeNthFromEnd(head = [1], n = 1)
test.removeNthFromEnd(head = [1,2], n = 1)