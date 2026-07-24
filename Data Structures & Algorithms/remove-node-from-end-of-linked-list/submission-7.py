# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        slow = dummy
        fast = dummy
        # we want fast to be n + 1 steps ahead of slow so then we can move both until fast reaches None (the end), then when that happens, slow will be at the index before the node to delete (n + 1th index from the end) - n + 1 nodes behind fast / the end,so the node after n + 1 is the one to delete
        for _ in range(n + 1):
            fast = fast.next
        while fast:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return dummy.next
