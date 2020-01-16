from linked_lists.single_link import Node, Linked_list


def test_node():
    node = Node(12)
    assert node.value == 12
    assert not node.next

def test_node_functions():
    node = Node(13, 'apple')
    assert node.get_data() == 13
    assert node.get_next() == 'apple'
    node2 = Node(14, 'banana')
    node.set_next(node2)
    assert node.next == node2

def test_linked_list():
    node1 = Node('apple')
    node2 = Node('banana', node1)
    node3 = Node('cabbage', node2)

    ll = Linked_list(node3)

    assert ll.get_head() == 'cabbage'
    assert ll.get_tail() == 'apple'


def test_list_insertions():
    node1 = Node('apple')
    node2 = Node('banana', node1)
    node3 = Node('cabbage', node2)

    ll = Linked_list(node3)

    ll.add_at_head('raddish')
    assert ll.head.value == 'raddish'

    ll.add_at_tail('bazooka')
    assert ll.get_tail() == 'bazooka'

def test_list_search():
    node1 = Node('apple')
    node2 = Node('banana', node1)
    node3 = Node('cabbage', node2)
    node4 = Node('raddish', node3)

    ll = Linked_list(node4)

    # test list terms
    assert ll.get_node('cabbage')
    assert not ll.get_node('friend')

    # test list search using index
    assert ll.get_node(idx=1) == 'raddish'
    assert ll.get_node(idx=3) == 'banana'

    # test list insertions
    ll.insert_node('pineapple', 2)
    ll.insert_node('fresh', 3)

    assert ll.get_node(idx=3) == 'fresh'
    assert ll.get_node(idx=2) == 'pineapple'
