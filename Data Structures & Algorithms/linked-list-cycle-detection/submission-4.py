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
            # reassign and increment slow by 1
            slow = slow.next
            
            # reassign and increment fast by 2
            fast = fast.next.next

            # check if crossing
            if fast == slow:
                return True
        
        # Whole list has been checked, null hit, no loop detected
        return False
