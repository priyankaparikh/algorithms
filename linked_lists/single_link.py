"""python implementation for a singly linked linked list."""


class Node():
    """Node object."""

    def __init__(self, value, next=None):
        """A node has two attributes, it's own value and a pointer to the
        next node."""
        self.value = value
        self.next = next

    def get_data(self):
        """returns the value of a given node."""
        return self.value

    def get_next(self):
        """returns the next node to a given node."""
        return self.next

    def set_next(self, next):
        """Sets the pointer to the next node."""
        self.next = next


class Linked_list():
    """linked list object."""

    def __init__(self, head):
        """Instantiate a linked list to point to the head"""
        self.head = head

    def get_head(self):
        """return the first node value."""
        return self.head.value

    def get_tail(self):
        """Return the value of the last node."""
        curr =  self.head

        while curr:
            if not curr.next:
                return curr.value
            else:
                curr = curr.next

    def insert_node_idx
