from tree_breadth_first.binary_tree import BinaryTree
from tree_breadth_first.queue import Queue


def breadth_first(tree):

    q = []

    q.enqueue(tree.root.value)

    while not q.is_empty():

        tree.root.value = q.dequeue()

        if tree.root.left is not None:

            q.enqueue(tree.root.left)

        if tree.root.right is not None:

            q.enqueue(tree.root.right)
