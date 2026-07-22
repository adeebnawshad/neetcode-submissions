# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head.next:
                return
        # divide the list into 2 halves
        slow = head
        fast = head
        while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
        # split the list : now slow has the second half, head the first half
        cur = head
        while cur.next != slow:
                cur = cur.next
        cur.next = None
        # revese the second
        prev = None
        cur = slow
        while cur:
                nxt = cur.next
                cur.next = prev
                prev = cur
                cur = nxt
        # now prev has the reversed second half
        # merge the lists, alternating between l1 and l2
        count = 0
        dummy = ListNode()
        cur = dummy
        while head and prev:
                cur.next = head
                head = head.next
                cur = cur.next
                cur.next = prev
                prev = prev.next
                cur = cur.next
        cur.next = head or prev
        


