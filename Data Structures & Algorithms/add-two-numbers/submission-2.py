# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy

        carry = 0
        
        # loop
        while l1 or l2 or carry:

            # get values
            v1 = l1.val if l1.val else 0
            v2 = l2.val if l2.val else 0

            # get 10's and 1's place of answer
            total = v1 + v2 + carry
            carry = total // 10  # double slash rounds down
            total = total % 10

            # attach node
            cur.next = ListNode(total)

            # update pointer
            cur = cur.next
            l1 = l1.next if l1.next else None   # get next pointer if it exist
            l2 = l2.next if l2.next else None
        
        return dummy.next
