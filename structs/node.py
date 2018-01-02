class Node:
    """
    A node is a store of data with methods/attributes to access
    other nodes along vertices.
    """
    left = right = parent = None
    def __init__(self, data):
        self.data = data
