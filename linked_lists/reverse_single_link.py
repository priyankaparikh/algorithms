""" Reverse a single linked list iteratively and recursively """

class Node():
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


class List():
    def __init__(self, head):
        self.head = head

    def reverse_it(self):
        """iteratively reverse the linked list"""
        curr = self.head
        prev = None

        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        self.head = prev


    def reverse_rec(self, node):
        """ recursively reverse a linked list"""
        pass