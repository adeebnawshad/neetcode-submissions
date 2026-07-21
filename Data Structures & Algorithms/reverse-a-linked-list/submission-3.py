# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 0->1->2->3->None # prev = None, cur = 0; prev = 0, cur = 1, ... prev = 3, cur = None
        # 3->2->1->0->None
        prev = None
        cur = head # 0
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        return prev