# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # split list into 2 parts
        slow = head
        fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        second = slow.next
        slow.next = None
        
        # reverse second part
        prev = None
        cur = second
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        # prev has head of reversed list

        # join the two lists alternating
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
        