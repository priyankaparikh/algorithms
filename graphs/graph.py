"""Test driven implement of a Binary tree structure."""
class BinaryNode():
    def __init__(self, val, right=None, left=None):
        self.val = val
        self.right = right
        self.left = left

    def insert(self, val):
        if self.val == val:
            return self.val
        # if the value of the node that needs to be inserted is less than the new node then
        # we want to insert the new node in the left side of the tree
        elif self.val > val:
            if not self.left:
                self.left = BinaryNode(val)
            else:
                self.left.insert(val)
        # if the value of the new node is greater than the root then we want to insert the new
        # node to the right side of the tree
        elif self.val < val:
            if not self.right:
                self.right = BinaryNode(val)
            else:
                self.right.insert(val)

    def find(self, val):
        if self.val == val:
            return True
        elif self.val < val:
            if self.right:
                self.right.find(val)
            else:
                return False
        elif self.val > val:
            if self.left:
                self.left.find(val)
            else:
                return False


class BinaryTree():
    def __init__(self, root=None):
        self.root = root

    def insert_node(self, val):
        if self.root:
            self.root.insert(val)
        else:
            self.root = BinaryNode(val)

    def search_node(self, val):
        if self.root:
            return self.root.find(val)
        else:
            return False

    def delete_node(self):
        pass

    def traverse_tree(self):
        pass


###################################################################################

"""python test driven implement of a graph data structure.
    NOTES:
        there are two types of graphs: directed and undirected.
        there are two types of graph implementations: if the nodes are
        weighted, the graph can be implemented using a two dimensional matrix
        (graph adjacency matrix).I f the graph is a directed structure a
        graPH adjacency list can be used.
        there are two types of search methods: bfs, dfs"""

class Node():
    def __init__(self, n):
        self.name = n
        self.neighbours = list()


class Graph():
    def __init__(self):
        pass