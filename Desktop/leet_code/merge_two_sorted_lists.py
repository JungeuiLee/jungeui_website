from typing import Optional

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        result= ListNode()
        cur = result

        while list1 and list2:
            if list1.val > list2.val:
                cur.next = list2
                list2 = list2.next
            
            else:
                cur.next = list1
                list1 = list1.next

            cur = cur.next

        if list1:
            cur.next = list1

        else:
            cur.next = list2
        
        return result.next


test = Solution()
print(test.mergeTwoLists(list1 = [1,2,4], list2 = [1,3,4]))
print(test.mergeTwoLists(list1 = [], list2 = []))
print(test.mergeTwoLists(list1 = [], list2 = [0]))