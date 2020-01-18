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
        self.vals = {}
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

            #add the values the vals map
            self.vals[key] = value

        elif self.len == self.capacity:
            self.pop_least_used()
            self.put(key, value)


    def get(self, value):
        """Check for a given value"""

        if value in self.vals:
            self.adjust_cache(value)
            return value

        return -1


    def pop_least_used(self):

        self.tail.prev = self.tail.prev.prev
        self.tail.prev.next = self.tail


    def adjust_cache(self, value):
        """ When a node is referenced, move the node to the top of the cache. This ensures that the
        least recently used node remains previous to the tail."""


        curr = self.head.next

        while curr:
            if curr.value == value:

                dummy1 = curr.next
                dummy2 = curr.prev

                #adjust the links of the node
                curr.next = self.head.next
                curr.prev = self.head

                #adjust the links of the cache nodes

                self.head.next.next.prev = curr
                self.head.next = curr

                dummy2.next = dummy1
                dummy1.prev = dummy2
                return

            else:
                curr = curr.next




