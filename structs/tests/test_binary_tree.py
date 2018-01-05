import nose
import mock
import random
from binary_tree import BinaryTree

class TestCaseBinaryTree:
    def test_init(self):
        sequence = [11, 6, 8, 19, 4, 10, 5, 17, 43, 49, 31]
        bt = BinaryTree(sequence)

    def test_traverse(self):
        sequence = [11, 6, 8, 19, 4, 10, 5, 17, 43, 49, 31]
        bt = BinaryTree(sequence)
        for node in bt.traverse():
            print node.data

    def test_traverse_count(self):
        sequence = [11, 6, 8, 19, 4, 10, 5, 17, 43, 49, 31]
        bt = BinaryTree(sequence)
        traverse_count = len(list(bt.traverse()))
        assert(traverse_count == len(sequence))

    def test_traverse_order_is_preorder(self):
        sequence = [11, 6, 8, 19, 4, 10, 5, 17, 43, 49, 31]
        bt = BinaryTree(sequence)
        traversed_order = [node_.data for node_ in bt.traverse()]
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

    def test_find_largest(self):
        sequence = [11, 6, 8, 19, 4, 10, 5, 17, 43, 49, 31]
        bt = BinaryTree(sequence)
        actual = bt.find_largest()
        expected = max(sequence)
        assert(expected==actual.data)

    def test_find_largest_2(self):
        sequence = random.sample(range(1, 10000), 999)
        bt = BinaryTree(sequence)
        actual = bt.find_largest()
        expected = max(sequence)
        assert(expected==actual.data)

    def test_find_smallest(self):
        sequence = [11, 6, 8, 19, 4, 10, 5, 17, 43, 49, 31]
        bt = BinaryTree(sequence)
        actual = bt.find_smallest()
        expected = min(sequence)
        assert(expected==actual.data)

    def test_find_smallest_2(self):
        sequence = random.sample(range(1, 10000), 999)
        bt = BinaryTree(sequence)
        actual = bt.find_smallest()
        expected = min(sequence)
        assert(expected==actual.data)


class TestCaseBinaryTreeDeleteNode:
        # TODO: What happenes when replacement has more branches on its node.left?
        #TODO: Cases:
        # - replacement is node.left.right
        # - replacement has one leaf
        # - replacement node has left and that has a leaf
        # - node.left != replacement and replacement.parent.right already exists
        #^ NOT NECESSARY, p.right will always be an empty leaf after the swap & before the change
        # - Node has no parent.
        # node has a parent.
        # node has many parents

    def test_delete_node_repl_is_leaf(self):
        sequence = [11, 6, 8, 19, 4, 10, 5, 17, 43, 49, 31]
        bt = BinaryTree(sequence)
        delete_node = list(bt.traverse())[-0] # del node is 11, replacement is 10
        bt.delete(delete_node)
        expected = [10, 6, 4, 5, 8, 19, 17, 43, 31, 49]
        actual = [node_.data for node_ in bt.traverse()]
        print expected, actual
        assert(expected == actual)

    def test_delete_node_repl_is_node_left(self):
        # Repl. node is node.left & has many parents, 
        sequence = [11, 6, 8, 19, 4, 10, 5, 17, 43, 49, 31]
        bt = BinaryTree(sequence)
        delete_node = list(bt.traverse())[-3] # del node is 43, replacement is 31
        bt.delete(delete_node)
        expected = [11, 6, 4, 5, 8, 10, 19, 17, 31, 49]
        actual = [node_.data for node_ in bt.traverse()]
        print expected, actual
        assert(expected == actual)

    def test_delete_node_repl_is_not_leaf(self):
        # Repl. node is not a leaf; has one leaf
        sequence = [11, 6, 8, 19, 4, 10, 5, 17, 43, 49, 31,28]
        bt = BinaryTree(sequence)
        delete_node = list(bt.traverse())[-4] # del node is 43, replacement is 31
        bt.delete(delete_node)
        expected = [11, 6, 4, 5, 8, 10, 19, 17, 31, 28, 49]
        actual = [node_.data for node_ in bt.traverse()]
        print expected, actual
        assert(expected == actual)

    def test_delete_node_repl_has_left_which_has_leaf(self):
        # Repl. node is not a leaf; has left which has a leaf
        sequence = [11, 6, 8, 19, 4, 10, 5, 17, 43, 49, 31,28,20]
        bt = BinaryTree(sequence)
        delete_node = list(bt.traverse())[-5] # del node is 43, replacement is 31
        bt.delete(delete_node)
        expected = [11, 6, 4, 5, 8, 10, 19, 17, 31, 28, 20, 49]
        actual = [node_.data for node_ in bt.traverse()]
        print expected, actual
        assert(expected == actual)


    def test_delete_node_repl_is_left_right(self):
        # Repl. node is node.left.right
        sequence = [11, 6, 8, 19, 4, 10, 5, 17, 43, 49, 31,37]
        bt = BinaryTree(sequence)
        delete_node = list(bt.traverse())[-4] # del node is 43, replacement is 31
        bt.delete(delete_node)
        expected = [11, 6, 4, 5, 8, 10, 19, 17, 37, 31, 49]
        actual = [node_.data for node_ in bt.traverse()]
        print expected, actual
        assert(expected == actual)

    def test_delete_node_random_samples_low_node_count(self):
        # Repl. node is node.left.right
        for i in range(1000):
            num_nodes = 10
            sequence = random.sample(range(1, 100), num_nodes)
            bt = BinaryTree(sequence)
            del_idx = random.choice(range(num_nodes))
            delete_node = list(bt.traverse())[del_idx]
            print 'delete node, sequence, preorder', delete_node.data, del_idx, sequence, [node_.data for node_ in bt.traverse()]
            bt.delete(delete_node)
            expected = num_nodes -1
            actual = len(list(bt.traverse()))
            print [node_.data for node_ in bt.traverse()]
            assert(expected == actual)
            assert(delete_node.data not in list(bt.traverse()))
            assert(bt.root)

    def test_delete_node_repl_is_left_right(self):
        # Repl. node is node.left.right
        sequence = [11, 6, 8, 19, 4, 10, 5, 17, 43, 49, 31,37]
        bt = BinaryTree(sequence)
        delete_node = list(bt.traverse())[-4] # del node is 43, replacement is 31
        bt.delete(delete_node)
        expected = [11, 6, 4, 5, 8, 10, 19, 17, 37, 31, 49]
        actual = [node_.data for node_ in bt.traverse()]
        print expected, actual
        assert(expected == actual)

    def test_delete_node_random_samples_high_node_count(self):
        # Repl. node is node.left.right
        for i in range(10):
            num_nodes = 1000
            sequence = random.sample(range(1, 3000), num_nodes)
            bt = BinaryTree(sequence)
            del_idx = random.choice(range(num_nodes))
            delete_node = list(bt.traverse())[del_idx]
            print 'delete node, sequence, preorder', delete_node.data, del_idx, sequence, [node_.data for node_ in bt.traverse()]
            bt.delete(delete_node)
            expected = num_nodes -1
            actual = len(list(bt.traverse()))
            print [node_.data for node_ in bt.traverse()]
            assert(expected == actual)
            assert(delete_node.data not in list(bt.traverse()))
            assert(bt.root)

    def test_delete_node_random_samples_high_node_count_2(self):
        # Repl. node is node.left.right
        for i in range(10):
            num_nodes = 10000
            sequence = random.sample(range(1, 30000), num_nodes)
            bt = BinaryTree(sequence)
            del_idx = random.choice(range(num_nodes))
            delete_node = list(bt.traverse())[del_idx]
            bt.delete(delete_node)
            expected = num_nodes -1
            actual = len(list(bt.traverse()))
            print [node_.data for node_ in bt.traverse()]
            assert(expected == actual)
            assert(delete_node.data not in list(bt.traverse()))
            assert(bt.root)

    def test_delete_node_no_node_left(self):
        # Node.left doesn't exist. Node.right becomes repl.
        sequence = [3872, 5014, 2141, 5048, 2601, 8014, 5403, 8294, 6646]
        bt = BinaryTree(sequence)
        del_idx = 3 # repl is 8014
        delete_node = list(bt.traverse())[del_idx]
        print delete_node.data, del_idx
        bt.delete(delete_node)
        expected = [3872, 2141, 2601, 5048, 8014, 5403, 6646, 8294]
        actual = [node_.data for node_ in bt.traverse()]
        print expected, actual
        assert(expected == actual)

    def test_delete_node_no_node_left_and_no_parent(self):
        # Node.left doesn't exist. No node.parent
        sequence = [5014, 5048, 8014]
        bt = BinaryTree(sequence)
        del_idx = 0 # repl is 5014
        delete_node = list(bt.traverse())[del_idx]
        print delete_node.data, del_idx
        bt.delete(delete_node)
        expected = [5048, 8014]
        actual = [node_.data for node_ in bt.traverse()]
        print expected, actual
        assert(expected == actual)

    def test_delete_node_root_right_branch_only(self):
        sequence = [5014, 5048]
        bt = BinaryTree(sequence)
        del_idx = 0 # repl is 5014
        delete_node = list(bt.traverse())[del_idx]
        print delete_node.data, del_idx
        bt.delete(delete_node)
        expected = [5048]
        actual = [node_.data for node_ in bt.traverse()]
        print expected, actual
        assert(expected == actual)

    def test_delete_node_root_left_branch_only(self):
        sequence = [5014, 5013]
        bt = BinaryTree(sequence)
        del_idx = 0 # repl is 5014
        delete_node = list(bt.traverse())[del_idx]
        print delete_node.data, del_idx
        bt.delete(delete_node)
        expected = [5013]
        actual = [node_.data for node_ in bt.traverse()]
        print expected, actual
        assert(expected == actual)

