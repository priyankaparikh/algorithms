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

    def preorder(self):
        if self:
            print(f'{self.val}')
            if self.left:
                self.left.preorder()
            if self.right:
                self.right.preorder()

    def postorder(self):
        if self:
            if self.left:
                self.left.postorder()
            if self.right:
                self.right.postorder()
            print(f'{self.val}')


    def inorder(self):
        if self:
            if self.left:
                self.left.inorder()
            print(f'{self.val}')
            if self.right:
                self.right.inorder()

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

    def preorder(self):
        print('preorder')
        self.root.preorder()

    def postorder(self):
        print('postorder')
        self.root.postorder()

    def inorder(self):
        print('inorder')
        self.root.inorder()

    def delete_node(self):
        pass


###############################################################################
# Trie implementation without trie nodes.

class Trie(object):

    def __init__(self, root=None):
        """
        Initialize your data structure here.
        """
        self.root = {}

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        curr_node = self.root

        for char in word:
            if not char in curr_node:
                curr_node[char] = {}
            curr_node = curr_node[char]
        curr_node["*"] = {}

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        curr_node = self.root

        for char in word:
            if char not in curr_node:
                return False
            curr_node = curr_node[char]
        return '*' in curr_node

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        curr_node = self.root

        for char in prefix:
            if char not in curr_node:
                return False
            curr_node = curr_node[char]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)


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