""" A doubly linked list imagined and utilized as an LRU cache that gives us 0(1) get, pop and delete operations"""

class dlNode():
    """A single node object for the double ended linked list implementation"""
    def __init__(self, key=0, value=0, prev=None, next=None):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next


class LRUCache():
    """A double link linked list."""
    def __init__(self, capacity):
        dummy1 = dlNode()
        dummy2 = dlNode()
        self.head = dummy1
        self.tail = dummy2
        self.head.next = self.tail
        self.tail.prev = self.head

        self.capacity = capacity
        self.len = 0


    def put(self, key, value):
        """Insert a node to the front of the linked list after the head."""

        if self.len < self.capacity:
            node1 = dlNode(key, value, self.head, self.head.next)

            #change the pointers for the head
            self.head.next = node1
            self.head.next.next.prev = node1

            #increase the length of the cache
            self.len += 1


    def get(self, value):
        """Check for a given value"""
        curr = self.head

        while curr:
            if curr.value == value:
                return curr.value
            else:
                curr = curr.next

        return -1


    def pop_least_used(self):

        self.tail.prev = self.tail.prev.prev


    def adjust_cache(self):
        pass

