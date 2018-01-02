import nose
import mock
from binary_tree import BinaryTree

class TestCaseBinaryTree:
    def test_init(self):
        sequence = [11, 6, 8, 19, 4, 10, 5, 17, 43, 49, 31]
        bt = BinaryTree(sequence)

    def test_traverse(self):
        sequence = [11, 6, 8, 19, 4, 10, 5, 17, 43, 49, 31]
        bt = BinaryTree(sequence)
        for node in bt.traverse():
            print node

    def test_traverse_count(self):
        sequence = [11, 6, 8, 19, 4, 10, 5, 17, 43, 49, 31]
        bt = BinaryTree(sequence)
        traverse_count = len(list(bt.traverse()))
        assert(traverse_count == len(sequence))

    def test_traverse_order_is_preorder(self):
        sequence = [11, 6, 8, 19, 4, 10, 5, 17, 43, 49, 31]
        bt = BinaryTree(sequence)
        traversed_order = list(bt.traverse())
        expected_order = [11, 6, 4, 5, 8, 10, 19, 17, 43, 31, 49]
        assert(traversed_order==expected_order)

    @mock.patch('binary_tree.BinaryTree.traverse_from')
    def test_traverse_traverse_from_called(self,mock_trav_from):
        sequence = [11, 6, 8, 19, 4, 10, 5, 17, 43, 49, 31]
        bt = BinaryTree(sequence)
        bt.traverse().next()
        mock_trav_from.assert_called()

    @nose.tools.raises(StopIteration)
    def test_traverse_from_returns_none(self):
        sequence = [11, 6, 8, 19, 4, 10, 5, 17, 43, 49, 31]
        bt = BinaryTree(sequence)
        actual = bt.traverse_from(None)
        actual.next()
