# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # create fast and slow pointer starting at head:
        fast, slow = head, head

        # check for null using the fast pointer
        while fast and fast.next:
            # increment slow by 1
            slow.next
            
            # increment slow by 2
            fast.next.next

            # check if crossing
            if fast == slow:
                return False
            else:
                return True
