# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        leading = dummy
        lagging = dummy

        # move fast pointer up to create offset
        for i in range(n+1):
            leading = leading.next
        
        # move both pointers until 'fast' hits end
        while leading:
            leading = leading.next
            lagging = lagging.next
        
        # skip node
        lagging.next = lagging.next.next

        # return Linked-list
        return dummy.next
