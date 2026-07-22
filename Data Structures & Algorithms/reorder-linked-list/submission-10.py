# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # divide the list into 2 halves
        slow = head
        fast = head
        while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
        # split the list : now slow has the second half, head the first half
        second = slow.next
        slow.next = None
        # now the first half always has more nodes, even when even, but that's not an issue as the last node added to the result will be the last node in either list
        # revese the second
        prev = None
        cur = second
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
        cur.next = head
        


