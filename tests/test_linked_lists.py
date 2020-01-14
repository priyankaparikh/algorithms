from linked_lists.single_link import Node, Linked_list
import mock


def test_node():
    node = Node(12)
    assert node.value == 12
    assert node.next == None

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

    ll.insert_node_at_start('friend')
    assert ll.get_head() == 'friend'
    #
    # assert ll.search_node('pete') == True
    # assert ll.search_node('priyanka') == False

    ll.insert_node_idx('priyanka', 3)
    assert ll.get_tail() == 'priyanka'
