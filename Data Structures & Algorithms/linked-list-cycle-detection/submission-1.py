# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None:
            return False
        fastptr = head.next
        slowptr = head
        while fastptr != slowptr:
            if fastptr == None or fastptr.next == None:
                return False
            fastptr = fastptr.next.next
            slowptr = slowptr.next
        return True