import nose
import mock
import random
from rb_tree import RedBlackTree

class TestCaseRedBlackTreeInit:
    def test_rb_tree_init(self):
        sequence = [87, 55, 107, 93, 120]
        bt = RedBlackTree(sequence)
        print bt

class TestCaseRedBlackBinaryTreeRotations:
    def test_left_rotate_root_example(self):
        # Left rotate 107 into 87, check the pre-order traversal afterwards
        sequence = [87, 55, 107, 93, 120]
        bt = RedBlackTree(sequence)
        rotate_node = bt.root # 87 (107 will be root after rotate)
        bt.left_rotate(rotate_node)
        nodes = [node_.data for node_ in bt.traverse()]
        expected = [107, 87, 55, 93, 120]
        actual = [node_.data for node_ in bt.traverse()]
        assert(expected == actual)

    def test_left_rotate_not_root_example(self):
        # Left rotate 120 into 107, check the pre-order traversal afterwards
        sequence = [87, 55, 107, 93, 120]
        bt = RedBlackTree(sequence)
        rotate_node = bt.root.right # 107 (120 will be parent after rotate)
        bt.left_rotate(rotate_node)
        nodes = [node_.data for node_ in bt.traverse()]
        expected = [87, 55, 120, 107, 93]
        actual = [node_.data for node_ in bt.traverse()]
        assert(expected == actual)

    def test_left_rotate_root_check(self):
        # Root should now be 107; 87 shouldn't be root
        sequence = [87, 55, 107, 93, 120]
        bt = RedBlackTree(sequence)
        rotate_node = bt.root # 87 (107 will be root after rotate)
        bt.left_rotate(rotate_node)
        nodes = [node_.data for node_ in bt.traverse()]
        assert(bt.root != rotate_node)
        assert(bt.root.data == 107)


    @nose.tools.raises(AttributeError)
    def test_left_rotate_no_right_child(self):
        # Because there is no node.right child to rotate into node, this should
        # raise an exception.
        sequence = [87, 55,]
        bt = RedBlackTree(sequence)
        rotate_node = bt.root # 87
        bt.left_rotate(rotate_node)

    def test_left_rotate_no_left_child(self):
        # Rotate node Having no left child shouldn't raise an exception.
        sequence = [87, 97,]
        bt = RedBlackTree(sequence)
        rotate_node = bt.root # 87
        bt.left_rotate(rotate_node)

    def test_right_rotate_root_example(self):
        # Right rotate 55 into 87, check the pre-order traversal afterwards
        sequence = [87, 55, 107, 93, 120]
        bt = RedBlackTree(sequence)
        rotate_node = bt.root # 87 (55 will be root after rotate)
        bt.right_rotate(rotate_node)
        nodes = [node_.data for node_ in bt.traverse()]
        expected = [55, 87, 107, 93, 120]
        actual = [node_.data for node_ in bt.traverse()]
        print actual
        assert(expected == actual)

    def test_right_rotate_not_root_example(self):
        # right rotate 93 into 107, check the pre-order traversal afterwards
        sequence = [87, 55, 107, 93, 120]
        bt = RedBlackTree(sequence)
        rotate_node = bt.root.right # 107 (93 will be parent after rotate)
        bt.right_rotate(rotate_node)
        nodes = [node_.data for node_ in bt.traverse()]
        expected = [87, 55, 93, 107, 120]
        actual = [node_.data for node_ in bt.traverse()]
        assert(expected == actual)

    def test_right_rotate_root_check(self):
        # Root should now be 55; 87 shouldn't be root
        sequence = [87, 55, 107, 93, 120]
        bt = RedBlackTree(sequence)
        rotate_node = bt.root # 87 (55 will be root after rotate)
        bt.right_rotate(rotate_node)
        nodes = [node_.data for node_ in bt.traverse()]
        assert(bt.root != rotate_node)
        assert(bt.root.data == 55)


    def test_right_rotate_no_right_child(self):
        # Right rotate should work without a right child, shouldn't raise exc
        sequence = [87, 55,]
        bt = RedBlackTree(sequence)
        rotate_node = bt.root # 87
        bt.right_rotate(rotate_node)

    @nose.tools.raises(AttributeError)
    def test_right_rotate_no_left_child(self):
        # Right Rotate node having no left child should raise an exception.
        sequence = [87, 97,]
        bt = RedBlackTree(sequence)
        rotate_node = bt.root # 87 (107 will be root after rotate)
        bt.right_rotate(rotate_node)
