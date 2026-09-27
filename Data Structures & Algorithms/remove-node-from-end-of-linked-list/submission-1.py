# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        fast = dummy
        slow = dummy

        # move fast pointer up to create offset
        for i in range(n+1):
            fast = fast.next
        
        # move both pointers until 'fast' hits end
        while fast:
            fast = fast.next
            slow = slow.next
        
        # skip node
        slow.next = slow.next.next

        # return Linked-list
        return dummy.next
