from node import RBNode
from binary_tree import BinaryTree

class RedBlackTree(BinaryTree):
    """
        A Red Black tree is a form of binary tree with additional properties.

        The 5 properties that makeup a red black tree are:
        1. Every node has a color of either red or black
        2. The root node must be black
        3. Every leaf node is black
        4. If a node is red, then both left and right children are black
        5. For every node, all paths from the node to descendant leaves
           contain the same number of black nodes
    """
    def __str__(self):
        """
        Show the tree structure by printing nodes at each height of tree
        """
        all_nodes = self.traverse()
        height = self.get_height()
        tree_levels = [[] for i in range(height)]
        for node in all_nodes:
            node_idx = height - self.get_height(node)
            tree_levels[node_idx].append(node)

        tree_str = ''
        for level in tree_levels:
            nodes = str([(node_.color, node_.data) for node_ in level])
            tree_str = '\n'.join([tree_str,nodes])
        return tree_str


    def left_rotate(self,node):
        """
        Rotate a node's right child (other_node) into node, while preserving BST
        properties. Other_node will take the place of node and all of it's
        connections. Node will become the child of other_node.

        :param node: A node that has a right child.
        """
        other_node = node.right

        # Reset other_node's children/parent connections
        node.right = other_node.left
        if other_node.left:
            other_node.left.parent = node
        other_node.parent = node.parent

        # Reset connection for node.parent
        # Node is root case
        if not node.parent:
            self.root = other_node
        # Node is left/right of its parent cases
        elif node == node.parent.left:
            node.parent.left = other_node
        elif node == node.parent.right:
            node.parent.right = other_node

        # Now set node to be child of node.right
        other_node.left = node
        node.parent = other_node

    def right_rotate(self,node):
        """
        Rotate a node's left child (other_node) into node, while preserving BST
        properties. Other_node will take the place of node and all of it's
        connections. Node will become the child of other_node.

        :param node: A node that has a left child.
        """
        other_node = node.left

        # Reset other_node's children/parent connections
        node.left = other_node.right
        if other_node.right:
            other_node.right.parent = node
        other_node.parent = node.parent

        # Reset connection for node.parent
        # Node is root case
        if not node.parent:
            self.root = other_node
        # Node is left/right of its parent cases
        elif node == node.parent.left:
            node.parent.left = other_node
        elif node == node.parent.right:
            node.parent.right = other_node

        # Now set node to be child of node.right
        other_node.right = node
        node.parent = other_node

    def insert(self, value):
        """ Check if root node exists, then set root or insert node into tree.

        :param value: an integer or float
        """
        if not self.root:
            self.root = RBNode(value)
            self.root.color = 'black'
        else:
            self.insert_node(self.root, value)
        self.node_count += 1

    def insert_node(self, current_node, value):
        """
        Inserting a node into a red black tree is the simple insert method
        for a basic binary tree, just additional steps are needed to maintain
        the properties of the red black tree data structure.

        :param node: A rb node (has color property)
        """

        node = RBNode(value)
        # Traverse until leaf node
        while current_node:
            # Keep a reference to the last non-None node, to be used later.
            # current_node will always be set to None once this loop is broken.
            node_to_use = current_node
            if node.data <= current_node.data:
                current_node = current_node.left
            else:
                current_node = current_node.right

        # Set parent & l/r connections
        node.parent = node_to_use
        if not node_to_use:
            self.root = node
        elif node.data <= node_to_use.data:
            node_to_use.left = node
        else:
            node_to_use.right = node

        # Default color set to red
        node.color = 'red'
        # Fix any red-black tree violations
        self.fix_colors(node)

    def fix_colors(self,node):
        """ """
