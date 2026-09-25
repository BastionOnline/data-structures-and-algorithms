# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head
    
        while curr:
            # copy next node
            nextNode = curr.next
            
            # copy prev to next node
            curr.next = prev
    
            # move prev foward
            prev = curr

            # move curr forward
            curr = nextNode
        
        return prev