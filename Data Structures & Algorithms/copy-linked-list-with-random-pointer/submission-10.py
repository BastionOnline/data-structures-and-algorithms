"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # create hashmap
            # None filler is used incase there is only 1 node and no more
        oldAddressKey_NewAddressValue = {None:None}

        # loop once to copy empty nodes
        curr = head
        while curr:
            # create NEW node using value of old address and log the NEW address as 
            oldAddressKey_NewNodeAddressValue[curr] = Node(curr.val)

            curr = curr.next

        # loop again to copy properties
        curr = head
        while curr:
            # 1. Grab the NEW node object sitting at address 0x999
            copyNode = oldAddressKey_NewAddressValue[curr]
            
            # 2. Look up the NEW node addresses for next and random, and attach them!
            copyNode.next = oldAddressKey_NewAddressValue[curr.next]
            copyNode.random = oldAddressKey_NewAddressValue[curr.random]
            
            curr = curr.next
        
        return oldAddressKey_NewAddressValue[head]