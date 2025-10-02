from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode()
        dummy = result

        dummy.next = head
        dummy = dummy.next
        print(result)
        print(head.val)

def list_to_linked(lst):
    dummy = ListNode()
    cur = dummy
    for val in lst:
        cur.next = ListNode(val)
        cur = cur.next
    return dummy.next

test = Solution()
head1 = list_to_linked([1,2,3,4])
head2 = list_to_linked([])
head3 = list_to_linked([1])
head4 = list_to_linked([1,2,3])

print(test.swapPairs(head1))
print(test.swapPairs(head2))
print(test.swapPairs(head3))
print(test.swapPairs(head4))