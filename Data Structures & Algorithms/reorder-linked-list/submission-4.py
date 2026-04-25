# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # divide the list into 2 halves
        if not head.next:
            return
        slow, fast = head, head
        while fast and fast.next:
            prev = slow # to cut the list
            slow = slow.next
            fast = fast.next.next
        prev.next = None # split the list : now slow has the second half, head the first half
        # revese the second
        prev = None
        cur = slow
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        # now prev has the reversed second half
        # merge the lists, alternating between l1 and l2
        dummy = node = ListNode()
        l1 = head
        l2 = prev
        count = 1
        while l1 and l2:
            if count % 2 == 1:
                node.next = l1
                l1 = l1.next
            else:
                node.next = l2
                l2 = l2.next
            node = node.next
            count += 1
        node.next = l2


