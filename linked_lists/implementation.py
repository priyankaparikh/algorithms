"""python implementation for a singly linked linked list."""


class Node():
    """Node object."""

    def __init__(self, value):
        """."""
        self.value = value
        self.next = None


class linked_list():
    """linked list object."""

    def __init__(self, head):
        """."""
        self.head = head
