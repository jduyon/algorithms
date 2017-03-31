from nose.plugins import cover
import mock
from mock import call
import nose.tools as nt
from nose.plugins.attrib import attr
from linked_list import SinglyLinkedList, Node
from linked_list import CircularReference,IsEmpty,NotFound


class TestCaseLinkedLists:
    def setUp(self):
        pass
    def tearDown(self):
        pass

    def test_sll_base(self):
        """ Test simple use case for single linked list """
        sll = SinglyLinkedList()
        a = Node('a')
        b = Node('b')
        sll.insert_beg(a)
        sll.insert_beg(b)

    @nt.raises(CircularReference)
    def test_add_circular_node_sll(self):
        """
            Head and next should never be the same (otherwise we have
            a circular loop).
        """
        sll = SinglyLinkedList()
        a = Node('a')
        sll.insert_beg(a)
        sll.insert_beg(a)

    def test_iter_sll_base(self):
        """ Test that you can iterate over SLL"""
        sll = SinglyLinkedList()
        a = Node('a')
        b = Node('b')
        sll.insert_beg(a)
        sll.insert_beg(b)
        for i in sll:
            print i
    def test_iter_empty_sll(self):
        """ If empty SLL, no exception should be raise"""
        sll = SinglyLinkedList()
        a = Node('a')
        sll.insert_beg(a)
        sll.delete(a,a)
        print [i for i in sll]
    def test_iter_sll_twice(self):
        """ Calling __iter__ shouldn't alter the SLL object """
        sll = SinglyLinkedList()
        a = Node('a')
        b = Node('b')
        sll.insert_beg(a)
        sll.insert_beg(b)
        actual = "".join(i.data for i in sll)
        expected = "".join(i.data for i in sll)
        assert(actual==expected)

    def test_insert_end(self):
        """ Adding a node with insert_end should put it at the end"""
        sll = SinglyLinkedList()
        a = Node('a')
        b = Node('b')
        c = Node('c')
        sll.insert_beg(a)
        sll.insert_end(b)
        sll.insert_beg(c)
        actual = [i.data for i in sll][-1]
        expected = 'b'
        assert(actual==expected)

    def test_delete_sll_next_node(self):
        """ Delete the next node"""
        sll = SinglyLinkedList()
        a = Node('a')
        b = Node('b')
        c = Node('c')
        sll.insert_beg(a)
        sll.insert_beg(b)
        sll.insert_beg(c)
        sll.delete(a,start_node=b)
        actual = [i.data for i in sll]
        expected = 'a'
        nt.assert_not_in(expected,actual)


    def test_delete_sll_next_next_node(self):
        """ Delete a node"""
        sll = SinglyLinkedList()
        a = Node('a')
        b = Node('b')
        c = Node('c')
        d = Node('d')
        sll.insert_beg(a)
        sll.insert_beg(b)
        sll.insert_beg(c)
        sll.insert_beg(d)
        sll.delete(a,start_node=c)
        actual = [i.data for i in sll]
        expected = 'a'
        nt.assert_not_in(expected,actual)

    def test_delete_sll_next_next_node(self):
        """ Delete a node"""
        sll = SinglyLinkedList()
        a = Node('a')
        b = Node('b')
        c = Node('c')
        d = Node('d')
        sll.insert_beg(a)
        sll.insert_beg(b)
        sll.insert_beg(c)
        sll.insert_beg(d)
        sll.delete(a,start_node=c)
        actual = [i.data for i in sll]
        expected = 'a'
        nt.assert_not_in(expected,actual)

    def test_delete_node_sll_is_head(self):
        """
            Head should be reassigned when deleting the head node
            from singly linked.
        """
        sll = SinglyLinkedList()
        a = Node('a')
        b = Node('b')
        sll.insert_beg(a)
        sll.insert_beg(b)
        sll.delete(b,start_node=b)
        assert(sll.head)

    def test_delete_node_sll_is_start(self):
        """
            Delete a node from singly linked list that is the start arg.
        """
        sll = SinglyLinkedList()
        a = Node('a')
        b = Node('b')
        sll.insert_beg(a)
        sll.insert_beg(b)
        sll.delete(a,start_node=a)

    @nt.raises(NotFound)
    def test_delete_node_sll_not_found(self):
        """
            Try to delete a node that is not found.
        """
        sll = SinglyLinkedList()
        a = Node('a')
        b = Node('b')
        sll.insert_beg(a)
        sll.delete(b,start_node=a)
