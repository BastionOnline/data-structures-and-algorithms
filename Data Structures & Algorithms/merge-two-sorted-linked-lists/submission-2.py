# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy

        while list1 and list2:
            if list1.val < list2.val:
                # set the next node to the lowest value
                curr.next = list1

                # move list1 down one node
                list1 = list1.next
            else:
                # set the next node to the lowest value
                curr.next = list2

                # move list down one node
                list2 = list2.next
            
            # move pointer forward regardless of which branch was taken
            curr = curr.next
        
        curr.next = list1 if list1 else list2

        return dummy.next