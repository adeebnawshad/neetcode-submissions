# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # 0, 1, 2, 3, 4, 5, 6, 7
        # 0, 6, 1, 5, 2, 4, 3
        # 0, n, 1, n-1, 2, n-2, 3
        # nodes are alternating from the beginning and the end
        
        # divide the list into 2 parts
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # once fast reaches the end / is about to reach tht end, slow is at the halfway node, rounded up for lists of even length
        # cut the list
        second = slow.next
        slow.next = None
        # reverse the second part
        prev = None
        cur = second
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        # now head of reversed second part of list is at prev
        # merge them with alternating nodes
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
        