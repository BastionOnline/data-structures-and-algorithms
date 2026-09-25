# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find mid point
            # use slow and fast pointer

        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # slow exiting here shows the LAST node of the list
        # increment slow by one at midpoint to place in the OTHER list

        # midpoint now held by slow
        curr = slow.next
        prev = None

        while curr:
            # flip order
            nextNode = curr.next
            curr.next = prev

            # shift focus
            prev = curr
            curr = nextNode

        # rearrange list
        h, t = head, prev
        
        while t:
            hTemp, tTemp = h.next, t.next
            
            # merge
            h.next = t
            t.next = hTemp

            # shift pointer
            h, t = hTemp, tTemp