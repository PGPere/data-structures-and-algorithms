from multiprocessing.sharedctypes import Value


class BinaryTree:

    def __init__(self):
        self.root = None

    def pre_order(self):

        def traverse(root):

            if not root:
                return

            values.append(root.value)

            traverse(root.left)

            traverse(root.right)

        values = []

        traverse(self.root)

        return values

    def in_order(self):

        def traverse(root):

            if not root:
                return

            traverse(root.left)

            values.append(root.value)

            traverse(root.right)

        values = []

        traverse(self.root)

        return values

    def post_order(self):

        def traverse(root):

            if not root:
                return

            traverse(root.left)

            traverse(root.right)

            values.append(root.value)

        values = []

        traverse(self.root)

        return values

    def find_maximum_value(self):

        def traverse(root):

            if not root:
                return

            values.append(root.value)

            traverse(root.left)

            traverse(root.right)

        values = []

        traverse(self.root)

        return max(values)


class Node:

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        return f"Node{self.value}"
