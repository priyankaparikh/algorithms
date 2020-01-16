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
        curr = self.head

        while curr.next:
            curr = curr.next

        return curr.value

    def add_at_head(self, value):
        """ A node to the head of the linked list"""

        temp = self.head
        self.head = Node(value, temp)

    def add_at_tail(self, value):
        """ A node to the end of the linked list"""

        curr = self.head

        while curr.next:
            curr = curr.next

        temp = Node(value)
        curr.next = temp

    def get_node(self, search_term=None, idx=None):
        """ Iteratively search for a node within the link list"""

        curr = self.head
        count = 1

        while curr:
            if curr.value == search_term:
                return True
            if count == idx:
                return curr.value
            curr = curr.next
            count += 1

        return False


    def print_nodes(self):
        curr = self.head

        while curr:
            print(curr.value)
            curr = curr.next


    def insert_node(self, value, idx):
        """Insert a node of a given value or at an index"""

        curr = self.head
        count = 1
        new_node = Node(value)

        while curr and count <= idx:
            if count == (idx-1):
                temp = curr.next
                curr.next = new_node
                curr.next.next = temp
            self.print_nodes()
            curr = curr.next
            count += 1

