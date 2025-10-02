from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        result = ListNode()
        dummy = result

        while lists:
            

test = Solution()
print(test.mergeKLists(lists = [[1,4,5],[1,3,4],[2,6]]))
print(test.mergeKLists(lists = []))
print(test.mergeKLists(lists = [[]]))