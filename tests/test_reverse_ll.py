from linked_lists.reverse_single_link import Node, List

# original input list
node1 = Node('a')
node2 = Node('b', node1)
node3 = Node('c', node2)
node4 = Node('d', node3)
node5 = Node('e', node4)

ll = List(node5)

def test_reverse_it():
    ll.reverse_it()
    assert ll.head.value == 'a'
    assert ll.head.next.value == 'b'
    assert ll.head.next.next.value == 'c'
    assert ll.head.next.next.next.value == 'd'
    assert ll.head.next.next.next.next.value == 'e'

