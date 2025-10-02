from typing import Optional



# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        ans = 0

        while fast and fast.next:
            
            
            slow = slow.next
            fast = fast.next.next

        return ans

    
test = Solution()
print(test.detectCycle(head = [3,2,0,-4]))
print(test.detectCycle(head = [1,2]))
print(test.detectCycle(head = [1]))