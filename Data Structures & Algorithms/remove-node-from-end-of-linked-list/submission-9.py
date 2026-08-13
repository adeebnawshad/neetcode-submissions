# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        advance = dummy
        for _ in range(n + 1):
            advance = advance.next
        behind = dummy
        while advance:
            advance = advance.next
            behind = behind.next
        behind.next = behind.next.next
        return dummy.next
