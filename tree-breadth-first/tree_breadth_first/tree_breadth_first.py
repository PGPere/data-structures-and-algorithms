from tree_breadth_first.binary_tree import BinaryTree
from tree_breadth_first.queue import Queue


def breadth_first(tree):

    q = Queue()
    output = []

    if tree.root is None:
        return output

    q.enqueue(tree.root)

    while not q.is_empty():

        tree.root = q.dequeue()

        output.append(tree.root.value)

        if tree.root.left is not None:

            q.enqueue(tree.root.left)

        if tree.root.right is not None:

            q.enqueue(tree.root.right)

    return output
