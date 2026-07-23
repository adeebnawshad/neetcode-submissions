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
        # slow is at the middle now if odd, at the rounded up middle if even
        second = slow.next
        slow.next = None
        # the first list is a bit longer than the second but that's okay as we alternate and the last element can be in either list
        # reverse the second half
        prev = None
        cur = second
        while cur:
                nxt = cur.next
                cur.next = prev
                prev = cur
                cur = nxt
        # now head of the second list is prev
        # merge the two lists with alternating elements to the list, starting with first list
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
