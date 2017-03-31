class CircularReference(Exception):
    pass
class IsEmpty(Exception):
    pass
class NotFound(Exception):
    pass

class SinglyLinkedList(object):
    def __init__(self):
        self.head = None

    def __iter__(self):
        """ Iterate over all nodes"""
        i = self.head
        while True:
            if not i:
                break
            yield i
            i = i.next
            if not i:
                break

    def insert_beg(self,node):
        """ Add a new node to head """
        if self.head == node:
            raise CircularReference(
                'Head and next can not be the same ref'
            )

        node.next = self.head
        self.head = node

    def insert_end(self,node):
        i = self.head
        while True:
            if not i.next:
                i.next = node
                break
            i = i.next

    def insert_after(self,node,new_node):
        """ Insert new node after a certain node"""
        new_node.next = node.next
        node.next = new_node
    def delete(self,del_node,start_node=None):
        """ Remove reference to del_node, start looking from start_node.
            Special cases:
            -If no start_node start from head
            -If start_node is del_node, start from head because we
             need to get the previous node in order to not break the chain
            -If deleting head, reassing head
            -If node not found, raise exception
        """
        if not self.head:
            raise IsEmpty(
                "There are no nodes."
            )

        elif self.head == del_node:
            self.head = self.head.next
            return

        elif start_node == del_node or not start_node:
            start_node = self.head

        start = start_node
        next_node = start_node.next

        while True:
            if next_node == del_node:
                start.next = start.next.next
                return
            elif not next_node:
                raise NotFound("Can't find node")
            start = next_node
            next_node = next_node.next
    def print_nodes(self):
        i = self.head
        while True:
            print i.data
            i = i.next
            if not i:
                break

class Node(object):
    def __init__(self,obj):
        self.data = obj
        self.next = None

