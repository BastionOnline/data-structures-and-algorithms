# Setup
# Create node class, not connected to anything
# Create cache, set cap and init-connected nodes
# do simple functions and assign helper functions
# create helper functions


class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev, self.next = None, None

class LRUCache:

    def __init__(self, capacity: int):
        # establish capcity of cache
        self.cap = capacity
        
        # set cache as hash
        self.cache = {}

        # est left and right dummy nodes to track usage
        # left: Least Recently Used
        # right: Most Recently Used
        self.left, self.right = Node(0,0), Node(0,0)

        # join nodes together
        self.left.next, self.right.prev = self.right, self.left

    # remove node from list
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    # insert at right
    def insert(self, node):
        # before right node, and right node itself
        prev, nxt = self.right.prev, self.right
        # insert inbetween
        prev.next, nxt.prev = node, node # don't assign to property, node.prev, node.next. connect to exact node
        node.prev, node.next = prev, nxt


    # get value and remove from cache
    def get(self, key: int) -> int:
        if key in self.cache:
            # regardless where it sits in the linked-list, pull it
                # self.cache[key] IS NODE OBJECT
            self.remove(self.cache[key])
            
            # then put it a the right
                # this over time will create a list of least to most recently used.
            self.insert(self.cache[key])

            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # node exists with the same value, remove it from hash
            self.remove(self.cache[key])

        # create new node and cache (hash)
        self.cache[key] = Node(key,value)
        
        # wire the new node
        self.insert(self.cache[key])

        # check if capcity is exceeded
        if len(self.cache) > self.cap:
            # remove LRU from list and delete from cache (hash)
            # returns node
            lru = self.left.next

            self.remove(lru) #?????? why not lru.key
            del self.cache[lru.key] #cache only has keys, so you need the lru key to access cache