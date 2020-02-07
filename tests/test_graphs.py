from graphs.graph import Node, Graph, BinaryNode, BinaryTree

def test_binary_tree():
    BST = BinaryTree()
    BST.insert_node(12)
    BST.insert_node(10)
    BST.insert_node(14)
    assert BST.root.right.val == 14
    assert BST.root.left.val == 10
    BST.insert_node(24)
    BST.insert_node(50)
    BST.insert_node(-121)
    assert BST.root.left.left.val == -121
    assert BST.root.val == 12
    assert BST.search_node(12)
    assert not BST.search_node(52)