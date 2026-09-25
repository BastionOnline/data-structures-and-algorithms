# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find mid point
            # use slow and fast pointer

        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # slow exiting here shows the LAST node of, what is now, the low sublist
        # increment slow by one at midpoint to place in the OTHER list

        # midpoint now held by slow
        curr = slow.next

        # lower half of sublist needs to end.
        # lowNode1 -> lowNode2 -> Null
        slow.next = None

        # higher half of sublist previous should be None.
        # Null <- highNode1 <- highNode2
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