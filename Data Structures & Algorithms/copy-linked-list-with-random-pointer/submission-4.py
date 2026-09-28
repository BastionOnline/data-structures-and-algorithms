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
        newLLHash = {None:None}

        # loop once to copy empty nodes
        curr = head
        while curr:
            # copy node data
            currNodeValue = Node(curr.val)
            
            # update copyHash so its Node: Value
            # newLLHash[curr] = currNodeValue
            
            # increment
            curr = curr.next

        # loop again to copy properties
        curr = head
        while curr:
            copyNode = newLLHash[curr]
            copyNode.next = newLLHash[curr.next]
            copyNode.random = newLLHash[curr.random]
            curr.next
        
        return newLLHash[head]