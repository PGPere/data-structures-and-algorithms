from unittest import TestResult
from binary_tree.binary_tree import BinaryTree
from binary_tree.binary_tree import Node


class BinarySearchTree(BinaryTree):

    def __init__(self):
        self.root = None

    def add(self, value):
        node = Node(value)

        if not self.root:
            self.root = node
            return

        def traverse(root, node):
            if not root:
                return

            if node.value < root.value:
                if root.left:
                    traverse(root.left, node)
                else:
                    root.left = node
            else:
                if root.right:
                    traverse(root.right, node)
                else:
                    root.right = node

        traverse(self.root, node)

    def contains(self, value):

        if self.root is None:
            return False

        def check(value):

            if self.root.value < value:
                self.root = self.root.right

            if self.root.value > value:
                self.root = self.root.left

        check(value)

        if self.root.value == value:
            return True

        if self.root.value != value:
            return False
