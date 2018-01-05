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
        yield node
        if node.left:
            # TODO: Replace for loop with 'yield from' in python 3
            for node_ in self.traverse_from(node.left):
                yield node_
        if node.right:
            # TODO: Replace for loop with 'yield from' in python 3
            for node_ in self.traverse_from(node.right):
                yield node_

    def find_largest(self,from_node=None):
        if not from_node:
            from_node = self.root
        while from_node.right:
            from_node = from_node.right
        return from_node

    def find_smallest(self,from_node=None):
        if not from_node:
            from_node = self.root
        while from_node.left:
            from_node = from_node.left
        return from_node

    def delete(self, node):
        """
        Delete node from tree. This is performed by finding the largest
        node from the left subtree (if it exists), and inserting it where
        the current node is to be deleted. There are different situations
        a node can be in.. for example:

        - A node can have both left and right children, along with many
          sub-children
        - A node can have one child (left or right) along with many
          sub-children
        - A node can be a leaf node with only a parent connection
        - A node can be the root of the tree
        - A node only has a right subtree
        - The replacement node is node's left child, or is not it's left
          child

        The toughest of these, is when there are both left and right branches.
        The hard implementation aspect of this is actually managing the branches
        of both the deletion node, it's parent, and it's replacement. I originally
        tried to write logic for this, and it became hard to read. Instead, a
        "trick" exists which works in the general case. It goes like this:

        * Write code to implement deletion of 1 or 0 child branches
          (^ this is straight-forward)
        * In the case that the delete node has both left and right child branches:
        * Find the replacement
        * SWAP the replacement data with the delete node
        * Delete the replacement node which will only have 1 child branch.

        By design, the replacement node should always have only 1 or 0 child
        branch. This trick let's you get away with not having to manage all
        the branches of each node involved when it is most inconvenient, and
        is much more readable.

        :param node: The node to be deleted.
        """

        if node.left and node.right:
            replacement = self.find_largest(from_node=node.left)
            node.data = replacement.data
            self.delete(replacement)


        elif not node.left and not node.right:
            if node.parent:
                if node.parent.data >= node.data:
                    node.parent.left = None
                else:
                    node.parent.right = None
            else:
                replacement.parent = None
                self.root = replacement

        elif node.left and not node.right:
            replacement = node.left
            if node.parent:
                if node.parent.left == node:
                    node.parent.left = replacement
                else:
                    node.parent.right = replacement
                replacement.parent = node.parent
            else:
                replacement.parent = None
                self.root = replacement

            #replacement = self.find_largest(from_node=node.left)
            #self.update_parent_branch(node,replacement)

        elif node.right and not node.left:
            replacement = node.right
            if node.parent:
                if node.parent.left == node:
                    node.parent.left = replacement
                else:
                    node.parent.right = replacement
                replacement.parent = node.parent
            else:
                replacement.parent = None
                self.root = replacement


