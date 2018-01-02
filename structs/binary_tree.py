from node import Node
class BinaryTree:
    """
    A binary tree is made up of nodes, where each node has links of up to
    two children (left, right) and a parent node.
    This class takes an array of numbers, initializes all the nodes, and
    builds the tree structure. The tree is built by recursively inserting and
    initializing nodes with no children (called leaves), until none are left.
    The nodes are inserted by setting the node to the left or right attribute
    of the current node (and the parent attrinbute is set on the node).
    This also tree offers methods like: search, traversal (an iterator), merge

    :param root: The root node. The very first node given from a sequence.
    """
    root = None
    node_count = 0
    def __init__(self,data_sequence):
        """ Run the load_tree method to the data into the tree.

        :param data_sequence: The list of sorted or unsorted numbers to store
        Each data_array element should be floats or integers.
        """
        for value in data_sequence:
            self.insert(value)

    def insert(self, value):
        """ Check if root node exists, then set root or insert node into tree.

        :param value: an integer or float
        """
        if not self.root:
            self.root = Node(value)
        else:
            self.insert_node(self.root, value)
        self.node_count += 1

    def insert_node(self,current_node, value):
        """
        Recursively try to insert node into tree until no left or right
        nodes are found on current nod. Then, initialize the node and set
        parent.

        :param value: An integer or float
        """
        if value <= current_node.data:
            if current_node.left:
                self.insert_node(current_node.left, value)
            else:
                current_node.left = Node(value)
                current_node.left.parent = current_node
        elif value > current_node.data:
            if current_node.right:
                self.insert_node(current_node.right, value)
            else:
                current_node.right = Node(value)
                current_node.right.parent = current_node

    def traverse(self):
        """
        Perform a pre-order traversal of the entire tree
        """
        return self.traverse_from(self.root)

    def traverse_from(self,node):
        """
        Perform the pre-order traversal of tree starting at a node.

        :param node: A node to start traversing from. Every level and child below
        this node will be traversed (including this node).
        """
        if not node:
            return
        yield node.data
        if node.left:
            for node_ in self.traverse_from(node.left):
                yield node_
        if node.right:
            for node_ in self.traverse_from(node.right):
                yield node_

