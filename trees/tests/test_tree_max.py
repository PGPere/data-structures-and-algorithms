import pytest
from binary_tree.binary_tree import BinaryTree, Node


# @pytest.mark.skip("TODO")
def test_max_val():
    tree = BinaryTree()
    tree.root = Node(10)
    tree.root.left = Node(30)
    tree.root.right = Node(-7)

    actual = tree.find_maximum_value()
    expected = 30

    assert actual == expected


# @pytest.mark.skip("TODO")
def test_max1_val():
    tree = BinaryTree()
    tree.root = Node(-1500)
    tree.root.left = Node(-2500)
    tree.root.right = Node(0)

    actual = tree.find_maximum_value()
    expected = 0

    assert actual == expected


# @pytest.mark.skip("TODO")
def test_max2_val():
    tree = BinaryTree()
    tree.root = Node(-15)
    tree.root.left = Node(25)
    tree.root.right = Node(-1)

    actual = tree.find_maximum_value()
    expected = 25

    assert actual == expected

# @pytest.mark.skip("TODO")


def test_max3_val():
    tree = BinaryTree()
    tree.root = Node(100)
    tree.root.left = Node(101)
    tree.root.right = Node(102)

    actual = tree.find_maximum_value()
    expected = 102

    assert actual == expected
